"""Durable execution lineage and forensic evidence metadata.

These tables survive normal ephemeral Assistant lifecycle operations.

Foreign keys to Runs and Actions use RESTRICT, not CASCADE. Controlled
retention and erasure services must reconcile lineage before deletion.

Import this module to register its models on the shared ORM Base.
"""

from __future__ import annotations

import time

from sqlalchemy import (
    JSON,
    BigInteger,
    Boolean,
    Column,
    ForeignKey,
    Index,
    Integer,
    String,
    UniqueConstraint,
)

from .base import Base


def _now() -> int:
    return int(time.time())


def _now_us() -> int:
    return time.time_ns() // 1_000


class RunExecutionEpoch(Base):
    """One execution attempt belonging to a durable logical Run."""

    __tablename__ = "run_execution_epochs"

    id = Column(String(64), primary_key=True)

    run_id = Column(
        String(64),
        ForeignKey("runs.id", ondelete="RESTRICT"),
        nullable=False,
    )

    root_run_id = Column(
        String(64),
        ForeignKey("runs.id", ondelete="RESTRICT"),
        nullable=False,
    )

    owner_user_id = Column(String(64), nullable=False)
    epoch_number = Column(Integer, nullable=False)

    state = Column(
        String(32),
        nullable=False,
        default="reserved",
    )

    created_at = Column(BigInteger, nullable=False, default=_now)
    started_at = Column(BigInteger, nullable=True)
    last_seen_at = Column(BigInteger, nullable=True)
    ended_at = Column(BigInteger, nullable=True)
    terminal_status = Column(String(32), nullable=True)

    __table_args__ = (
        UniqueConstraint(
            "run_id",
            "epoch_number",
            name="uq_exec_epoch_run_number",
        ),
        Index(
            "ix_exec_epoch_root_created",
            "root_run_id",
            "created_at",
        ),
        Index(
            "ix_exec_epoch_owner_root",
            "owner_user_id",
            "root_run_id",
        ),
        Index(
            "ix_exec_epoch_state_seen",
            "state",
            "last_seen_at",
        ),
    )


class ExecutionActor(Base):
    """Durable actor reservation and identity snapshot.

    One actor can occupy a named slot within a Run execution epoch.
    Database uniqueness prevents competing supervisor reservations.
    """

    __tablename__ = "execution_actors"

    id = Column(String(64), primary_key=True)

    epoch_id = Column(
        String(64),
        ForeignKey(
            "run_execution_epochs.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    slot = Column(String(48), nullable=False)
    execution_role = Column(String(48), nullable=False)

    # Snapshots intentionally have no FK to assistants.
    # Assistant cleanup must not invalidate execution provenance.
    assistant_id_snapshot = Column(String(64), nullable=True)
    model_snapshot = Column(String(128), nullable=True)

    ephemeral = Column(Boolean, nullable=False, default=False)

    state = Column(
        String(32),
        nullable=False,
        default="reserved",
    )

    reserved_at = Column(BigInteger, nullable=False, default=_now)
    activated_at = Column(BigInteger, nullable=True)
    retired_at = Column(BigInteger, nullable=True)
    last_seen_at = Column(BigInteger, nullable=True)

    __table_args__ = (
        UniqueConstraint(
            "epoch_id",
            "slot",
            name="uq_exec_actor_epoch_slot",
        ),
        Index(
            "ix_exec_actor_assistant",
            "assistant_id_snapshot",
        ),
        Index(
            "ix_exec_actor_state_seen",
            "state",
            "last_seen_at",
        ),
    )


class RunDelegation(Base):
    """Links a parent Action to a delegated child execution."""

    __tablename__ = "run_delegations"

    id = Column(String(64), primary_key=True)

    parent_epoch_id = Column(
        String(64),
        ForeignKey(
            "run_execution_epochs.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    child_epoch_id = Column(
        String(64),
        ForeignKey(
            "run_execution_epochs.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    parent_action_id = Column(
        String(64),
        ForeignKey("actions.id", ondelete="RESTRICT"),
        nullable=False,
    )

    initiating_actor_id = Column(
        String(64),
        ForeignKey("execution_actors.id", ondelete="RESTRICT"),
        nullable=True,
    )

    created_at = Column(BigInteger, nullable=False, default=_now)

    __table_args__ = (
        UniqueConstraint(
            "child_epoch_id",
            name="uq_run_delegation_child_epoch",
        ),
        Index(
            "ix_run_delegation_parent",
            "parent_epoch_id",
        ),
        Index(
            "ix_run_delegation_parent_action",
            "parent_action_id",
        ),
    )


class ExecutionEvent(Base):
    """Structured, ordered execution evidence.

    Raw reasoning, credentials and unfiltered tool outputs must not be
    stored in details. The writer service must enforce an allowlist,
    redact secrets, and protect events against unauthorised mutation.

    Evidence digests require protected external checkpoints to provide
    meaningful tamper-evidence.
    """

    __tablename__ = "execution_events"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    epoch_id = Column(
        String(64),
        ForeignKey(
            "run_execution_epochs.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    actor_id = Column(
        String(64),
        ForeignKey(
            "execution_actors.id",
            ondelete="RESTRICT",
        ),
        nullable=True,
    )

    origin_run_id = Column(
        String(64),
        ForeignKey("runs.id", ondelete="RESTRICT"),
        nullable=False,
    )

    event_type = Column(String(64), nullable=False)
    schema_version = Column(Integer, nullable=False, default=1)

    evidence_class = Column(
        String(24),
        nullable=False,
        default="operational",
    )

    # Microsecond timestamps permit high-resolution reconstruction
    # of interleaved agent and tool activity.
    occurred_at_us = Column(BigInteger, nullable=False)
    recorded_at_us = Column(
        BigInteger,
        nullable=False,
        default=_now_us,
    )

    evidence_expires_at = Column(BigInteger, nullable=True)

    action_id_snapshot = Column(String(64), nullable=True)
    tool_call_id_snapshot = Column(String(64), nullable=True)

    details = Column(JSON, nullable=False, default=dict)

    # Opaque reference to governed, separately protected evidence.
    evidence_ref = Column(String(255), nullable=True)
    evidence_sha256 = Column(String(64), nullable=True)

    previous_digest = Column(String(64), nullable=True)
    record_digest = Column(String(64), nullable=True)

    __table_args__ = (
        Index(
            "ix_exec_event_epoch_id",
            "epoch_id",
            "id",
        ),
        Index(
            "ix_exec_event_origin_time",
            "origin_run_id",
            "occurred_at_us",
        ),
        Index(
            "ix_exec_event_type_time",
            "event_type",
            "occurred_at_us",
        ),
    )


class EvidenceRetentionHold(Base):
    """Authorised preservation hold for one root Run.

    An open hold blocks ordinary retention purging. Releasing a hold
    does not independently authorise deletion of otherwise protected data.
    """

    __tablename__ = "evidence_retention_holds"

    id = Column(String(64), primary_key=True)

    root_run_id = Column(
        String(64),
        ForeignKey("runs.id", ondelete="RESTRICT"),
        nullable=False,
    )

    case_reference = Column(String(128), nullable=False)
    reason_code = Column(String(48), nullable=False)
    authorised_by = Column(String(64), nullable=False)

    created_at = Column(BigInteger, nullable=False, default=_now)
    reviewed_at = Column(BigInteger, nullable=True)
    expires_at = Column(BigInteger, nullable=True)
    released_at = Column(BigInteger, nullable=True)

    __table_args__ = (
        Index(
            "ix_evidence_hold_root_released",
            "root_run_id",
            "released_at",
        ),
        Index(
            "ix_evidence_hold_case",
            "case_reference",
        ),
    )

from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    String,
    UniqueConstraint,
)

from .base import Base


class ProviderKey(Base):
    """User-owned registration of an encrypted inference credential.

    Secret material lives exclusively in the existing Credential table.
    This model stores only provider-specific metadata and a keyed
    fingerprint used for idempotent registration.
    """

    __tablename__ = "provider_keys"

    id = Column(String(64), primary_key=True)

    owner_id = Column(
        String(64),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    credential_id = Column(
        String(64),
        nullable=False,
    )

    provider = Column(String(64), nullable=False)
    name = Column(String(128), nullable=True)

    # HMAC-SHA256 hex digest, never a plain SHA256 of the secret.
    # Cleared on revocation to permit a fresh registration.
    fingerprint = Column(String(64), nullable=True)

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    revoked_at = Column(DateTime, nullable=True)

    __table_args__ = (
        ForeignKeyConstraint(
            ["credential_id", "owner_id"],
            ["credentials.id", "credentials.owner_id"],
            name="fk_provider_keys_credential_owner",
            ondelete="CASCADE",
        ),
        UniqueConstraint(
            "credential_id",
            name="uq_provider_keys_credential",
        ),
        UniqueConstraint(
            "owner_id",
            "provider",
            "fingerprint",
            name="uq_provider_keys_owner_provider_fingerprint",
        ),
        CheckConstraint(
            "(revoked_at IS NULL AND fingerprint IS NOT NULL) OR "
            "(revoked_at IS NOT NULL AND fingerprint IS NULL)",
            name="ck_provider_keys_revocation",
        ),
        Index(
            "idx_provider_keys_owner_provider",
            "owner_id",
            "provider",
        ),
    )

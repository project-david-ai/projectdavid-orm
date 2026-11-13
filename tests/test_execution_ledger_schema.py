"""Structural tests for Project David execution-lineage models."""

from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.mysql import dialect as mysql_dialect
from sqlalchemy.schema import CreateTable

from projectdavid_orm.projectdavid_orm import execution_ledger, models

EXPECTED_TABLES = {
    "run_execution_epochs",
    "execution_actors",
    "run_delegations",
    "execution_events",
    "evidence_retention_holds",
}


def test_models_share_existing_metadata():
    metadata = models.User.metadata

    assert EXPECTED_TABLES.issubset(metadata.tables.keys())


def test_supervisor_and_epoch_uniqueness():
    metadata = models.User.metadata

    expected = {
        "run_execution_epochs": "uq_exec_epoch_run_number",
        "execution_actors": "uq_exec_actor_epoch_slot",
        "run_delegations": "uq_run_delegation_child_epoch",
    }

    for table_name, constraint_name in expected.items():
        table = metadata.tables[table_name]
        names = {
            constraint.name
            for constraint in table.constraints
            if isinstance(constraint, UniqueConstraint)
        }
        assert constraint_name in names


def test_protected_foreign_keys_restrict_deletion():
    metadata = models.User.metadata

    for name in EXPECTED_TABLES:
        table = metadata.tables[name]

        assert table.foreign_keys

        for foreign_key in table.foreign_keys:
            assert foreign_key.ondelete == "RESTRICT"


def test_actor_identity_survives_assistant_deletion():
    actor_table = models.User.metadata.tables["execution_actors"]

    assistant_id = actor_table.c.assistant_id_snapshot

    # This is an identity snapshot, deliberately not a foreign key.
    assert not assistant_id.foreign_keys


def test_forensic_event_resolution():
    table = models.User.metadata.tables["execution_events"]

    assert "occurred_at_us" in table.c
    assert "recorded_at_us" in table.c
    assert "evidence_sha256" in table.c
    assert "evidence_expires_at" in table.c


def test_mysql_ddl_compiles_for_every_new_table():
    metadata = models.User.metadata
    dialect = mysql_dialect()

    for table_name in EXPECTED_TABLES:
        statement = CreateTable(metadata.tables[table_name])
        compiled = str(statement.compile(dialect=dialect))

        assert "CREATE TABLE" in compiled
        assert "RESTRICT" in compiled

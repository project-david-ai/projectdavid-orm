from sqlalchemy import BigInteger, String

from projectdavid_orm import AccountErasure, Base


def test_account_erasure_uses_authoritative_metadata():
    table = AccountErasure.__table__

    assert table.metadata is Base.metadata
    assert Base.metadata.tables["account_erasures"] is table


def test_account_erasure_schema():
    columns = AccountErasure.__table__.columns

    assert set(columns.keys()) == {
        "subject_hash",
        "state",
        "created_at",
        "completed_at",
    }

    assert isinstance(columns.subject_hash.type, String)
    assert columns.subject_hash.type.length == 64
    assert columns.subject_hash.primary_key
    assert not columns.subject_hash.nullable

    assert isinstance(columns.state.type, String)
    assert columns.state.type.length == 24
    assert not columns.state.nullable

    assert isinstance(columns.created_at.type, BigInteger)
    assert not columns.created_at.nullable

    assert isinstance(columns.completed_at.type, BigInteger)
    assert columns.completed_at.nullable


def test_erasure_receipt_is_independent_of_user_lifecycle():
    table = AccountErasure.__table__

    assert not table.foreign_keys
    assert not table.foreign_key_constraints

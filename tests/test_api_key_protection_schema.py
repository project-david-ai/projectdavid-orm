"""Regression tests for protected, user-scoped API keys."""

from projectdavid_orm import ApiKey


def test_api_key_protection_is_opt_in():
    column = ApiKey.__table__.c.is_protected

    assert column.nullable is False
    assert column.type.python_type is bool

    assert column.default is not None
    assert column.default.arg is False

    assert column.server_default is not None
    assert str(column.server_default.arg) == "0"


def test_protected_key_preserves_user_ownership():
    table = ApiKey.__table__
    user_id = table.c.user_id

    assert user_id.nullable is False
    assert any(fk.target_fullname == "users.id" for fk in user_id.foreign_keys)

    assert "is_protected" in table.c
    assert "is_active" in table.c

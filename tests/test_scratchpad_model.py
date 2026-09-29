from sqlalchemy import inspect
from sqlalchemy.orm import configure_mappers

from projectdavid_orm.projectdavid_orm.models import Scratchpad, Thread, User


def test_scratchpad_resource_contract():
    configure_mappers()

    table = Scratchpad.__table__

    assert table.name == "scratchpads"

    assert {
        "id",
        "owner_id",
        "thread_id",
        "created_at",
        "updated_at",
        "meta_data",
    }.issubset(table.columns.keys())

    assert table.c.id.primary_key is True
    assert table.c.owner_id.nullable is False
    assert table.c.thread_id.nullable is False
    assert table.c.created_at.nullable is False
    assert table.c.updated_at.nullable is False
    assert table.c.meta_data.nullable is False

    owner_fk = next(iter(table.c.owner_id.foreign_keys))
    thread_fk = next(iter(table.c.thread_id.foreign_keys))

    assert owner_fk.target_fullname == "users.id"
    assert owner_fk.ondelete == "CASCADE"

    assert thread_fk.target_fullname == "threads.id"
    assert thread_fk.ondelete == "CASCADE"

    unique_sets = {
        tuple(constraint.columns.keys())
        for constraint in table.constraints
        if constraint.__class__.__name__ == "UniqueConstraint"
    }

    assert ("thread_id",) in unique_sets


def test_scratchpad_relationship_contract():
    configure_mappers()

    user_relationships = inspect(User).relationships
    thread_relationships = inspect(Thread).relationships
    scratchpad_relationships = inspect(Scratchpad).relationships

    assert "scratchpads" in user_relationships
    assert "scratchpad" in thread_relationships
    assert "owner" in scratchpad_relationships
    assert "thread" in scratchpad_relationships

    assert thread_relationships["scratchpad"].uselist is False

    assert thread_relationships["scratchpad"].back_populates == "thread"
    assert scratchpad_relationships["thread"].back_populates == "scratchpad"

    assert user_relationships["scratchpads"].back_populates == "owner"
    assert scratchpad_relationships["owner"].back_populates == "scratchpads"

from projectdavid_orm import OrmInterface, Scratchpad


def test_scratchpad_is_exposed_through_public_orm_api():
    assert Scratchpad.__tablename__ == "scratchpads"
    assert OrmInterface.Scratchpad is Scratchpad

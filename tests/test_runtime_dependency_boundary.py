from pathlib import Path

from projectdavid_orm.enums import StatusEnum
from projectdavid_orm.projectdavid_orm.models import ApiKey

EXPECTED_STATUS_VALUES = {
    "deleted": "deleted",
    "active": "active",
    "queued": "queued",
    "in_progress": "in_progress",
    "pending_action": "action_required",
    "completed": "completed",
    "failed": "failed",
    "cancelling": "cancelling",
    "cancelled": "cancelled",
    "pending": "pending",
    "processing": "processing",
    "expired": "expired",
    "retrying": "retrying",
    "offline": "offline",
}


def test_status_enum_persistence_contract_is_preserved():
    assert {item.name: item.value for item in StatusEnum} == EXPECTED_STATUS_VALUES


def test_models_have_no_runtime_dependency_on_common():
    models_path = (
        Path(__file__).parents[1]
        / "src"
        / "projectdavid_orm"
        / "projectdavid_orm"
        / "models.py"
    )

    source = models_path.read_text(encoding="utf-8")

    assert "projectdavid_common" not in source
    assert "ValidationInterface" not in source
    assert "LoggingUtility" not in source


def test_bcrypt_backend_hashes_and_verifies_api_keys():
    plain = "project-david-runtime-dependency-probe"

    hashed = ApiKey.hash_key(plain)

    assert hashed != plain

    api_key = ApiKey(
        key_name="dependency-probe",
        hashed_key=hashed,
    )

    assert api_key.verify_key(plain)
    assert not api_key.verify_key(plain + "-invalid")

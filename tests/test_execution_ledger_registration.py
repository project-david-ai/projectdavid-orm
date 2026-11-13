"""Verify normal ORM imports register the execution ledger.

The test runs in a fresh Python interpreter so that earlier test imports
cannot accidentally register the tables and mask a packaging defect.
"""

import subprocess
import sys


def test_fresh_models_import_registers_execution_ledger():
    code = """
from projectdavid_orm.projectdavid_orm import models

expected = {
    "run_execution_epochs",
    "execution_actors",
    "run_delegations",
    "execution_events",
    "evidence_retention_holds",
}

registered = set(models.User.metadata.tables)
missing = expected - registered

assert not missing, (
    f"Unregistered execution ledger tables: {sorted(missing)}"
)
"""

    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, (
        "Fresh ORM import failed.\n"
        f"STDOUT:\n{result.stdout}\n"
        f"STDERR:\n{result.stderr}"
    )

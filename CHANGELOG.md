# [1.9.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.8.0...v1.9.0) (2026-04-19)


### Features

* **schema:** add cancelled_at column to TrainingJob ([134d8cf](https://github.com/project-david-ai/projectdavid-orm/commit/134d8cf63d1ec889841a7bdae5f39efbf5b9ee43))

# [1.8.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.7.0...v1.8.0) (2026-04-12)


### Features

* **inference_deployment:** add mm_processor_kwargs column ([ae55b96](https://github.com/project-david-ai/projectdavid-orm/commit/ae55b96acf0696b27b27afa24d9ab515bb35481c))

# [1.7.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.6.3...v1.7.0) (2026-04-12)


### Features

* **inference_deployment:** add vLLM hyperparam columns ([6c6de67](https://github.com/project-david-ai/projectdavid-orm/commit/6c6de67eca69c7e71c9c3755765254fe1aeac25d))

## [1.6.3](https://github.com/project-david-ai/projectdavid-orm/compare/v1.6.2...v1.6.3) (2026-04-11)


### Bug Fixes

* **orm:** declare Base locally in models.py — remove dependency on projectdavid_common.projectdavid_orm.base ([0d43ad1](https://github.com/project-david-ai/projectdavid-orm/commit/0d43ad1984a72765d651b4080325cecbe35ca3ef))

## [1.6.2](https://github.com/project-david-ai/projectdavid-orm/compare/v1.6.1...v1.6.2) (2026-04-05)


### Bug Fixes

* **exports:** trigger release with correct ORM __init__ exports ([bb7092b](https://github.com/project-david-ai/projectdavid-orm/commit/bb7092bd88104b5ab4a1f59b988d876d3b4170e6))

## [1.6.1](https://github.com/project-david-ai/projectdavid-orm/compare/v1.6.0...v1.6.1) (2026-04-04)


### Bug Fixes

* **exports:** expose all ORM models via __all__ and top-level imports ([33ea05b](https://github.com/project-david-ai/projectdavid-orm/commit/33ea05b04e155039de958a43e21bc06c7fccf761))

# [1.6.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.5.0...v1.6.0) (2026-03-29)


### Features

* publish v1.6.0 — skip duplicate v1.5.0 on PyPI ([636aaf6](https://github.com/project-david-ai/projectdavid-orm/commit/636aaf67a7cedfdd094d47229984074b1305b491))

# [1.5.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.4.0...v1.5.0) (2026-03-29)


### Bug Fixes

* correct semantic-release script path to update_version.py ([59af721](https://github.com/project-david-ai/projectdavid-orm/commit/59af721199849f06c89804df3b28d287e2aa47f6))


### Features

* add max_tokens to Assistant, fix temperature and top_p Integer to Float on Assistant and Run ([b990759](https://github.com/project-david-ai/projectdavid-orm/commit/b9907590bdf46c1d20f908faac7dcfe3ed70d404))
* add nullable endpoint field to BaseModel ([a902d5b](https://github.com/project-david-ai/projectdavid-orm/commit/a902d5ba45852cfbb8f6cd31ebcfed3850fc2354))
* add nullable endpoint field to BaseModel ([6f4aa94](https://github.com/project-david-ai/projectdavid-orm/commit/6f4aa949a7167cdce9311c8d9b03ecd16d373830))
* bump to v1.6.0 — clear duplicate PyPI artefact ([0e616e3](https://github.com/project-david-ai/projectdavid-orm/commit/0e616e36e2a1007e4276223f25443f00c01e727d))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([edf837a](https://github.com/project-david-ai/projectdavid-orm/commit/edf837a7810ee744df011d81f56e5f761ba4135a))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([f4165da](https://github.com/project-david-ai/projectdavid-orm/commit/f4165da7a1784b2e9e89b01384a2a9fb2d898b61))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([ff4a08b](https://github.com/project-david-ai/projectdavid-orm/commit/ff4a08b6b92cb4355568cc299c2e6b51f248cd34))
* Phase 4 ([fb58012](https://github.com/project-david-ai/projectdavid-orm/commit/fb580125b975369c3a3a089f177c31e74561c72e))
* Phase 4 ([6c0c17c](https://github.com/project-david-ai/projectdavid-orm/commit/6c0c17cae3f4560b6dbed4621a4e6844a982d525))
* Phase 5a ([0ea00c5](https://github.com/project-david-ai/projectdavid-orm/commit/0ea00c5ccde65c4e9d191ed1239e0fe1d069c4d0))
* Phase 5a ([32cd97b](https://github.com/project-david-ai/projectdavid-orm/commit/32cd97b97e6fdff515318a61d902d3eb755447d8))
* trigger fresh publish after tag cleanup ([3ad924b](https://github.com/project-david-ai/projectdavid-orm/commit/3ad924be92635c8e4b2f870a021f47496cab32cb))
* trigger release — max_tokens, Float fix, remove BatfishSnapshot, Gold Standard CI ([1569cff](https://github.com/project-david-ai/projectdavid-orm/commit/1569cffcf18bb4fc44f897707ee2aa6e362edc72))

# [1.5.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.4.0...v1.5.0) (2026-03-29)


### Bug Fixes

* correct semantic-release script path to update_version.py ([59af721](https://github.com/project-david-ai/projectdavid-orm/commit/59af721199849f06c89804df3b28d287e2aa47f6))


### Features

* add max_tokens to Assistant, fix temperature and top_p Integer to Float on Assistant and Run ([b990759](https://github.com/project-david-ai/projectdavid-orm/commit/b9907590bdf46c1d20f908faac7dcfe3ed70d404))
* add nullable endpoint field to BaseModel ([a902d5b](https://github.com/project-david-ai/projectdavid-orm/commit/a902d5ba45852cfbb8f6cd31ebcfed3850fc2354))
* add nullable endpoint field to BaseModel ([6f4aa94](https://github.com/project-david-ai/projectdavid-orm/commit/6f4aa949a7167cdce9311c8d9b03ecd16d373830))
* bump to v1.6.0 — clear duplicate PyPI artefact ([0e616e3](https://github.com/project-david-ai/projectdavid-orm/commit/0e616e36e2a1007e4276223f25443f00c01e727d))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([edf837a](https://github.com/project-david-ai/projectdavid-orm/commit/edf837a7810ee744df011d81f56e5f761ba4135a))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([f4165da](https://github.com/project-david-ai/projectdavid-orm/commit/f4165da7a1784b2e9e89b01384a2a9fb2d898b61))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([ff4a08b](https://github.com/project-david-ai/projectdavid-orm/commit/ff4a08b6b92cb4355568cc299c2e6b51f248cd34))
* Phase 4 ([fb58012](https://github.com/project-david-ai/projectdavid-orm/commit/fb580125b975369c3a3a089f177c31e74561c72e))
* Phase 4 ([6c0c17c](https://github.com/project-david-ai/projectdavid-orm/commit/6c0c17cae3f4560b6dbed4621a4e6844a982d525))
* Phase 5a ([0ea00c5](https://github.com/project-david-ai/projectdavid-orm/commit/0ea00c5ccde65c4e9d191ed1239e0fe1d069c4d0))
* Phase 5a ([32cd97b](https://github.com/project-david-ai/projectdavid-orm/commit/32cd97b97e6fdff515318a61d902d3eb755447d8))
* trigger release — max_tokens, Float fix, remove BatfishSnapshot, Gold Standard CI ([1569cff](https://github.com/project-david-ai/projectdavid-orm/commit/1569cffcf18bb4fc44f897707ee2aa6e362edc72))

# [1.5.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.4.0...v1.5.0) (2026-03-29)


### Bug Fixes

* correct semantic-release script path to update_version.py ([59af721](https://github.com/project-david-ai/projectdavid-orm/commit/59af721199849f06c89804df3b28d287e2aa47f6))


### Features

* add max_tokens to Assistant, fix temperature and top_p Integer to Float on Assistant and Run ([b990759](https://github.com/project-david-ai/projectdavid-orm/commit/b9907590bdf46c1d20f908faac7dcfe3ed70d404))
* add nullable endpoint field to BaseModel ([a902d5b](https://github.com/project-david-ai/projectdavid-orm/commit/a902d5ba45852cfbb8f6cd31ebcfed3850fc2354))
* add nullable endpoint field to BaseModel ([6f4aa94](https://github.com/project-david-ai/projectdavid-orm/commit/6f4aa949a7167cdce9311c8d9b03ecd16d373830))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([edf837a](https://github.com/project-david-ai/projectdavid-orm/commit/edf837a7810ee744df011d81f56e5f761ba4135a))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([f4165da](https://github.com/project-david-ai/projectdavid-orm/commit/f4165da7a1784b2e9e89b01384a2a9fb2d898b61))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([ff4a08b](https://github.com/project-david-ai/projectdavid-orm/commit/ff4a08b6b92cb4355568cc299c2e6b51f248cd34))
* Phase 4 ([fb58012](https://github.com/project-david-ai/projectdavid-orm/commit/fb580125b975369c3a3a089f177c31e74561c72e))
* Phase 4 ([6c0c17c](https://github.com/project-david-ai/projectdavid-orm/commit/6c0c17cae3f4560b6dbed4621a4e6844a982d525))
* Phase 5a ([0ea00c5](https://github.com/project-david-ai/projectdavid-orm/commit/0ea00c5ccde65c4e9d191ed1239e0fe1d069c4d0))
* Phase 5a ([32cd97b](https://github.com/project-david-ai/projectdavid-orm/commit/32cd97b97e6fdff515318a61d902d3eb755447d8))
* trigger release — max_tokens, Float fix, remove BatfishSnapshot, Gold Standard CI ([1569cff](https://github.com/project-david-ai/projectdavid-orm/commit/1569cffcf18bb4fc44f897707ee2aa6e362edc72))

# [1.5.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.4.0...v1.5.0) (2026-03-28)


### Bug Fixes

* correct semantic-release script path to update_version.py ([59af721](https://github.com/project-david-ai/projectdavid-orm/commit/59af721199849f06c89804df3b28d287e2aa47f6))


### Features

* add max_tokens to Assistant, fix temperature and top_p Integer to Float on Assistant and Run ([b990759](https://github.com/project-david-ai/projectdavid-orm/commit/b9907590bdf46c1d20f908faac7dcfe3ed70d404))
* add nullable endpoint field to BaseModel ([a902d5b](https://github.com/project-david-ai/projectdavid-orm/commit/a902d5ba45852cfbb8f6cd31ebcfed3850fc2354))
* add nullable endpoint field to BaseModel ([6f4aa94](https://github.com/project-david-ai/projectdavid-orm/commit/6f4aa949a7167cdce9311c8d9b03ecd16d373830))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([edf837a](https://github.com/project-david-ai/projectdavid-orm/commit/edf837a7810ee744df011d81f56e5f761ba4135a))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([f4165da](https://github.com/project-david-ai/projectdavid-orm/commit/f4165da7a1784b2e9e89b01384a2a9fb2d898b61))
* max_tokens on Assistant, temperature/top_p Integer to Float, remove BatfishSnapshot, Gold Standard CI, PolyForm licence, COMMERCIAL.md, SECURITY.md, pre-commit, mypy ([ff4a08b](https://github.com/project-david-ai/projectdavid-orm/commit/ff4a08b6b92cb4355568cc299c2e6b51f248cd34))
* Phase 4 ([fb58012](https://github.com/project-david-ai/projectdavid-orm/commit/fb580125b975369c3a3a089f177c31e74561c72e))
* Phase 4 ([6c0c17c](https://github.com/project-david-ai/projectdavid-orm/commit/6c0c17cae3f4560b6dbed4621a4e6844a982d525))
* Phase 5a ([0ea00c5](https://github.com/project-david-ai/projectdavid-orm/commit/0ea00c5ccde65c4e9d191ed1239e0fe1d069c4d0))
* Phase 5a ([32cd97b](https://github.com/project-david-ai/projectdavid-orm/commit/32cd97b97e6fdff515318a61d902d3eb755447d8))

# [1.4.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.3.0...v1.4.0) (2026-03-23)


### Features

* Phase 5a ([7213c69](https://github.com/project-david-ai/projectdavid-orm/commit/7213c698beb56eddb5230bbcf609f250e6b20c5e))

# [1.3.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.2.0...v1.3.0) (2026-03-23)


### Features

* Phase 4 ([235a547](https://github.com/project-david-ai/projectdavid-orm/commit/235a54724dee1555c6e23febc9dec5d85dda5328))

# [1.2.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.12...v1.2.0) (2026-03-22)


### Features

* add internal_hostname to  InferenceDeployment ([20aa5d2](https://github.com/project-david-ai/projectdavid-orm/commit/20aa5d23fae57e510b63bcb59b24ff0c1544be9b))

## [1.1.12](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.11...v1.1.12) (2026-03-21)


### Bug Fixes

* clean up column formatting and relationships in models for improved readability and consistency ([fb5a873](https://github.com/project-david-ai/projectdavid-orm/commit/fb5a8736c6d3fa726c806e6bba7de06f00f234e4))
* clean up column formatting and relationships in models for improved readability and consistency ([fb5e05f](https://github.com/project-david-ai/projectdavid-orm/commit/fb5e05f5b0c94d05f1ce4b32ce46b61f8f33f96d))
* clean up column formatting and relationships in models for improved readability and consistency ([bca098e](https://github.com/project-david-ai/projectdavid-orm/commit/bca098e76a04011bff6a3d719100d76dbbc650b9))
* standardize timestamp columns, add soft-delete logic, and improve comments in models ([480baa1](https://github.com/project-david-ai/projectdavid-orm/commit/480baa17f1f34b575d3e6ba921ba6df9be3ac13b))
* standardize timestamp columns, add soft-delete logic, and improve comments in models ([568c93d](https://github.com/project-david-ai/projectdavid-orm/commit/568c93dc8523c159ebc0c67f5a6b909cc2fe6352))

## [1.1.11](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.10...v1.1.11) (2026-03-20)


### Bug Fixes

* add updated_at column to TrainingJobs table. ([18f38b7](https://github.com/project-david-ai/projectdavid-orm/commit/18f38b77802200038a3bd30bea01492f431d79f0))
* remove projectdavid_common dependency from pyproject.toml ([8550789](https://github.com/project-david-ai/projectdavid-orm/commit/85507896809a78ff44b0ca07258c3a727d7a2819))
* standardize timestamp columns, add soft-delete logic, and improve comments in models ([b9859c7](https://github.com/project-david-ai/projectdavid-orm/commit/b9859c74802dde63945d22485db9b426f447c971))
* update model imports and clean up column definitions in models ([5cc9fff](https://github.com/project-david-ai/projectdavid-orm/commit/5cc9fff84411a36e486742a6736934d41191ade6))

## [1.1.10](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.9...v1.1.10) (2026-03-20)


### Bug Fixes

* standardize timestamp columns, add soft-delete logic, and improve comments in models ([0aa5983](https://github.com/project-david-ai/projectdavid-orm/commit/0aa59836c1f37c5ee70a90cea269bfa2a2a8fb1f))
* standardize timestamp columns, add soft-delete logic, and improve comments in models ([d28dbc2](https://github.com/project-david-ai/projectdavid-orm/commit/d28dbc28a8413a67790f46627b0f35b2e828427c))

## [1.1.9](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.8...v1.1.9) (2026-03-19)


### Bug Fixes

* add updated_at column to TrainingJobs table. ([bf438d8](https://github.com/project-david-ai/projectdavid-orm/commit/bf438d8856af88a03d41dab3b7cf4d5bd56ce339))
* remove projectdavid_common dependency from pyproject.toml ([6537c42](https://github.com/project-david-ai/projectdavid-orm/commit/6537c42a1a7437c19a601fd154e655739c8f005b))

## [1.1.8](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.7...v1.1.8) (2026-03-19)


### Bug Fixes

* remove projectdavid_common dependency from pyproject.toml ([8f6faa1](https://github.com/project-david-ai/projectdavid-orm/commit/8f6faa1d494a864998e31aa073308c13c65889cf))

## [1.1.7](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.6...v1.1.7) (2026-03-19)


### Bug Fixes

* remove projectdavid_common dependency from pyproject.toml ([15fe2f7](https://github.com/project-david-ai/projectdavid-orm/commit/15fe2f79d6d2ac6ed5fdc59f71a8df891727aeb0))

## [1.1.6](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.5...v1.1.6) (2026-03-19)


### Bug Fixes

* remove redundant newline in README.md instructions ([81a423f](https://github.com/project-david-ai/projectdavid-orm/commit/81a423fb14dc4d46640b3a8d6b5748ddb794f720))
* upgrade projectdavid_common to v0.53.0 and remove redundant comments in models.py ([ac95695](https://github.com/project-david-ai/projectdavid-orm/commit/ac9569594868bbcbcefe5987195518482fad962b))

## [1.1.5](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.4...v1.1.5) (2026-03-18)


### Bug Fixes

* streamline test_tag_release workflow by removing `dev` branch logic and updating PyPI token configuration ([89a1be2](https://github.com/project-david-ai/projectdavid-orm/commit/89a1be2b410a1ce275f36e224fa407a4be4a1a26))

## [1.1.4](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.3...v1.1.4) (2026-03-18)


### Bug Fixes

* remove unused id-token permission from test_tag_release workflow ([c7225e7](https://github.com/project-david-ai/projectdavid-orm/commit/c7225e7432a26bf1fe32d429347ab79c286bced1))

## [1.1.3](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.2...v1.1.3) (2026-03-18)


### Bug Fixes

* remove unused id-token permission from test_tag_release workflow ([cd79ff9](https://github.com/project-david-ai/projectdavid-orm/commit/cd79ff9465b532031c64a7add2a9785a8bfef567))

## [1.1.2](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.1...v1.1.2) (2026-03-18)


### Bug Fixes

* remove unused id-token permission from test_tag_release workflow ([a34000d](https://github.com/project-david-ai/projectdavid-orm/commit/a34000da052f404db798da691ab2c5fa5815eeeb))

## [1.1.1](https://github.com/project-david-ai/projectdavid-orm/compare/v1.1.0...v1.1.1) (2026-03-18)


### Bug Fixes

* update PyPI repository URLs and add attestations flag in test_tag_release workflow ([a2dca7e](https://github.com/project-david-ai/projectdavid-orm/commit/a2dca7e521732302f8d0acb86390f3f061aae07e))

# [1.1.0](https://github.com/project-david-ai/projectdavid-orm/compare/v1.0.0...v1.1.0) (2026-03-18)


### Bug Fixes

* remove redundant newline in README.md instructions ([dea758d](https://github.com/project-david-ai/projectdavid-orm/commit/dea758d4d80eb0e6f2b75e80e712652779afbe63))


### Features

* add version.py for managing application versioning ([6ec6e42](https://github.com/project-david-ai/projectdavid-orm/commit/6ec6e425eba9e790e2a4a4c24aea5fa60c1f1057))

# 1.0.0 (2026-03-18)


### Bug Fixes

* codebase for improved readability by consistently formatting SQLAlchemy column definitions and relationships. Adjust test log messages for clarity. ([e302b55](https://github.com/project-david-ai/projectdavid-orm/commit/e302b5580d35537db028a4cbea23d2d7f833cffc))


### Features

* Set up release automation and project metadata files, including .releaserc.json, scripts, and editor configurations. ([4a747bb](https://github.com/project-david-ai/projectdavid-orm/commit/4a747bbf133f19c31629587955dd009545e241b5))

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

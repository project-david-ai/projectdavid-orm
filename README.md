# projectdavid-orm

Shared SQLAlchemy ORM models and database utilities for the ProjectDavid platform.

Provides a single source of truth for all database models used across ProjectDavid microservices, eliminating duplication between the core API, training service, and any future services that require direct database access.

---

## Overview

ProjectDavid is a self-hosted, multi-provider LLM runtime API. As the platform grows into multiple microservices (inference API, training API, sandbox, etc.), each service needs access to the same database schema. Rather than duplicating model definitions or making inter-service HTTP calls just to read data, `projectdavid-orm` exposes the full SQLAlchemy model layer as a shared, versioned package.

Any service that needs direct DB access simply installs this package and imports the models it needs.

---
## Installation
```bash
pip install projectdavid-orm

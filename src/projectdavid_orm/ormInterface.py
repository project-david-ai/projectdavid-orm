# src/projectdavid_orm/ormInterface.py
from projectdavid_orm.projectdavid_orm.models import *


class OrmInterface:
    """
    Exposes Pydantic validation classes, retaining their original naming.

    This interface allows consumers to access the various schemas like:
        - ValidationInterface.FileUploadRequest
        - ValidationInterface.ActionCreate
        - etc.
    """

    # Api Key model
    ApiKey = ApiKey
    # User model
    User = User
    # GDPR Audit log
    AuditLog = AuditLog
    # Thread model
    Thread = Thread
    # Message model
    Message = Message
    # Run model
    Run = Run
    # Assistant model
    Assistant = Assistant
    # Action model
    Action = Action
    # Sandbox model
    Sandbox = Sandbox
    # File model
    File = File
    # FileStorage model
    FileStorage = FileStorage
    # Batfish model
    BatfishSnapshot = BatfishSnapshot
    # VectorStore model
    VectorStore = VectorStore
    # VectorStoreFile model
    VectorStoreFile = VectorStoreFile

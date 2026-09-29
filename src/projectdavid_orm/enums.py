from enum import Enum


class StatusEnum(str, Enum):
    """Canonical persistence status values used by ORM models."""

    deleted = "deleted"
    active = "active"
    queued = "queued"
    in_progress = "in_progress"
    pending_action = "action_required"
    completed = "completed"
    failed = "failed"
    cancelling = "cancelling"
    cancelled = "cancelled"
    pending = "pending"
    processing = "processing"
    expired = "expired"
    retrying = "retrying"
    offline = "offline"

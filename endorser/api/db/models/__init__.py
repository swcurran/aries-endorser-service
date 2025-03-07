# Import all the models, so that Base has them before being imported by Alembic

from api.db.models.base import BaseTable  # noqa: F401
from api.db.models.configuration import ConfigurationDB  # noqa: F401
from api.db.models.contact import Contact  # noqa: F401
from api.db.models.endorse_request import EndorseRequest  # noqa: F401

__all__ = [
    "BaseTable",
    "ConfigurationDB",
    "Contact",
    "EndorseRequest",
]

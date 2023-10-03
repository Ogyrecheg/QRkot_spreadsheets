from sqlalchemy import Column, String, Text

from app.core.db import CustomBaseModel
from app.services.constants import CHARITYPROJECT_NAME_LENGTH


class CharityProject(CustomBaseModel):
    name = Column(
        String(CHARITYPROJECT_NAME_LENGTH),
        unique=True,
        nullable=False,
    )
    description = Column(Text, nullable=False)

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator

from app.services.constants import (CHARITYPROJECT_DESCRIPTION_MIN_LENGTH,
                                    CHARITYPROJECT_NAME_LENGTH,
                                    CHARITYPROJECT_NAME_MIN_LENGTH,
                                    MIN_FULL_AMOUNT)


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=CHARITYPROJECT_NAME_MIN_LENGTH,
        max_length=CHARITYPROJECT_NAME_LENGTH,
    )
    description: Optional[str] = Field(
        None,
        min_length=CHARITYPROJECT_DESCRIPTION_MIN_LENGTH,
    )
    full_amount: Optional[int] = Field(None, gt=MIN_FULL_AMOUNT)

    class Config:
        extra = Extra.forbid


class CharityProjectUpdate(CharityProjectBase):
    pass

    @validator('name')
    def name_cant_be_none(cls, value):
        if value is None:
            raise ValueError('Имя не может быть None')
        return value


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(
        min_length=CHARITYPROJECT_NAME_MIN_LENGTH,
        max_length=CHARITYPROJECT_NAME_LENGTH,
    )
    description: str = Field(min_length=CHARITYPROJECT_DESCRIPTION_MIN_LENGTH)
    full_amount: int = Field(gt=MIN_FULL_AMOUNT)

    @validator('name', 'description')
    def none_and_empty_not_allowed(cls, value: str):
        if not value or value is None:
            raise ValueError(
                'Все поля обязательны. "" или None не допускаются.'
            )
        return value


class CharityProjectBD(CharityProjectBase):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True

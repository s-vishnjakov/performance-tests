from typing import Annotated
from pydantic import BaseModel, Field, EmailStr, ConfigDict, StringConstraints
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """Schema for user"""
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')
    phone_number: str = Field(alias='phoneNumber')


class CreateUserRequestSchema(BaseModel):
    """Request schema for creating a new user"""
    model_config = ConfigDict(alias_generator=to_camel, validate_by_alias=True)

    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """Response schema for creating a new user"""
    user: UserSchema

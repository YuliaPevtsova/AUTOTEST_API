from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel

from tools.fakers import get_random_email


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str
    email: EmailStr = Field(default_factory=get_random_email)
    last_name: str = Field(alias="lastName")
    first_name: str= Field(alias="firstName")
    middle_name: str= Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr = Field(default_factory=get_random_email)
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
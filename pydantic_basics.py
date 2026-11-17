import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel

from tools.fakers import get_random_email

"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
   
    "estimatedTime": "string",
    
  }
{
    "course": {
        "id": "string",
        "title": "string",
        "maxScore": 0,
        "minScore": 0,
        "description": "string",
        "previewFile": {
          "id": "string",
          "filename": "string",
          "directory": "string",
          "url": "https://example.com/"
        },
        "estimatedTime": "string",
        "createdByUser": {
          "id": "string",
          "email": "user@example.com",
          "lastName": "string",
          "firstName": "string",
          "middleName": "string"
        }
      }
}
  
"""
class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl = Field(default="https://example.com/")

class UserSchema(BaseModel):
    id: str
    email: EmailStr = Field(default_factory=get_random_email)
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self)->str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self)-> str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory= lambda: str(uuid.uuid4()) )
    title: str = "course_title"
    # maxScore: int
    # minScore: int
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=10)
    # max_score: int
    # min_score: int
    description: str = "new description"
    preview_file: FileSchema = Field(alias="previewFile")
    # estimated_time: str = Field(alias="estimatedTime")
    # estimatedTime: str
    estimated_time: str = Field(alias="estimatedTime", default="1 week")
    created_by_user: UserSchema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id="course_id",
    title="course_title",
    maxScore=100,
    minScore=1,
    description="course_description",
    previewFile=FileSchema(
        id="file_id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses"
    ),
    estimatedTime="3 weeks",
    createdByUser=UserSchema(
        id = "user-id",
        email = "user@gmail.com",
        lastName = "Bond",
        firstName = "Zara",
        middleName = "Alice"
    )
)

print(course_default_model)

course_dict= {
    "id": "string",
    "title": "string",
    "maxScore": 20,
    "minScore": 2,
    "description": "string",
    "previewFile":{
        "id":"file_id",
        "url":"http://localhost:8000",
        "filename":"file.png",
        "directory":"courses"
    },
    "estimatedTime": "string",
    "createdByUser":{
        "id":"user-id",
        "email":"user@gmail.com",
        "lastName":"Bond",
        "firstName":"Zara",
        "middleName":"Alice"
    }
  }
course_dict_model = CourseSchema(**course_dict)
# print(course_dict_model)

course_json = """
 {
    "id": "string",
    "title": "string",
    "maxScore": 20,
    "minScore": 2,
    "description": "string",
    "previewFile":{
        "id":"file_id",
        "url":"http://localhost:8000",
        "filename":"file.png",
        "directory":"courses"
    },
    "estimatedTime": "string",
    "createdByUser":{
        "id":"user-id",
        "email":"user@gmail.com",
        "lastName":"Bond",
        "firstName":"Zara",
        "middleName":"Alice"
    }
  }
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print(course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))
#
# course1 = CourseSchema()
# course2 = CourseSchema()
# print(course1.id)
# print(course2.id)

user = UserSchema(
    id = "user-id",
    email = "user@gmail.com",
    lastName = "Bond",
    firstName = "Zara",
    middleName = "Alice"
)
print(user.get_username())

try:
    file = FileSchema(
        id="file_id",
        url="localhost",
        filename="file.png",
        directory="courses"
    )
except ValidationError as error:
    print(error)
    print(error.errors())
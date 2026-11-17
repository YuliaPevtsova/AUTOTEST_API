from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_user_client = get_public_users_client()
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string1",
    lastName="string1",
    firstName="string1",
    middleName="string1"
)
create_user_response = public_user_client.create_user(create_user_request)

authentication_user = AuthenticationUserDict(
    email=create_user_request["email"],
    password=create_user_request["password"]
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/cat6.png"
)
create_file_response = files_client.create_file(create_file_request)

create_course_request = CreateCourseRequestDict(
    title="NewCourseTest",
    maxScore=100,
    minScore=5,
    description="NewCorseForExercise",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)

create_exersice_request = CreateExerciseRequestDict(
    title="Exersice 1",
    courseId=create_course_response['course']['id'],
    maxScore= 200,
    minScore= 20,
    orderIndex= 2,
    description= "NewExerciseForCourse",
    estimatedTime= "3 weeks"
)
create_exercise_response = exercises_client.create_exercises(create_exersice_request)

print(create_exercise_response)
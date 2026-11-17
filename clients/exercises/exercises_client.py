from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class Exercise(TypedDict):
    """
    Описывает структуру упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения упражнения
    """
    exercise: Exercise

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка упражнений
    """
    exercises: list[Exercise]



class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, request: CreateExerciseRequestDict)->Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore,  minScore,
        orderIndex, description, estimatedTimed.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises",json=request)

    def update_course_api(self,  exercise_id: str, request: UpdateExerciseRequestDict)-> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore,  minScore,
        orderIndex, description, estimatedTimed.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercise/{exercise_id}", json=request)

    def delete_course_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str)->CreateExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercises(self, request: CreateExerciseRequestDict)->CreateExerciseResponseDict:
        response = self.create_exercises_api(request)
        return response.json()

    def update_exercise(self,  exercise_id: str, request: UpdateExerciseRequestDict)->CreateExerciseResponseDict:
        response = self.update_course_api(exercise_id, request)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict)->ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))

import httpx_create_file
from tools.fakers import get_random_email

payload = {
  "email": get_random_email(),
  "password": "qwerty",
  "lastName": "Last",
  "firstName": "First",
  "middleName": "string"
}

response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())

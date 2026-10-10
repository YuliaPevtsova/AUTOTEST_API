import httpx

payload = {"email": "user@example.com","password": "string"}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=2,
    headers=headers
)

get_user_me_response = client.get("/api/v1/users/me")
print(get_user_me_response.json())

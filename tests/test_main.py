from fastapi.testclient import TestClient
from app.main import app

# 기존의 FastAPI 앱을 테스트용 클라이언트에 담습니다.
client = TestClient(app)

def test_read_root():
    # "/" 경로로 GET 요청을 보냅니다.
    response = client.get("/")
    # 응답 코드가 200(성공)인지 확인합니다.
    assert response.status_code == 200
    # 응답 데이터가 예상한 문구와 일치하는지 확인합니다.
    assert response.json() == {"message": "서버가 정상적으로 작동 중입니다."}

def test_add_numbers():
    # "/add" 경로에 a=5, b=3 데이터를 담아 요청합니다.
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}
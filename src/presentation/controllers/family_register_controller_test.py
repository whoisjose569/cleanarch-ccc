from src.presentation.controllers.family_register_controller import FamilyRegisterController
from src.data.tests.family_register import FamilyRegisterSpy

class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {"family_name": "teste", "family_address": "teste", "phone": "12345", "email": "teste@email"}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = FamilyRegisterSpy()
    family_register_controller = FamilyRegisterController(use_case)
    
    response = family_register_controller.handle(http_request_mock)
    body_data = http_request_mock.body
    
    assert body_data["family_name"] == "teste"
    assert body_data["family_address"] == "teste"
    assert body_data["phone"] == "12345"
    assert body_data["email"] == "teste@email"
    assert response.status_code == 200
    assert response.body is not None


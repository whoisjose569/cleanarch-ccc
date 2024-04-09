from src.presentation.controllers.monthly_income_register_controller import MonthlyIncomeRegisterController
from src.data.tests.monthly_income_register import MonthlyIncomeRegisterSpy

class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {"family_id": 1, "income": 200, "date": "2000-05-02"}
    
def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = MonthlyIncomeRegisterSpy()
    monthly_income_register_controller = MonthlyIncomeRegisterController(use_case)
        
    response = monthly_income_register_controller.handle(http_request_mock)
    body_data = http_request_mock.body
        
    assert body_data["family_id"] == 1
    assert body_data["income"] == 200
    assert body_data["date"] == "2000-05-02"
    assert response.status_code == 200
    assert response.body is not None
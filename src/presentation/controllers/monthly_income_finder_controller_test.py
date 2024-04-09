from src.presentation.controllers.monthly_income_finder_controller import MonthlyIncomeFinderController
from src.data.tests.monthly_income_finder import MonthlyIncomeFinderSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"family_id": 1}
        

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = MonthlyIncomeFinderSpy()
    
    monthly_income_finder_controller = MonthlyIncomeFinderController(use_case)
    
    response = monthly_income_finder_controller.handle(http_request_mock)
    body_data = http_request_mock.query_params
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
    assert body_data["family_id"] == 1
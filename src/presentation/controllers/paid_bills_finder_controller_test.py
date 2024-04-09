from src.presentation.controllers.paid_bills_finder_controller import PaidBillsFinderController
from src.data.tests.paid_bills_finder import PaidBillsFinderSpy
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.http_types.http_request import HttpRequest

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"family_id": 1, "type": "luz", "value": 200, "payment_date": "2000-05-02"}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = PaidBillsFinderSpy()
    paid_bills_finder_controller = PaidBillsFinderController(use_case)
    http_request = HttpRequest()
    http_request.query_params = http_request_mock.query_params
    
    response = paid_bills_finder_controller.handle(http_request)
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body['data'] is not None


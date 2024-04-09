from src.presentation.controllers.paid_bills_register_controller import PaidBillsRegisterController
from src.data.tests.paid_bills_register import PaidBillsRegisterSpy

class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {"family_id": 1, "type": "luz", "value": 2000, "payment_date": "2000-05-02"}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = PaidBillsRegisterSpy()
    paid_bills_register_controller = PaidBillsRegisterController(use_case)
    
    response = paid_bills_register_controller.handle(http_request_mock)
    body_data = http_request_mock.body
    
    assert body_data["family_id"] == 1
    assert body_data["type"] == "luz"
    assert body_data["value"] == 2000
    assert body_data["payment_date"] == "2000-05-02"
    assert response.status_code == 200
    assert response.body is not None
from src.presentation.controllers.family_finder_controller import FamilyFinderController
from src.data.tests.family_finder import FamilyFinderSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"family_name": "teste"}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = FamilyFinderSpy()
    family_finder_controller = FamilyFinderController(use_case)
    
    response = family_finder_controller.handle(http_request_mock)
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body['data'] is not None
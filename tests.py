import pytest
from fastapi.testclient import TestClient

import schemas


@pytest.fixture
def api_client() -> TestClient:
    from main import app
    return TestClient(app)


def test_reverse_string_success(api_client: TestClient):
    # given
    input_string = "abcdefg"
    expected_string = "gfedcba"

    # when
    response = api_client.get(f"/string/{input_string}")

    # then
    assert response.status_code == 200, "Response status should indicate success"
    assert response.json() == schemas.ReverseStringResponse(
        reversed_string=expected_string), "Response should contain reversed string"

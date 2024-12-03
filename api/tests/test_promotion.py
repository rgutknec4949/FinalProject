from fastapi.testclient import TestClient
from ..controllers import promotion as controller
from ..main import app
import pytest
from ..models import promotion as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_promotion(db_session):
    # Create a sample order
    promo_data = {
        "code_name": "promo",
        "expiration_date": "date"
    }

    promo_object = model.Promotion(**promo_data)

    # Call the create function
    created_promo = controller.create(db_session, promo_object)

    # Assertions
    assert created_promo is not None
    assert created_promo.code_name == "promo"
    assert created_promo.expiration_date == "date"



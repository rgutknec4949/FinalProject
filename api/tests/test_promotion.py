import pytest
from datetime import date
from api.schemas.promotion import PromotionCreate, PromotionUpdate, Promotion

def test_promotion_create():
    promo = PromotionCreate(code_name="SUMMER21", expiration_date=date(2023, 12, 31))
    assert promo.code_name == "SUMMER21"
    assert promo.expiration_date == date(2023, 12, 31)

def test_promotion_update():
    promo = PromotionUpdate(code_name="WINTER21", expiration_date=date(2024, 1, 31))
    assert promo.code_name == "WINTER21"
    assert promo.expiration_date == date(2024, 1, 31)

def test_promotion():
    promo = Promotion(id=1, code_name="SPRING21", expiration_date=date(2023, 6, 30))
    assert promo.id == 1
    assert promo.code_name == "SPRING21"
    assert promo.expiration_date == date(2023, 6, 30)
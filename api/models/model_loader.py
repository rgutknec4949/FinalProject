from . import orders, order_details, recipes, resources, menu, promotion
from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
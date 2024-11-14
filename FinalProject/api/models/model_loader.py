from . import order, order_details, recipes, sandwiches, resources, customer, menu, promotion, rating, payment

from ..dependencies.database import engine


def index():
    order.Base.metadata.create_all(engine)
    # order_details.Base.metadata.create_all(engine)
    # recipes.Base.metadata.create_all(engine)
    # sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    rating.Base.metadata.create_all(engine)


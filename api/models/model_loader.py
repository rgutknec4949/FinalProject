from . import orders, order_details, resources, menu, payment
from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)

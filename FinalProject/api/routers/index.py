from . import orders, order_details, promotion, recipes


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(promotion.router)
    app.include_router(recipes.router)

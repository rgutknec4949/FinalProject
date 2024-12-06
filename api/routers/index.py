from . import orders, order_details, menu, promotion, recipes, resources


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(menu.router)
    app.include_router(promotion.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)


from . import orders, menu, promotion


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(menu.router)
    app.include_router(promotion.router)

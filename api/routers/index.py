from . import orders, order_details, customer, payment, rating, sandwiches, menu, promotion, recipes, resources


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customer.router)
    app.include_router(payment.router)
    app.include_router(rating.router)
    app.include_router(sandwiches.router)
    app.include_router(menu.router)
    app.include_router(resources.router)
    app.include_router(promotion.router)
    app.include_router(recipes.router)





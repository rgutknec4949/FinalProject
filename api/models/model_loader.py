from . import orders, recipes, resources, menu
from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
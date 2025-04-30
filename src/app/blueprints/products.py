import inject
from flask import Blueprint, current_app, request
from flask_login import login_required
from pydantic import RootModel

from src.domain.models import Product
from src.domain.usecases.product_actions import GetProductsAction

Products = RootModel[list[Product]]

bp = Blueprint("products", __name__)

@bp.route("/products", methods=["GET"])
@login_required
@inject.autoparams()
def get_products(get_product_action: GetProductsAction):
    category = request.args.get("category", None)
    products = get_product_action.execute(category=category)
    return current_app.response_class(
        response=Products([
            product for product in products
        ]).model_dump_json(indent=2),
        status=200,
        mimetype="application/json",
    )

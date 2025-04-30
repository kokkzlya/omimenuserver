import inject

from src.domain.models import Product
from src.infra.repositories.postgres.product_repository import ProductRepository

class GetProductsAction:
    product_repository = inject.attr(ProductRepository)

    def execute(self, category: str | None = None) -> list[Product]:
        return self.product_repository.get_products(category=category)

class AddProductAction:
    product_repository = inject.attr(ProductRepository)

    def execute(self, product: Product) -> None:
        self.product_repository.add_product(product)

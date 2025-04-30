import inject
from sqlalchemy import select
from sqlalchemy.orm import scoped_session

from src.domain import models
from src.infra.repositories.postgres.entities import Product

class ProductRepository:
    session = inject.attr(scoped_session)

    def get_products(self, category: str | None = None) -> list[models.Product]:
        query = select(Product)
        if category:
            query = query.where(Product.category == category)
        products = self.session.execute(query).scalars().all()
        return [
            models.Product.model_validate(product, from_attributes=True)
            for product in products
        ]

    def add_product(self, product: models.Product) -> None:
        new_product = Product(
            name=product.name,
            description=product.description,
            price=product.price,
            category=product.category,
        )
        self.session.add(new_product)
        self.session.commit()
        product.id = new_product.id

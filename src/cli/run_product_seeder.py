import logging

import inject

from src.domain.models import Product
from src.domain.usecases.product_actions import AddProductAction

logger = logging.getLogger(__name__)

@inject.autoparams()
def run(add_product_action: AddProductAction):
    products = [
        {
            "name": "Bubur Ayam",
            "description":
                "Bubur ayam adalah makanan khas Indonesia yang terbuat dari "
                "beras yang dimasak dengan air kaldu ayam.",
            "price": 20000,
            "category": "main_course",
        },
        {
            "name": "Nasi Goreng",
            "description":
                "Nasi goreng adalah makanan khas Indonesia yang terbuat "
                "dari nasi yang digoreng dengan bumbu-bumbu.",
            "price": 15000,
            "category": "main_course",
        },
        {
            "name": "Sate Ayam",
            "description":
                "Sate ayam adalah makanan khas Indonesia yang terbuat dari daging ayam "
                "yang ditusuk dengan tusuk sate dan dibakar.",
            "price": 25000,
            "category": "main_course",
        },
        {
            "name": "Rendang",
            "description":
                "Rendang adalah makanan khas Indonesia yang terbuat dari daging sapi "
                "yang dimasak dengan bumbu rempah-rempah.",
            "price": 30000,
            "category": "main_course",
        },
        {
            "name": "Gado-Gado",
            "description":
                "Gado-gado adalah makanan khas Indonesia yang terbuat dari sayuran "
                "segar yang disiram dengan saus kacang.",
            "price": 20000,
            "category": "main_course",
        },
        {
            "name": "Soto Ayam",
            "description":
                "Soto ayam adalah makanan khas Indonesia yang terbuat dari ayam yang "
                "dimasak dengan bumbu rempah-rempah.",
            "price": 25000,
            "category": "main_course",
        },
        {
            "name": "Bakso",
            "description":
                "Bakso adalah makanan khas Indonesia yang terbuat dari daging sapi "
                "yang digiling halus dan dibentuk bulat.",
            "price": 15000,
            "category": "main_course",
        },
        {
            "name": "Pecel Lele",
            "description":
                "Pecel lele adalah makanan khas Indonesia yang terbuat dari ikan lele "
                "yang digoreng dan disajikan dengan sambal.",
            "price": 20000,
            "category": "main_course",
        },
        {
            "name": "Ayam Penyet",
            "description":
                "Ayam penyet adalah makanan khas Indonesia yang terbuat dari ayam yang "
                "digoreng dan disajikan dengan sambal.",
            "price": 25000,
            "category": "main_course",
        },
        {
            "name": "Nasi Uduk",
            "description":
                "Nasi uduk adalah makanan khas Indonesia yang terbuat dari nasi yang "
                "dimasak dengan santan.",
            "price": 15000,
            "category": "main_course",
        },
        {
            "name": "Es Teh Manis",
            "description":
                "Es teh manis adalah minuman khas Indonesia yang terbuat dari teh yang "
                "disajikan dengan es dan gula.",
            "price": 5000,
            "category": "drink",
        },
        {
            "name": "Es Jeruk",
            "description":
                "Es jeruk adalah minuman khas Indonesia yang terbuat dari jeruk yang "
                "disajikan dengan es.",
            "price": 7000,
            "category": "drink",
        },
        {
            "name": "Kopi Susu",
            "description":
                "Kopi susu adalah minuman khas Indonesia yang terbuat dari kopi yang "
                "dicampur dengan susu.",
            "price": 10000,
            "category": "drink",
        },
        {
            "name": "Teh Tarik",
            "description":
                "Teh tarik adalah minuman khas Indonesia yang terbuat dari teh yang "
                "dicampur dengan susu dan gula.",
            "price": 8000,
            "category": "drink",
        },
        {
            "name": "Salad",
            "description":
                "Salad adalah makanan khas Indonesia yang terbuat dari sayuran segar "
                "yang disajikan dengan saus.",
            "price": 12000,
            "category": "appetizer",
        },
        {
            "name": "Sushi",
            "description":
                "Sushi adalah makanan khas Jepang yang terbuat dari nasi yang "
                "dibungkus dengan rumput laut dan diisi dengan ikan.",
            "price": 30000,
            "category": "appetizer",
        },
        {
            "name": "Spring Roll",
            "description":
                "Spring roll adalah makanan khas Indonesia yang terbuat dari sayuran "
                "yang dibungkus dengan kulit lumpia.",
            "price": 15000,
            "category": "appetizer",
        },
        {
            "name": "Bruschetta",
            "description":
                "Bruschetta adalah makanan khas Italia yang terbuat dari roti yang "
                "dipanggang dan disajikan dengan tomat dan bawang putih.",
            "price": 20000,
            "category": "appetizer",
        },
        {
            "name": "Nachos",
            "description":
                "Nachos adalah makanan khas Meksiko yang terbuat dari tortilla yang "
                "dipanggang dan disajikan dengan keju.",
            "price": 25000,
            "category": "appetizer",
        },
        {
            "name": "Pudding",
            "description":
                "Pudding adalah makanan penutup yang terbuat dari susu dan gula yang "
                "dimasak hingga mengental.",
            "price": 10000,
            "category": "dessert",
        },
        {
            "name": "Kue Cubir",
            "description":
                "Kue cubir adalah makanan penutup yang terbuat dari tepung terigu dan "
                "gula yang dipanggang.",
            "price": 12000,
            "category": "dessert",
        },
        {
            "name": "Es Krim",
            "description":
                "Es krim adalah makanan penutup yang terbuat dari susu dan gula yang "
                "dibekukan.",
            "price": 15000,
            "category": "dessert",
        },
        {
            "name": "Brownies",
            "description":
                "Brownies adalah makanan penutup yang terbuat dari cokelat dan tepung "
                "terigu yang dipanggang.",
            "price": 20000,
            "category": "dessert",
        },
        {
            "name": "Cheesecake",
            "description":
                "Cheesecake adalah makanan penutup yang terbuat dari keju dan gula "
                "yang dipanggang.",
            "price": 25000,
            "category": "dessert",
        },
    ]

    for product in products:
        new_product = Product.model_validate(product)
        add_product_action.execute(new_product)
        logger.info("Product %s added with ID %s", new_product.name, new_product.id)

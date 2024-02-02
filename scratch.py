from pprint import pprint

from checkout.models import Category, Product
from carts.utils import product_listing


def handle():
    categories = Category.objects.all()
    products = Product.objects.all()

    return product_listing(products, categories)


pprint(handle())

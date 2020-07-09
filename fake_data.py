# base importing
import os, django, random
from django.db import connection

# configure settings for project
# need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()

# faker importing
from faker import Faker
# custom app models importing
from products_category.models import Category, Product

# creating Faker object
fake_data = Faker()

# custom data based on needs
category_name_list = [
    'Bike', 'Mobile', 'Production/Operation', 'Accounting/Finance', 'Garments/Textile',
    'Education/Training', 'Medical/Pharma', 'Marketing/Sales'
]

product_name_list = [
    'Samsung', 'Brain Station', 'SouthTech', 'Ador Composite Ltd', 'Texstream Fashion Ltd', 'DreamOnline Limited',
    'AKH Knitting', 'Rim Leather Ltd.', 'Akij Bakers Ltd.', 'M.N Group', 'Partex Star Group', 'UBF Bridal Ltd.',
    'IUBAT',
    'Dikkha Online', 'PRAN-RFL Group', 'Friendship', 'Rupayan Group', 'Paragon Group'
]

price_list = ['100', '200', '399', '500']
quantity_list = ['3', '5', '7', '8']
in_stock_list = ['10', '20', '39', '50']
supplier_name_list = ['tt', 'ifrana', 'farhana', 'hr']


# 1st, creating the priority object with fake data
def add_category():
    category = Category.objects.get_or_create(
        name=random.choice(category_name_list),
    )[0]

    # note: [0] = Usage of get_or_create() method, if priority object already exists then get from first index.
    # if not, then create the priority object.

    # saving priority obj
    category.save()

    # returning priority obj
    return category


# populating the other classes
def populate(n):
    for entry in range(n):
        # 1st, calling priority method for creating priority object first
        category = add_category()

        # 2nd, creating next objects with previously created priority object
        Product.objects.get_or_create(

            product_name=random.choice(product_name_list),
            price=random.choice(price_list),
            quantity=random.choice(quantity_list),
            in_stock=random.choice(in_stock_list),
            supplier_name=random.choice(supplier_name_list),

            category=category,
        )


# calling the populate() method
if __name__ == '__main__':
    print("** Populating the Database, Please Wait...")
    populate(10)
    print('** Populating Complete!')

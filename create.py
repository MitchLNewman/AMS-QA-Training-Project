from app import app
from application import db, bcrypt
from application.models import Product, Category, User, Orders, OrderItem, Cart, CartItem, WishList, CartDisplay, PaymentDetails
from datetime import datetime


# Standard create.py code from previous work 

with app.app_context():
    db.drop_all()
    db.create_all()

# Creates the categories for Phones, Laptops and TVs

    from application.models import Product
    phones = Category(name='Phones')
    laptops = Category(name='Laptops')
    tvs = Category(name='TVs')
    db.session.add(phones)
    db.session.add(laptops)
    db.session.add(tvs)
    db.session.commit()

    # Product page code for phones including link to image and description 

    phone_1 = Product(name='iPhone 12 Pro', price=500, image="images/iphone_12_pro.jpg", description='Originally released in October 2020.', category_id=1)
    phone_2 = Product(name='Samsung Galaxy S20', price=400, image="images/samsung_galaxy_s20.jpg", description='Originally released in Feburary 2020.', category_id=1)
    phone_3 = Product(name='Google Pixel 5', price=300, image="images/google_pixel_5.jpg", description='Originally released in October 2020.', category_id=1)
    phone_4 = Product(name='OnePlus 8T', price=200, image="images/oneplus_8t.jpg", description='Originally released in October 2020.', category_id=1)
    phone_5 = Product(name='Huawei P40 Pro', price=100, image="images/huawei_p40_pro.jpg", description='Originally released in April 2020.', category_id=1)
    db.session.add(phone_1)
    db.session.add(phone_2)
    db.session.add(phone_3)
    db.session.add(phone_4)
    db.session.add(phone_5)
    db.session.commit()

    # Product page code for laptops including link to image and description 

    laptop_1 = Product(name='MacBook Pro', price=500, image="images/macbook_pro.jpg", description='Apple M2 chip, 8-core CPU, 10-core GPU, 8GB RAM, 512GB SSD.', category_id=2)
    laptop_2 = Product(name='Dell XPS 13', price=400, image="images/dell_xps_13.jpg", description='Intel i7, Windows 11, 8GB RAM, 512GB SSD.', category_id=2)
    laptop_3 = Product(name='Lenovo ThinkPad X1 Carbon', price=300, image="images/lenovo_thinkpad_x1_carbon.jpg", description='Intel i7, Windows 11, 16GB RAM, 1TB SSD.', category_id=2)
    laptop_4 = Product(name='HP Envy 13', price=200, image="images/hp_envy_13.jpg", description='Intel i7, Windows 11, 16GB RAM, 1TB SSD.', category_id=2)
    laptop_5 = Product(name='Microsoft Surface Laptop 3', price=100, image="images/microsoft_surface_3.jpg", description='Intel i7, Windows 11, 8GB RAM, 512GB SSD.', category_id=2)
    db.session.add(laptop_1)
    db.session.add(laptop_2)
    db.session.add(laptop_3)
    db.session.add(laptop_4)
    db.session.add(laptop_5)
    db.session.commit()

     # Product page code for TVs including link to image and description 
    
    tv_1 = Product(name='Samsung Q90 QLED TV', price=500, image="images/samsung_q90.jpg", description='Good TV i guess I know nothing about TVs.', category_id=3)
    tv_2 = Product(name='LG CX OLED TV', price=400, image="images/lg_cx_qled.jpg", description='Good TV i guess I know nothing about TVs.', category_id=3)
    tv_3 = Product(name='Samsung Q80T QLED TV', price=300, image="images/samsung_q80t.jpg", description='Good TV i guess I know nothing about TVs.', category_id=3)
    tv_4 = Product(name='Sony Bravia A8H OLED TV', price=200, image="images/sony_bravia.jpg", description='Good TV i guess I know nothing about TVs.', category_id=3)
    tv_5 = Product(name='TCL 6-Series QLED TV', price=100, image="images/tcl_6series.jpg", description='Good TV i guess I know nothing about TVs.', category_id=3)
    db.session.add(tv_1)
    db.session.add(tv_2)
    db.session.add(tv_3)
    db.session.add(tv_4)
    db.session.add(tv_5)
    db.session.commit()

    # Test users for login - can also use the created signup sheet to create an account to access the cart

    user_mitch = User(name='Mitch', password=bcrypt.generate_password_hash('password'), email="Mitch@qa.com", address="1 Mitch Street", postcode=" MIT 3S", phone="01234567890")
    
    user_josh = User(name='Josh', password=bcrypt.generate_password_hash('password'), email="josh@qa.com", address="1 Josh Street", postcode="JOS 3M", phone="01234567890")
    
    user_olly = User(name='Olly', password=bcrypt.generate_password_hash('password'), email="Olly@qa.com'", address="1 Olly Street", postcode="OLL 3N", phone="01234567890")
    
    db.session.add(user_mitch)
    db.session.add(user_josh)
    db.session.add(user_olly)
    db.session.commit()
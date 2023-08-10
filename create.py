from app import app
from application import db, bcrypt
from application.models import Product
from datetime import datetime


with app.app_context():
    db.drop_all()
    db.create_all()

    from application.models import Product

    phone = Product(name='Mobile Phone', price=500, description='Android', category='Electronics')
    db.session.add(phone)
    db.session.commit()
    print (phone)
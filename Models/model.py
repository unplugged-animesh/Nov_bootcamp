from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(25),unique=True,nullable=False)
    email=db.Column(db.String(),unique=True,nullable=False)
    password=db.Column(db.String(12),nullable=False)
    user_cart=db.relationship("Cart",backref="User",lazy=True,cascade='all,delete-orphan')

#if user_query_filter_by for admin creation

    
class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True,nullable=False)
    products=db.relationship("Product",backref="Category",lazy=True,cascade="all,delete-orphan")

    
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True,nullable=False)
    price=db.Column(db.Float,nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    mf_date=db.Column(db.Date,nullable=False)
    expiry_date=db.Column(db.Date,nullable=False)
    category_id=db.Column(db.Integer,db.ForeignKey("category.id"),nullable=False)
    
    
    
        
    
    
    
    
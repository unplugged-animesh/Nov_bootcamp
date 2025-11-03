from flask import Flask
from Models.model import *


app=Flask(__name__)
app.config['SECRET_KEY']="East"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///grocery_store.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db.init_app(app)

with app.app_context():
    db.create_all()
    
#admin-credentials:for admin creation
    
    
if __name__=="__main__":
    app.run(port=5000,debug=True)
    
    
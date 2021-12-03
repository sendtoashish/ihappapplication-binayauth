from app import db, User, Product, photos
from passlib.hash import sha256_crypt
from werkzeug.datastructures import FileStorage

####Create Admin User###########
admin = User()
admin.username = "admin"
password = sha256_crypt.hash("1234")
admin.password = password
admin.admin = True
db.session.add(admin)
db.session.commit()
print("Admin Created successfully")


#####Add Sample products#######


p1 = Product()
p1.name = "Handloom Saree"
p1.price = 4999
p1.description = "Handloom saree woven diligently and by skilled artisans"
p1.stock = 10
p1.image = "http://127.0.0.1:5000/_uploads/photos/handloomsaree.jpg"

p2 = Product()
p2.name = "Pashmina Shawl"
p2.price = 9999
p2.description = "100% Original Pasmina Shawl, also called soft gold. Made by grassroot artisians"
p2.stock = 5
p2.image = "http://127.0.0.1:5000/_uploads/photos/pashmina-shawl.jpg"

p3 = Product()
p3.name = "Embroidered Scarf"
p3.price = 1000
p3.description = "Embriodered scarf in excting and vibrant design"
p3.stock = 4
p3.image = "http://127.0.0.1:5000/_uploads/photos/embriodered-scarf.jpg"



p4 = Product()
p4.name = "Wooden Bangle"
p4.price = 400
p4.description = "Wooden bangle hand painted with vibrant colours"
p4.stock = 15
p4.image = "http://127.0.0.1:5000/_uploads/photos/woodenbangle.jpg"


p5 = Product()
p5.name = "Tribal Painting"
p5.price = 5000
p5.description = "Indian Tribal Painting done on paper, wall mounted"
p5.stock = 3
p5.image = "http://127.0.0.1:5000/_uploads/photos/painting.jpg"


p6 = Product()
p6.name = "Statue"
p6.price = 1000
p6.description = "Statue of Lord Ganesha, handmade in brass metal"
p6.stock = 7
p6.image = "http://127.0.0.1:5000/_uploads/photos/statue.jpg"


db.session.add_all([p1,p2,p3,p4,p5,p6])
db.session.commit()
print("Products added successfully")

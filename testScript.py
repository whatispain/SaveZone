from api import app,Users
from werkzeug.security import generate_password_hash, check_password_hash

print(Users.query.all())
login = "root"
password = "root"
user = Users.query.filter(Users.login == login).all()
print(user[0].password)
print(check_password_hash(user[0].password,password))

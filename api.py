'''Что в планах?
    Сделать бд: Таблица авторизации. Готово
    Сделать регистрацию нового пользователя от имени root

    '''
from flask import Flask, jsonify, request,abort,make_response
from searchSummariesInVk import TakeTopAdress
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

#import database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/db_for_py_safe_zone'

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<users {self.id}>"

# Пример запроса к api
# 127.0.0.1:5024/create_new_user?login=root&password=root&newUserLogin=uzver&newUserPassword=root
@app.route('/create_new_user', methods=['GET'])
async def create_new_user():
    if (InvalidAutch(request.values["login"], request.values["password"], "su")):
        abort(400)
    try:
        db.session.add(Users(login=request.values["newUserLogin"],password=generate_password_hash(request.values["password"])))
        db.session.flush()
        db.session.commit()
    except:
        db.session.rollback()
        print("Ошибка")
        return jsonify("Ошибка")
    return jsonify("cool")
#127.0.0.1:5024/get_streets_list?login=root&password=root
@app.route('/get_streets_list', methods=['GET'])
async def get_streets_list():
    if(InvalidAutch(request.values["login"], request.values["password"])):
        abort(400)
    streets_list = ["Донецк, ул. Умова, 57", "Макеевка, ул. Садовая, 28"]
    #streets_list = await TakeTopAdress()
    return jsonify(streets_list)

def InvalidAutch(*args): #Проверка валидности учетных данных (login,password,helpArg)
    if(args[2]=="su"): # Проверить
        if args[0]!="root":
            return True

    user = Users.query.filter(Users.login == args[0]).all()
    if len(user):
        if check_password_hash(user[0].password, args[1]) == True:
            return False
    return True

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Invalid parameters'}), 400)

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=False, host="127.0.0.1", port=5024)




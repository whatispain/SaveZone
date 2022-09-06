from api import db,Users
from werkzeug.security import generate_password_hash, check_password_hash

if __name__ == '__main__':
    suLogin = "root"
    suPassword = "root"

    db.create_all()
    try:
        db.session.add(Users(login=suLogin,password=generate_password_hash(suPassword)))
        db.session.flush()
        db.session.commit()
    except:
        db.session.rollback()
        print("Ошибка")

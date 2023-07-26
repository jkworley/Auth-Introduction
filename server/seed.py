from app import app
from models import db, User

with app.app_context():

    print("Deleting all records...")
    User.query.delete()

    user_1 = User (
        username = 'Mii_12'
    )

    user_2 = User (
        username = 'coding_mollie'
    )

    db.session.add(user_1)
    db.session.add(user_2)

    db.session.commit()

    user_1_password = 'mii'

    user_2_password = 'p4ssw0rd'

    user_1.password_hash = user_1_password

    user_2.password_hash = user_2_password

    db.session.add(user_1)

    db.session.add(user_2)

    db.session.commit()
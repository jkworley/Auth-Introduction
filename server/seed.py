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
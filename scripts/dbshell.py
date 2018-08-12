from app.database import db, User, Transaction


def populate_test_data():
    db.create_tables([User, Transaction])

    user1 = User.create(
        name='Misha',
        email='bmwant@gmail.com',
        telegram_handle='test_telega1',
        wallet='somewallet1',
    )

    user2 = User.create(
        name='Vlad',
        email='imressed@gmail.com',
        telegram_handle='test_telega2',
        wallet='somewallet2',
    )

    trans1 = Transaction.create(
        user=user1,
        amount=150,
        diff=100,
        rate_opened=6444.3,
    )

    trans2 = Transaction.create(
        user = user2,
        amount=100,
        diff=200,
        rate_opened=6328.1,
    )


if __name__ == '__main__':
    populate_test_data()

from app.models import Owner


def test__create_owner(database):
    name = "Fulano de Tal"
    database.session.add(owner)
    database.session.commit()

    owner = Owner.query.first()

    assert owner.name == name
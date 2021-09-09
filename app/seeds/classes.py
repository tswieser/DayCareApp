from app.models import db, Class


def seed_class():
    new_class = Class(
        name="infant room", description="3 months to 1 year", school_id=1
    )

    db.session.add(new_class)
    db.session.commit()


def undo_class():
    db.session.execute('TRUNCATE classes RESTART IDENTITY CASCADE;')
    db.session.commit()

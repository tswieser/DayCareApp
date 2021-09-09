from app.models import db, School


def seed_school():
    aa_zz = School(name="aa-zz child care and learning center", location="2498 W Philadelphia St, York, PA 17404",
                   description="Hands-on, involved & passionate in the care of your children")

    db.session.add(aa_zz)

    db.session.commit()


def undo_school():
    db.session.execute('TRUNCATE schools RESTART IDENTITY CASCADE;')
    db.session.commit()

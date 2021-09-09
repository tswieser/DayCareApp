from .db import db


class Child(db.Model):
    __tablename__ = "children"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    profile_img_url = db.Column(db.Text)
    allergies = db.Column(db.Text)
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey(
        'school.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)

    users = db.relationship('User', back_populates='children')
    schools = db.relationship('School', back_populates='children')
    classes = db.relationship('Class', back_populates="children")
    reports = db.relationship('Report', back_populates="children")

    def to_dict(self):
        return{
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'birthday': self.birthday,
            'profile_img_url': self.profile_img_url,
            'allergies': self.allergies,
            'notes': self.notes,
        }

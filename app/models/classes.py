from .db import db


class Class(db.Model):
    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey(
        'schools.id'), nullable=False)

    users = db.relationship('User', back_populates='classes')
    schools = db.relationship('School', back_populates='classes')
    children = db.relationship('Child', back_populates="classes")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

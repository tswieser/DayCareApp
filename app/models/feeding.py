from .db import db


class Feeding(db.Model):
    __tablename__ = 'feedings'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    bottom = db.Column(db.Boolean)
    ounces = db.Column(db.Integer)
    amount = db.Column(db.String(50))
    description = db.Column(db.Text)
    report_id = db.Column(db.Integer, db.ForeignKey(
        'report.id'), nullable=False)

    reports = db.relationship('Report', back_populates='feedings')

    def to_dict(self):
        return{
            'id': self.id,
            'time': self.time,
            'bottom': self.bottom,
            'ounces': self.ounces,
            'amount': self.amount,
            'description': self.description,
        }

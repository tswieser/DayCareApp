from .db import db


class Bathroom(db.Model):
    __tablename__ = 'bathroom'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    status_cd = db.Column(db.String(50), nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey(
        'reports.id'), nullable=False)

    reports = db.relationship('Report', back_populates="bathroom")

    def to_dict(self):
        return{
            'id': self.id,
            'time': self.time,
            'status_cd': self.status_cd,
        }

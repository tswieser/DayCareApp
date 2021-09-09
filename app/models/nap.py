from .db import db


class Nap(db.Model):
    __tablename__ = "naps"

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime)
    status_cd = db.Column(db.String(50), nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey(
        'reports.id'), nullable=False)

    reports = db.relationship('Report', back_populates="naps")

    def to_dict(self):
        return{
            'id': self.id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'status_cd': self.status_cd,
        }

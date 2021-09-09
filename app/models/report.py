from .db import db


class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    arrival = db.Column(db.DateTime, nullable=False)
    departure = db.Column(db.DateTime)
    woke = db.Column(db.DateTime, nullable=False)
    last_ate = db.Column(db.DateTime)
    mood = db.Column(db.String(50), nullable=False)
    parent_comments = db.Column(db.Text)
    teacher_comments = db.Column(db.Text)
    needs_cd = db.Column(db.String(50))
    highlights = db.Column(db.Text)
    child_id = db.Column(db.Integer, db.ForeignKey('children.id'), nullable=False)

    children = db.relationship("Child", back_populates='reports')
    naps = db.relationship("Nap", back_populates="reports")
    bathroom = db.relationship("Bathroom", back_populates="reports")
    feedings = db.relationship("Feeding", back_populates="reports")

    def to_dict(self):
        return{
            'id': self.id,
            'arrival': self.arrival,
            'departure': self.departure,
            'woke': self.woke,
            'last_ate': self.last_ate,
            'mood': self.mood,
            'parent_comments': self.parent_comments,
            'teacher_comments': self.teacher_comments,
            'needs_cd': self.needs_cd,
            'highlights': self.highlights,
        }

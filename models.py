from database import db
from datetime import datetime

class Job(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)

    uuid = db.Column(db.String(100), unique=True)

    description = db.Column(db.Text)

    status = db.Column(db.String(20), default="queued")

    output_video = db.Column(db.String(255))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
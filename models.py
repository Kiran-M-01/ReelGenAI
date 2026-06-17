from database import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    uuid = db.Column(db.String(100), unique=True)

    description = db.Column(db.Text)

    status = db.Column(db.String(20), default="queued")

    output_video = db.Column(db.String(255))

    def __repr__(self):
        return f"<Job {self.id}>"
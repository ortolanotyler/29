"""Pet Models for the Adoption Application."""

from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://example.com/default-pet-image.gif"

db = SQLAlchemy()

class Pet(db.Model):
    """Model for adoptable pets."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Get the pet's image URL, either bespoke or generic."""
        return self.photo_url or GENERIC_IMAGE

def connect_db(app):
    """Connect the database to the provided Flask app."""
    db.app = app
    db.init_app(app)

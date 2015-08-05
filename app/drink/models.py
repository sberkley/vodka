from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a User model
class Drink(Base):

    __tablename__ = 'drinks'

    name = db.Column(db.String(128),  nullable=False)
    abv = db.Column(db.Integer)
    with_ice = db.Column(db.Boolean)
    first_tried_on = db.Column(db.Date)

    # New instance instantiation procedure
    def __init__(self, name, abv, with_ice, first_tried_on):
        self.name     = name
        self.abv    = abv
        self.with_ice = with_ice
        self.first_tried_on = first_tried_on

    def __repr__(self):
        return '<Drink %r>' % (self.name)

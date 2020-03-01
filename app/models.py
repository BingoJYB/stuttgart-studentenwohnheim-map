from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class HousingInfo(db.Model):
    __tablename__ = 'housing_info'
    id = db.Column(db.Integer,
                   primary_key=True)
    image = db.Column(db.Text,
                      index=False,
                      unique=True,
                      nullable=False)
    name = db.Column(db.String(80),
                     index=True,
                     unique=True,
                     nullable=False)
    address = db.Column(db.Text,
                        index=False,
                        unique=True,
                        nullable=False)
    price = db.Column(db.Text,
                      index=False,
                      unique=False,
                      nullable=False)
    detail = db.Column(db.Text,
                       index=False,
                       unique=False,
                       nullable=False)

    def __repr__(self):
        return '<House {}>'.format(self.name)

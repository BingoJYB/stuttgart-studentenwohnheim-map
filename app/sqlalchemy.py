from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class WohnungInfo(db.Model):
    __tablename__ = 'wohnung_info'
    id = db.Column(db.Integer,
                   primary_key=True)
    image = db.Column(db.Text,
                      index=False,
                      unique=False,
                      nullable=False)
    name = db.Column(db.String(80),
                     index=False,
                     unique=False,
                     nullable=False)
    address = db.Column(db.Text,
                        index=True,
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
        return '<Wohnung {}>'.format(self.name)

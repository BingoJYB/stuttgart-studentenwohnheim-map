from flask import current_app, Blueprint, render_template

from app.models import db, HousingInfo
from app.scraper import WebScraper


my_app = Blueprint('my_app', __name__,
                   template_folder='templates')


@my_app.route('/')
def index():
    ws = WebScraper(current_app.config['HOUSING_URL'])
    houses = ws.parse_page()

    for housing_info in houses:
        existing_house = HousingInfo.query.filter_by(
            address=housing_info['address']).first()

        if existing_house:
            existing_house.image = housing_info['image']
            existing_house.name = housing_info['name']
            existing_house.price = housing_info['price']
            existing_house.detail = housing_info['detail']
        else:
            house = HousingInfo(
                image=housing_info['image'],
                name=housing_info['name'],
                address=housing_info['address'],
                price=housing_info['price'],
                detail=housing_info['detail']
            )
            db.session.add(house)

        db.session.commit()

    return render_template('index.html', name='World')

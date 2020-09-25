from flask import current_app, Blueprint, render_template

from app.sqlalchemy import db, WohnungInfo
from app.scraper import WebScraper


my_app = Blueprint('my_app', __name__,
                   template_folder='templates')


@my_app.route('/')
def index():
    ws = WebScraper(current_app.config['WOHNUNG_URL'])
    studentenwohnheim = ws.parse_page()

    for wohnung_info in studentenwohnheim.wohnungen:
        existing_wohnung = WohnungInfo.query.filter_by(
            address=wohnung_info.address).first()

        if existing_wohnung:
            existing_wohnung.image = wohnung_info.image
            existing_wohnung.name = wohnung_info.name
            existing_wohnung.price = wohnung_info.price
            existing_wohnung.detail = wohnung_info.detail
        else:
            wohnung = WohnungInfo(
                image=wohnung_info.image,
                name=wohnung_info.name,
                address=wohnung_info.address,
                price=wohnung_info.price,
                detail=wohnung_info.detail
            )
            db.session.add(wohnung)

        db.session.commit()

    return render_template('index.html', name='World')

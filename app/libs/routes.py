from flask import Blueprint, render_template

from app.libs.sqlalchemy import db, WohnungInfo
from app.libs.scraper import WebScraper
from app.libs.utilities import get_map_api_key, get_wohnung_detail_url, get_wohnung_url


my_app = Blueprint('my_app', __name__,
                   template_folder='templates')


@my_app.route('/')
def index():
    ws = WebScraper(get_wohnung_url())
    ws.parse_page()

    for wohnung_info in ws.studentenwohnheim.wohnungen:
        existing_wohnung = WohnungInfo.query.filter_by(
            address=wohnung_info.address).first()

        if existing_wohnung:
            existing_wohnung.image = wohnung_info.image_url
            existing_wohnung.name = wohnung_info.name
            existing_wohnung.price = wohnung_info.price
            existing_wohnung.detail = wohnung_info.detail_url
        else:
            wohnung = WohnungInfo(
                image=wohnung_info.image_url,
                name=wohnung_info.name,
                address=wohnung_info.address,
                price=wohnung_info.price,
                detail=wohnung_info.detail_url
            )
            db.session.add(wohnung)

        db.session.commit()

    # ws.download_images()

    wohnungen = [(wohnung.name, wohnung.address, get_wohnung_detail_url(
        wohnung.detail_url)) for wohnung in ws.studentenwohnheim]

    return render_template('index.html',
                           api_key=get_map_api_key(),
                           wohnungen=wohnungen)

from app.scraper import WebScraper

from flask import current_app, Blueprint, render_template


my_app = Blueprint('my_app', __name__,
                   template_folder='templates')


@my_app.route('/')
def index():
    ws = WebScraper(current_app.config['URL'])
    ws.parse_page()
    return render_template('index.html', name='World')

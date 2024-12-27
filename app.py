import sqlite3
from flask import Flask, render_template, jsonify
from src.scrapers.site_scraper import SiteScraper
from src.database.db_handler import DatabaseHandler
import yaml

app = Flask(__name__)

def load_config():
    with open('config/config.yaml', 'r') as f:
        return yaml.safe_load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    config = load_config()
    db_handler = DatabaseHandler(config['database']['path'])
    scraper = SiteScraper(config['scraping']['base_url'], db_handler)
    data = scraper.scrape()
    return jsonify({'status': 'success', 'items': len(data)})

@app.route('/data')
def get_data():
    try:
        db_handler = DatabaseHandler('data/scraper.db')
        with sqlite3.connect(db_handler.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM scraped_data ORDER BY created_at DESC')
            columns = [description[0] for description in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
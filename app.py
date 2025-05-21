import json
import os

from flask import Flask, render_template, request, redirect, url_for
from mobiles_data import mobiles

app = Flask(__name__)

# Load mobile data from JSON file
def load_mobile_data():
    # Check if the file exists, if not create it with sample data
    # if not os.path.exists("mobiles.json"):
    create_sample_data()
    
    with open("mobiles.json", "r") as f:
        mobiles = json.load(f)
    return mobiles

# Create sample data for initial setup
def create_sample_data():
    with open("mobiles.json", "w") as f:
        json.dump(mobiles, f, indent=4)

# Routes
@app.route('/')
def home():
    mobiles = load_mobile_data()
    return render_template('index.html', mobiles=mobiles["homepage_smartphones"])

@app.route('/price-category/<price_range>')
def price_category(price_range):
    mobiles = load_mobile_data()
    filtered_mobiles = []
    
    # Define price ranges
    ranges = {
        "under-10000": (0, 10000),
        "under-15000": (10001, 15000),
        "under-20000": (15001, 20000),
        "under-25000": (20001, 25000),
        "under-30000": (25001, 30000),
        "under-40000": (30001, 40000),
        "above-40000": (40001, float('inf'))
    }
    
    if price_range in ranges:
        min_price, max_price = ranges[price_range]
        filtered_mobiles = [mobile for mobile in mobiles["smartphones"] 
                           if min_price <= mobile["price"] <= max_price]
    
    return render_template('category.html', 
                           mobiles=filtered_mobiles, 
                           category=price_range.replace('-', ' ').title())

@app.route('/brand/<brand_name>')
def brand_category(brand_name):
    mobiles = load_mobile_data()
    filtered_mobiles = [mobile for mobile in mobiles["smartphones"] 
                      if mobile["brand"].lower() == brand_name.lower()]
    
    return render_template('category.html', 
                         mobiles=filtered_mobiles, 
                         category=f"{brand_name} Smartphones")

@app.route('/mobile/<mobile_id>')
def mobile_detail(mobile_id):
    mobiles = load_mobile_data()
    mobile = next((m for m in mobiles["smartphones"] if m["id"] == mobile_id), None)
    
    if not mobile:
        return redirect(url_for('home'))
    
    return render_template('mobile_detail.html', mobile=mobile)

@app.route('/compare')
def compare():
    mobiles = load_mobile_data()
    return render_template('compare.html', mobiles=mobiles["smartphones"])

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    mobiles = load_mobile_data()
    
    if not query:
        return redirect(url_for('home'))
    
    filtered_mobiles = [mobile for mobile in mobiles["smartphones"]
                      if query in mobile["name"].lower() or 
                         query in mobile["brand"].lower() or
                         query in str(mobile["price"])]
    
    return render_template('category.html', 
                         mobiles=filtered_mobiles, 
                         category=f"Search Results for '{query}'")

if __name__ == '__main__':
    app.run(debug=True)
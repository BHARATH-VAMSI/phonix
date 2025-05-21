# Mobile Recommendation Website

A beautiful Flask-based mobile recommendation website with category-based browsing, detailed specifications, and comparison features.

## Features

- Browse smartphones by price range (Under ₹10,000, ₹20,000, ₹30,000, ₹40,000)
- Browse smartphones by brand
- View detailed specifications for each smartphone
- Compare up to three smartphones side-by-side
- Responsive design that works on all devices
- Search functionality to find smartphones by name, brand, or price

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Flask

### Installation

1. Clone the repository or download the source code

2. Create a virtual environment (recommended)
   ```
   python -m venv venv
   ```

3. Activate the virtual environment
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies
   ```
   pip install flask
   ```

5. Create the necessary directories for static files
   ```
   mkdir -p static/images
   ```

6. Create the placeholder image
   - Save the SVG content from `static_placeholder.svg` as `static/images/placeholder.png`
   - Or use any smartphone image of your choice

7. Run the application
   ```
   python app.py
   ```

8. Open your browser and navigate to `http://127.0.0.1:5000/`

## Project Structure

```
mobile-recommendation-website/
├── app.py                  # Main Flask application
├── mobiles.json            # Database of smartphones (auto-created)
├── static/                 # Static files
│   └── images/             # Image files
│       └── placeholder.png # Placeholder image for smartphones
└── templates/              # HTML templates
    ├── layout.html         # Base layout template
    ├── index.html          # Homepage
    ├── category.html       # Category/filtered results page
    ├── mobile_detail.html  # Detailed smartphone page
    └── compare.html        # Comparison page
```

## Customization

### Adding Real Images

To add real images for the smartphones:

1. Place the images in the `static/images/` directory
2. Name the images according to the `image` field in the `mobiles.json` file

### Adding More Smartphones

You can add more smartphones by editing the `mobiles.json` file directly or by implementing an admin interface.

### Changing Price Categories

To modify the price categories:

1. Edit the price ranges in the `app.py` file in the `price_category` route
2. Update the corresponding links in `templates/layout.html` and `templates/index.html`

## Future Enhancements

- User authentication and personalized recommendations
- User reviews and ratings
- Price history tracking
- Stock availability information
- Advanced filtering options (e.g., RAM, processor, camera)
- Mobile specification data scraping from online sources

## License

This project is for educational purposes only.

## Acknowledgements

- Flask - The web framework used
- Font Awesome - Icons
- Google Fonts - Poppins font family
"# phonix" 

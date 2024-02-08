import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remarcable.settings')
django.setup()

from products.models import Product, Category, Tag

products_data = [
    {
        'name': 'Nike Air Max 90',
        'category': 'Footwear',
        'tags': ['Sneakers', 'Athletic Shoes', 'Air Cushioning', 'Classic Design', 'Comfortable', 'Iconic Brand']
    },
    {
        'name': 'Apple iPhone 12',
        'category': 'Electronics',
        'tags': ['Smartphone', 'iOS', 'Touchscreen', 'Camera', 'High-performance', 'Sleek Design']
    },
    {
        'name': 'Levi’s 501 Jeans',
        'category': 'Clothing',
        'tags': ['Denim', 'Classic Fit', 'Button Fly', 'Timeless Style', 'Durable', 'Versatile']
    },
    {
        'name': 'Coca-Cola Original',
        'category': 'Beverages',
        'tags': ['Soft Drink', 'Carbonated', 'Refreshing', 'Classic Taste', 'Iconic Brand', 'Caffeine']
    },
    {
        'name': 'Sony PlayStation 5',
        'category': 'Gaming',
        'tags': ['Console', 'Next-gen Gaming', '4K Gaming', 'DualSense Controller', 'High Performance', 'Exclusive Games']
    },
    {
        'name': 'Adidas Stan Smith',
        'category': 'Footwear',
        'tags': ['Sneakers', 'Classic Design', 'Leather Upper', 'Timeless Style', 'Comfortable', 'Iconic Brand']
    },
    {
        'name': 'Amazon Echo Dot',
        'category': 'Electronics',
        'tags': ['Smart Speaker', 'Voice Assistant', 'Alexa', 'Compact Design', 'Bluetooth', 'Streaming Music']
    },
    {
        'name': 'Gap T-Shirt',
        'category': 'Clothing',
        'tags': ['Cotton', 'Short Sleeve', 'Basic Tee', 'Comfortable Fit', 'Versatile', 'Affordable']
    },
    {
        'name': 'Lays Classic Potato Chips',
        'category': 'Snacks',
        'tags': ['Potato Chips', 'Crispy', 'Salty', 'Snack', 'Classic Flavor', 'Popular Brand']
    },
    {
        'name': 'Samsung Galaxy Watch',
        'category': 'Wearable Tech',
        'tags': ['Smartwatch', 'Fitness Tracker', 'Heart Rate Monitor', 'Water-resistant', 'Long Battery Life', 'Tizen OS']
    },
    {
        'name': 'Ray-Ban Wayfarer Sunglasses',
        'category': 'Eyewear',
        'tags': ['Sunglasses', 'Classic Design', 'UV Protection', 'Iconic Style', 'Durable', 'Fashionable']
    },
    {
        'name': 'Dell Inspiron Laptop',
        'category': 'Computers',
        'tags': ['Laptop', 'Windows', 'Intel Processor', 'Full HD Display', 'Slim Design', 'Reliable Performance']
    },
    {
        'name': 'Hanes Men’s Boxer Briefs',
        'category': 'Clothing',
        'tags': ['Underwear', 'Cotton', 'Comfortable Fit', 'Supportive', 'Multipack', 'Affordable']
    },
    {
        'name': 'Colgate Total Toothpaste',
        'category': 'Personal Care',
        'tags': ['Toothpaste', 'Oral Health', 'Fluoride', 'Cavity Protection', 'Fresh Breath', 'Trusted Brand']
    },
    {
        'name': 'Nintendo Switch',
        'category': 'Gaming',
        'tags': ['Console', 'Handheld', 'Hybrid Gaming', 'Joy-Con Controllers', 'Exclusive Games', 'Portable']
    },
    {
        'name': 'Nike Dri-FIT T-Shirt',
        'category': 'Clothing',
        'tags': ['Sportswear', 'Moisture-wicking', 'Breathable Fabric', 'Comfortable Fit', 'Athletic', 'Versatile']
    },
    {
        'name': 'Nivea Moisturizing Cream',
        'category': 'Personal Care',
        'tags': ['Skincare', 'Moisturizer', 'Hydrating', 'Sensitive Skin', 'Trusted Brand', 'Affordable']
    },
    {
        'name': 'Sharpie Permanent Markers',
        'category': 'Stationery',
        'tags': ['Markers', 'Permanent Ink', 'Assorted Colors', 'Fine Point', 'Versatile', 'High Quality']
    },
    {
        'name': 'Converse Chuck Taylor All Star',
        'category': 'Footwear',
        'tags': ['Sneakers', 'Canvas Upper', 'Classic Design', 'High Top', 'Comfortable', 'Timeless Style']
    },
    {
        'name': 'Kleenex Facial Tissues',
        'category': 'Household Essentials',
        'tags': ['Facial Tissues', 'Soft', 'Absorbent', 'Multi-purpose', 'Trusted Brand', 'Convenient']
    },
    {
        'name': 'Play-Doh Modeling Compound',
        'category': 'Toys & Games',
        'tags': ['Art & Craft', 'Creativity', 'Non-toxic', 'Colorful', 'Fun', 'Sensory Play']
    }
]


def import_products():
    for product_data in products_data:
        category, _ = Category.objects.get_or_create(name=product_data['category'])

        product = Product.objects.create(name=product_data['name'], category=category)

        tags = []
        for tag_name in product_data['tags']:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
        product.tags.set(tags)

        print(f"Imported product: {product}")

if __name__ == '__main__':
    import_products()

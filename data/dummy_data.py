"""
Dummy Data for E-Commerce Application
Contains sample products and reviews for testing
"""

from ecommerce_app import Product, Review, Sentiment

# Sample dummy data that can be extended
DUMMY_PRODUCTS = [
    Product(1, "Laptop", 999.99, [
        Review("John", 5, "Great performance!", Sentiment.POSITIVE),
        Review("Sarah", 5, "Very fast", Sentiment.POSITIVE),
        Review("Mike", 3, "It's okay", Sentiment.NEUTRAL),
        Review("Tom", 2, "Battery issues", Sentiment.NEGATIVE),
    ]),
    
    Product(2, "Headphones", 149.99, [
        Review("Alex", 5, "Amazing sound!", Sentiment.POSITIVE),
        Review("Lisa", 4, "Good quality", Sentiment.POSITIVE),
        Review("Chris", 3, "Nothing special", Sentiment.NEUTRAL),
        Review("David", 1, "Broke quickly", Sentiment.NEGATIVE),
    ]),
    
    Product(3, "Phone", 799.99, [
        Review("Emma", 5, "Best phone ever!", Sentiment.POSITIVE),
        Review("Jack", 4, "Really good", Sentiment.POSITIVE),
        Review("Nina", 3, "Average", Sentiment.NEUTRAL),
        Review("Bob", 2, "Overheats", Sentiment.NEGATIVE),
    ]),
    
    Product(4, "Keyboard", 89.99, [
        Review("Zoe", 5, "Perfect for typing!", Sentiment.POSITIVE),
        Review("Paul", 4, "Very comfortable", Sentiment.POSITIVE),
        Review("Rachel", 3, "Decent", Sentiment.NEUTRAL),
        Review("Steve", 1, "Keys stuck", Sentiment.NEGATIVE),
    ]),
    
    Product(5, "Monitor", 349.99, [
        Review("Anna", 5, "Clear display!", Sentiment.POSITIVE),
        Review("Mark", 5, "Love it", Sentiment.POSITIVE),
        Review("Kate", 3, "Okay screen", Sentiment.NEUTRAL),
        Review("Leo", 2, "Color issues", Sentiment.NEGATIVE),
    ]),
]

def get_all_products():
    """Return all dummy products"""
    return DUMMY_PRODUCTS

def get_product_by_id(product_id):
    """Get a product by ID"""
    for product in DUMMY_PRODUCTS:
        if product.id == product_id:
            return product
    return None

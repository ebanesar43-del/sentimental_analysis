"""
E-Commerce Website Application
Displays products with reviews categorized by sentiment (Positive, Negative, Neutral)
"""

from dataclasses import dataclass
from typing import List
from enum import Enum
from datetime import datetime, timedelta
import random


class Sentiment(Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"


@dataclass
class Review:
    reviewer_name: str
    rating: int  # 1-5
    comment: str
    date: str
    sentiment: Sentiment

    def __repr__(self):
        return f"⭐ {self.rating}/5 - {self.reviewer_name} ({self.sentiment.value}) | {self.comment}"


@dataclass
class Product:
    product_id: int
    name: str
    category: str
    price: float
    stock: int
    description: str
    reviews: List[Review]

    def get_average_rating(self) -> float:
        if not self.reviews:
            return 0
        return round(sum(r.rating for r in self.reviews) / len(self.reviews), 2)

    def get_reviews_by_sentiment(self, sentiment: Sentiment) -> List[Review]:
        return [r for r in self.reviews if r.sentiment == sentiment]

    def __repr__(self):
        avg_rating = self.get_average_rating()
        return f"[{self.product_id}] {self.name} | ${self.price} | Stock: {self.stock} | Rating: {avg_rating}/5 ⭐"


class ECommerceApp:
    def __init__(self):
        self.products = []
        self.cart = []
        self.load_dummy_data()

    def load_dummy_data(self):
        """Load dummy products with reviews"""
        reviews_data = {
            1: [  # Laptop Reviews
                Review("John Doe", 5, "Excellent performance! Worth every penny.", "2024-01-15", Sentiment.POSITIVE),
                Review("Sarah Smith", 5, "Great build quality and fast processing.", "2024-01-18", Sentiment.POSITIVE),
                Review("Mike Johnson", 4, "Good laptop, battery could be better.", "2024-01-20", Sentiment.POSITIVE),
                Review("Emily Davis", 3, "It's okay, nothing special.", "2024-01-22", Sentiment.NEUTRAL),
                Review("Tom Wilson", 2, "Overheats frequently, disappointed.", "2024-01-25", Sentiment.NEGATIVE),
                Review("Lisa Brown", 1, "Crashed after a week, horrible experience.", "2024-01-28", Sentiment.NEGATIVE),
            ],
            2: [  # Wireless Headphones
                Review("Alex Turner", 5, "Amazing sound quality!", "2024-02-01", Sentiment.POSITIVE),
                Review("Jessica Parker", 5, "Perfect for work calls and music.", "2024-02-03", Sentiment.POSITIVE),
                Review("Chris Green", 4, "Good, but a bit pricey.", "2024-02-05", Sentiment.POSITIVE),
                Review("Rachel White", 3, "Average headphones, nothing remarkable.", "2024-02-07", Sentiment.NEUTRAL),
                Review("David Black", 2, "Bluetooth connection drops often.", "2024-02-09", Sentiment.NEGATIVE),
            ],
            3: [  # USB-C Cable
                Review("Nathan Hall", 5, "Durable and reliable!", "2024-02-10", Sentiment.POSITIVE),
                Review("Olivia Martin", 4, "Good quality, fast charging.", "2024-02-12", Sentiment.POSITIVE),
                Review("Lucas Lee", 3, "Works fine, standard cable.", "2024-02-14", Sentiment.NEUTRAL),
                Review("Sophia Garcia", 2, "Stopped working after 2 months.", "2024-02-16", Sentiment.NEGATIVE),
                Review("Benjamin Rodriguez", 1, "Defective product from day one.", "2024-02-18", Sentiment.NEGATIVE),
            ],
            4: [  # Mechanical Keyboard
                Review("Charlotte Clark", 5, "Best keyboard I've ever used!", "2024-02-20", Sentiment.POSITIVE),
                Review("Mason Lewis", 5, "Great tactile feedback, excellent for gaming.", "2024-02-22", Sentiment.POSITIVE),
                Review("Amelia Walker", 4, "Nice keyboard, a bit loud.", "2024-02-24", Sentiment.POSITIVE),
                Review("Ethan Young", 3, "Decent keyboard, nothing exceptional.", "2024-02-26", Sentiment.NEUTRAL),
                Review("Harper Hernandez", 1, "Broke within a month, poor build quality.", "2024-02-28", Sentiment.NEGATIVE),
            ],
            5: [  # 4K Monitor
                Review("Logan King", 5, "Stunning display quality!", "2024-03-01", Sentiment.POSITIVE),
                Review("Isabella Wright", 5, "Perfect for video editing and design work.", "2024-03-03", Sentiment.POSITIVE),
                Review("Jacob Lopez", 3, "Good monitor, expensive.", "2024-03-05", Sentiment.NEUTRAL),
                Review("Mia Hill", 2, "Some color accuracy issues.", "2024-03-07", Sentiment.NEGATIVE),
                Review("Lucas Scott", 1, "Arrives defective, customer service unresponsive.", "2024-03-09", Sentiment.NEGATIVE),
            ],
        }

        products = [
            Product(
                1, "Laptop Pro 15", "Electronics", 1299.99, 45,
                "High-performance laptop with Intel i7, 16GB RAM, 512GB SSD",
                reviews_data[1]
            ),
            Product(
                2, "Wireless Headphones", "Audio", 199.99, 120,
                "Noise-canceling Bluetooth headphones with 30-hour battery life",
                reviews_data[2]
            ),
            Product(
                3, "USB-C Cable 2M", "Accessories", 14.99, 500,
                "Fast charging USB-C cable with 6ft length",
                reviews_data[3]
            ),
            Product(
                4, "Mechanical Keyboard", "Peripherals", 149.99, 85,
                "RGB mechanical keyboard with Cherry MX switches",
                reviews_data[4]
            ),
            Product(
                5, "4K Monitor 27\"", "Monitors", 449.99, 30,
                "27-inch 4K UHD IPS display with 60Hz refresh rate",
                reviews_data[5]
            ),
        ]

        self.products = products

    def display_all_products(self):
        """Display all products in a formatted table"""
        print("\n" + "="*100)
        print("📦 PRODUCTS CATALOG".center(100))
        print("="*100)
        for product in self.products:
            print(product)
        print("="*100 + "\n")

    def display_product_details(self, product_id: int):
        """Display detailed information about a product including all reviews"""
        product = next((p for p in self.products if p.product_id == product_id), None)

        if not product:
            print(f"❌ Product with ID {product_id} not found!")
            return

        print("\n" + "="*100)
        print(f"📄 PRODUCT DETAILS - {product.name}".center(100))
        print("="*100)
        print(f"ID: {product.product_id}")
        print(f"Category: {product.category}")
        print(f"Price: ${product.price:.2f}")
        print(f"Stock Available: {product.stock} units")
        print(f"Description: {product.description}")
        print(f"Average Rating: {product.get_average_rating()}/5 ⭐ ({len(product.reviews)} reviews)")
        print("-"*100)

        # Display reviews by sentiment
        positive_reviews = product.get_reviews_by_sentiment(Sentiment.POSITIVE)
        neutral_reviews = product.get_reviews_by_sentiment(Sentiment.NEUTRAL)
        negative_reviews = product.get_reviews_by_sentiment(Sentiment.NEGATIVE)

        # Positive Reviews
        print(f"\n✅ POSITIVE REVIEWS ({len(positive_reviews)}):")
        print("-" * 100)
        if positive_reviews:
            for review in positive_reviews:
                print(f"  {review}")
        else:
            print("  No positive reviews yet.")

        # Neutral Reviews
        print(f"\n⚪ NEUTRAL REVIEWS ({len(neutral_reviews)}):")
        print("-" * 100)
        if neutral_reviews:
            for review in neutral_reviews:
                print(f"  {review}")
        else:
            print("  No neutral reviews yet.")

        # Negative Reviews
        print(f"\n❌ NEGATIVE REVIEWS ({len(negative_reviews)}):")
        print("-" * 100)
        if negative_reviews:
            for review in negative_reviews:
                print(f"  {review}")
        else:
            print("  No negative reviews yet.")

        print("\n" + "="*100 + "\n")

    def display_review_summary(self, product_id: int):
        """Display a summary of reviews with statistics"""
        product = next((p for p in self.products if p.product_id == product_id), None)

        if not product:
            print(f"❌ Product with ID {product_id} not found!")
            return

        positive = product.get_reviews_by_sentiment(Sentiment.POSITIVE)
        neutral = product.get_reviews_by_sentiment(Sentiment.NEUTRAL)
        negative = product.get_reviews_by_sentiment(Sentiment.NEGATIVE)
        total = len(product.reviews)

        print("\n" + "="*60)
        print(f"REVIEW SUMMARY - {product.name}".center(60))
        print("="*60)
        print(f"Total Reviews: {total}")
        print(f"Average Rating: {product.get_average_rating()}/5 ⭐")
        print("-"*60)
        print(f"✅ Positive: {len(positive)} ({(len(positive)/total*100):.1f}%)")
        print(f"⚪ Neutral: {len(neutral)} ({(len(neutral)/total*100):.1f}%)")
        print(f"❌ Negative: {len(negative)} ({(len(negative)/total*100):.1f}%)")
        print("="*60 + "\n")

    def add_to_cart(self, product_id: int, quantity: int = 1):
        """Add product to cart"""
        product = next((p for p in self.products if p.product_id == product_id), None)

        if not product:
            print(f"❌ Product with ID {product_id} not found!")
            return

        if quantity > product.stock:
            print(f"❌ Only {product.stock} units available!")
            return

        self.cart.append({"product": product, "quantity": quantity})
        print(f"✅ Added {quantity}x {product.name} to cart!")

    def display_cart(self):
        """Display shopping cart"""
        if not self.cart:
            print("\n🛒 Your cart is empty!")
            return

        print("\n" + "="*80)
        print("🛒 SHOPPING CART".center(80))
        print("="*80)
        total = 0
        for idx, item in enumerate(self.cart, 1):
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity
            total += subtotal
            print(f"{idx}. {product.name} x{quantity} = ${subtotal:.2f}")
        print("-"*80)
        print(f"Total: ${total:.2f}".rjust(80))
        print("="*80 + "\n")

    def interactive_menu(self):
        """Interactive menu for browsing products and reviews"""
        while True:
            print("\n" + "="*50)
            print("E-COMMERCE STORE".center(50))
            print("="*50)
            print("1. View All Products")
            print("2. View Product Details & Reviews")
            print("3. View Review Summary")
            print("4. Add to Cart")
            print("5. View Cart")
            print("6. Exit")
            print("="*50)

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.display_all_products()

            elif choice == "2":
                try:
                    product_id = int(input("Enter product ID: "))
                    self.display_product_details(product_id)
                except ValueError:
                    print("❌ Invalid input! Please enter a valid product ID.")

            elif choice == "3":
                try:
                    product_id = int(input("Enter product ID: "))
                    self.display_review_summary(product_id)
                except ValueError:
                    print("❌ Invalid input! Please enter a valid product ID.")

            elif choice == "4":
                try:
                    product_id = int(input("Enter product ID: "))
                    quantity = int(input("Enter quantity: "))
                    self.add_to_cart(product_id, quantity)
                except ValueError:
                    print("❌ Invalid input!")

            elif choice == "5":
                self.display_cart()

            elif choice == "6":
                print("\n👋 Thank you for shopping! Goodbye!")
                break

            else:
                print("❌ Invalid choice! Please try again.")


def main():
    """Main application entry point"""
    app = ECommerceApp()
    
    # Display welcome message
    print("\n" + "="*100)
    print("🛍️ WELCOME TO E-COMMERCE STORE 🛍️".center(100))
    print("="*100)
    print("Browse products, read customer reviews, and manage your shopping cart!".center(100))
    print("="*100 + "\n")

    # Show demo of all products
    app.display_all_products()

    # Show detailed example (Product 1)
    print("\n📌 EXAMPLE: Viewing Product Details with Reviews\n")
    app.display_product_details(1)

    # Start interactive menu
    app.interactive_menu()


if __name__ == "__main__":
    main()

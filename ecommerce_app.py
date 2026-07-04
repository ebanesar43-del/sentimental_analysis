"""
Simple E-Commerce Application with Sentiment Analysis
"""

from dataclasses import dataclass
from typing import List
from enum import Enum


class Sentiment(Enum):
    POSITIVE = "Positive ✅"
    NEGATIVE = "Negative ❌"
    NEUTRAL = "Neutral ⚪"


@dataclass
class Review:
    name: str
    rating: int
    comment: str
    sentiment: Sentiment


@dataclass
class Product:
    id: int
    name: str
    price: float
    reviews: List[Review]

    def avg_rating(self):
        if not self.reviews:
            return 0
        return round(sum(r.rating for r in self.reviews) / len(self.reviews), 1)

    def get_by_sentiment(self, sentiment):
        return [r for r in self.reviews if r.sentiment == sentiment]


# Dummy Products Data
products = [
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


def show_all_products():
    """Display all products"""
    print("\n" + "="*60)
    print("📦 PRODUCTS".center(60))
    print("="*60)
    for p in products:
        print(f"[{p.id}] {p.name:15} | ${p.price:7.2f} | Rating: {p.avg_rating()}/5 ⭐")
    print("="*60 + "\n")


def show_product_reviews(product_id):
    """Show reviews for a product grouped by sentiment"""
    product = next((p for p in products if p.id == product_id), None)
    
    if not product:
        print("❌ Product not found!\n")
        return
    
    print("\n" + "="*70)
    print(f"📄 {product.name.upper()} - Average Rating: {product.avg_rating()}/5 ⭐".center(70))
    print("="*70)
    
    # Positive Reviews
    positive = product.get_by_sentiment(Sentiment.POSITIVE)
    print(f"\n✅ POSITIVE REVIEWS ({len(positive)}):")
    if positive:
        for r in positive:
            print(f"   ⭐ {r.rating}/5 - {r.name}: {r.comment}")
    else:
        print("   No positive reviews")
    
    # Neutral Reviews
    neutral = product.get_by_sentiment(Sentiment.NEUTRAL)
    print(f"\n⚪ NEUTRAL REVIEWS ({len(neutral)}):")
    if neutral:
        for r in neutral:
            print(f"   ⭐ {r.rating}/5 - {r.name}: {r.comment}")
    else:
        print("   No neutral reviews")
    
    # Negative Reviews
    negative = product.get_by_sentiment(Sentiment.NEGATIVE)
    print(f"\n❌ NEGATIVE REVIEWS ({len(negative)}):")
    if negative:
        for r in negative:
            print(f"   ⭐ {r.rating}/5 - {r.name}: {r.comment}")
    else:
        print("   No negative reviews")
    
    print("\n" + "="*70 + "\n")


def show_review_summary(product_id):
    """Show review statistics"""
    product = next((p for p in products if p.id == product_id), None)
    
    if not product:
        print("❌ Product not found!\n")
        return
    
    total = len(product.reviews)
    pos = len(product.get_by_sentiment(Sentiment.POSITIVE))
    neu = len(product.get_by_sentiment(Sentiment.NEUTRAL))
    neg = len(product.get_by_sentiment(Sentiment.NEGATIVE))
    
    print("\n" + "="*50)
    print(f"SUMMARY - {product.name}".center(50))
    print("="*50)
    print(f"Total Reviews: {total}")
    print(f"Average Rating: {product.avg_rating()}/5 ⭐")
    print("-"*50)
    print(f"✅ Positive: {pos} ({pos/total*100:.0f}%)")
    print(f"⚪ Neutral:  {neu} ({neu/total*100:.0f}%)")
    print(f"❌ Negative: {neg} ({neg/total*100:.0f}%)")
    print("="*50 + "\n")


def main():
    """Main menu"""
    print("\n🛍️  WELCOME TO E-COMMERCE STORE 🛍️\n")
    
    while True:
        print("="*40)
        print("MENU".center(40))
        print("="*40)
        print("1. View All Products")
        print("2. View Product Reviews")
        print("3. View Review Summary")
        print("4. Exit")
        print("="*40)
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            show_all_products()
        
        elif choice == "2":
            show_all_products()
            try:
                pid = int(input("Enter Product ID: "))
                show_product_reviews(pid)
            except:
                print("❌ Invalid input!\n")
        
        elif choice == "3":
            show_all_products()
            try:
                pid = int(input("Enter Product ID: "))
                show_review_summary(pid)
            except:
                print("❌ Invalid input!\n")
        
        elif choice == "4":
            print("\n👋 Thank you! Goodbye!\n")
            break
        
        else:
            print("❌ Invalid choice!\n")


if __name__ == "__main__":
    main()

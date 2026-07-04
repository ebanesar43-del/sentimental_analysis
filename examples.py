"""
Usage Examples for E-Commerce Application
"""

from ecommerce_app import Product, Review, Sentiment, show_all_products, show_product_reviews, show_review_summary

# Example 1: Create a custom product with reviews
print("=" * 60)
print("EXAMPLE 1: Creating a Custom Product".center(60))
print("=" * 60)

custom_product = Product(
    id=99,
    name="Custom Device",
    price=599.99,
    reviews=[
        Review("Alice", 5, "Excellent product!", Sentiment.POSITIVE),
        Review("Bob", 4, "Pretty good", Sentiment.POSITIVE),
        Review("Charlie", 3, "Average quality", Sentiment.NEUTRAL),
        Review("David", 2, "Has some issues", Sentiment.NEGATIVE),
        Review("Eve", 1, "Not satisfied", Sentiment.NEGATIVE),
    ]
)

print(f"\nProduct: {custom_product.name}")
print(f"Price: ${custom_product.price}")
print(f"Average Rating: {custom_product.avg_rating()}/5 ⭐")
print(f"\nReview Breakdown:")
print(f"  ✅ Positive: {len(custom_product.get_by_sentiment(Sentiment.POSITIVE))}")
print(f"  ⚪ Neutral: {len(custom_product.get_by_sentiment(Sentiment.NEUTRAL))}")
print(f"  ❌ Negative: {len(custom_product.get_by_sentiment(Sentiment.NEGATIVE))}")

# Example 2: Filter reviews by sentiment
print("\n\n" + "=" * 60)
print("EXAMPLE 2: Filtering Reviews by Sentiment".center(60))
print("=" * 60)

print(f"\n✅ POSITIVE REVIEWS for {custom_product.name}:")
for review in custom_product.get_by_sentiment(Sentiment.POSITIVE):
    print(f"  - {review.name}: {review.comment} ({review.rating}⭐)")

print(f"\n❌ NEGATIVE REVIEWS for {custom_product.name}:")
for review in custom_product.get_by_sentiment(Sentiment.NEGATIVE):
    print(f"  - {review.name}: {review.comment} ({review.rating}⭐)")

# Example 3: Calculate statistics
print("\n\n" + "=" * 60)
print("EXAMPLE 3: Review Statistics".center(60))
print("=" * 60)

total_reviews = len(custom_product.reviews)
positive_count = len(custom_product.get_by_sentiment(Sentiment.POSITIVE))
neutral_count = len(custom_product.get_by_sentiment(Sentiment.NEUTRAL))
negative_count = len(custom_product.get_by_sentiment(Sentiment.NEGATIVE))

print(f"\nTotal Reviews: {total_reviews}")
print(f"Positive: {positive_count} ({positive_count/total_reviews*100:.0f}%)")
print(f"Neutral: {neutral_count} ({neutral_count/total_reviews*100:.0f}%)")
print(f"Negative: {negative_count} ({negative_count/total_reviews*100:.0f}%)")

print("\n" + "=" * 60)
print("Run 'python ecommerce_app.py' to start the interactive application!")
print("=" * 60)

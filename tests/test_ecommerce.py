"""
Tests for E-Commerce Application
"""

import unittest
from ecommerce_app import Product, Review, Sentiment


class TestReview(unittest.TestCase):
    """Test Review class"""
    
    def test_positive_review(self):
        review = Review("John", 5, "Great!", Sentiment.POSITIVE)
        self.assertEqual(review.name, "John")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.sentiment, Sentiment.POSITIVE)
    
    def test_negative_review(self):
        review = Review("Tom", 1, "Bad!", Sentiment.NEGATIVE)
        self.assertEqual(review.rating, 1)
        self.assertEqual(review.sentiment, Sentiment.NEGATIVE)


class TestProduct(unittest.TestCase):
    """Test Product class"""
    
    def setUp(self):
        self.reviews = [
            Review("John", 5, "Great!", Sentiment.POSITIVE),
            Review("Sarah", 5, "Good!", Sentiment.POSITIVE),
            Review("Mike", 3, "Okay", Sentiment.NEUTRAL),
            Review("Tom", 1, "Bad", Sentiment.NEGATIVE),
        ]
        self.product = Product(1, "Laptop", 999.99, self.reviews)
    
    def test_product_creation(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.price, 999.99)
    
    def test_average_rating(self):
        avg = self.product.avg_rating()
        expected = (5 + 5 + 3 + 1) / 4
        self.assertEqual(avg, round(expected, 1))
    
    def test_get_positive_reviews(self):
        positive = self.product.get_by_sentiment(Sentiment.POSITIVE)
        self.assertEqual(len(positive), 2)
    
    def test_get_negative_reviews(self):
        negative = self.product.get_by_sentiment(Sentiment.NEGATIVE)
        self.assertEqual(len(negative), 1)
    
    def test_get_neutral_reviews(self):
        neutral = self.product.get_by_sentiment(Sentiment.NEUTRAL)
        self.assertEqual(len(neutral), 1)


class TestEmptySentiment(unittest.TestCase):
    """Test with no reviews"""
    
    def test_product_without_reviews(self):
        product = Product(6, "Tablet", 499.99, [])
        self.assertEqual(product.avg_rating(), 0)
        self.assertEqual(len(product.get_by_sentiment(Sentiment.POSITIVE)), 0)


if __name__ == "__main__":
    unittest.main()

# E-Commerce Sentiment Analysis Application

A simple Python application that demonstrates an e-commerce store with product reviews categorized by sentiment (Positive, Negative, Neutral).

## 📋 Features

- **5 Products** with detailed information (ID, name, price, reviews)
- **20 Customer Reviews** (4 per product)
- **Sentiment Analysis** - Reviews grouped by:
  - ✅ **Positive** (4-5 stars)
  - ⚪ **Neutral** (3 stars)
  - ❌ **Negative** (1-2 stars)
- **4 Menu Options**:
  1. View All Products
  2. View Product Reviews (grouped by sentiment)
  3. View Review Summary (percentages & statistics)
  4. Exit

## 🛍️ Products Included

1. **Laptop** - $999.99
2. **Headphones** - $149.99
3. **Phone** - $799.99
4. **Keyboard** - $89.99
5. **Monitor** - $349.99

## 📊 Sample Output

### Product Catalog
```
📦 PRODUCTS
============================================================
[1] Laptop         | $ 999.99 | Rating: 3.8/5 ⭐
[2] Headphones     | $ 149.99 | Rating: 3.3/5 ⭐
[3] Phone          | $ 799.99 | Rating: 3.5/5 ⭐
[4] Keyboard       | $  89.99 | Rating: 3.3/5 ⭐
[5] Monitor        | $ 349.99 | Rating: 3.8/5 ⭐
```

### Product Reviews (Grouped by Sentiment)
```
📄 LAPTOP - Average Rating: 3.8/5 ⭐

✅ POSITIVE REVIEWS (2):
   ⭐ 5/5 - John: Great performance!
   ⭐ 5/5 - Sarah: Very fast

⚪ NEUTRAL REVIEWS (1):
   ⭐ 3/5 - Mike: It's okay

❌ NEGATIVE REVIEWS (1):
   ⭐ 2/5 - Tom: Battery issues
```

### Review Summary (Statistics)
```
SUMMARY - Laptop
==================================================
Total Reviews: 4
Average Rating: 3.8/5 ⭐
--------------------------------------------------
✅ Positive: 2 (50%)
⚪ Neutral:  1 (25%)
❌ Negative: 1 (25%)
```

## 🚀 How to Run

### Requirements
- Python 3.7+
- No external dependencies

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ebanesar43-del/sentimental_analysis.git
cd sentimental_analysis
```

2. Run the application:
```bash
python ecommerce_app.py
```

## 📁 Project Structure

```
sentimental_analysis/
├── README.md              # This file
├── ecommerce_app.py       # Main application
├── requirements.txt       # Python dependencies
├── config.py              # Configuration settings
├── examples.py            # Usage examples
├── .gitignore             # Git ignore file
├── data/
│   └── dummy_data.py      # Sample data module
└── tests/
    └── test_ecommerce.py  # Unit tests
```

## 💻 Code Structure

### Main Components

1. **Sentiment Enum** - Defines sentiment types (Positive, Negative, Neutral)
2. **Review Class** - Stores reviewer name, rating, comment, and sentiment
3. **Product Class** - Stores product info and reviews with methods:
   - `avg_rating()` - Calculate average rating
   - `get_by_sentiment()` - Filter reviews by sentiment

4. **Functions**:
   - `show_all_products()` - Display all products
   - `show_product_reviews()` - Show reviews grouped by sentiment
   - `show_review_summary()` - Display review statistics
   - `main()` - Interactive menu loop

## 📝 Example Usage

```python
# View all products
1

# View reviews for a product
2
Enter Product ID: 1

# View sentiment statistics
3
Enter Product ID: 2

# Exit
4
```

## 🎯 Learning Outcomes

This project demonstrates:
- Object-oriented programming in Python
- Data structures (dataclasses, enums)
- Sentiment analysis concepts
- File I/O and data management
- Menu-driven applications
- Data filtering and statistics

## 🔧 Customization

To add more products:

```python
Product(6, "Product Name", 999.99, [
    Review("Name", 5, "Comment", Sentiment.POSITIVE),
    Review("Name", 3, "Comment", Sentiment.NEUTRAL),
    Review("Name", 1, "Comment", Sentiment.NEGATIVE),
])
```

## 📞 Support

For issues or questions, create an issue in the repository.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by ebanesar43-del

## 🔄 Version

**Version 1.0** - Initial Release

---

**Happy Shopping! 🛍️**

"""
Product Review Analyzer
Author: Deepak Sangwan
Date: 24/05/2025
Description: Analyze product reviews for average rating, verified users, helpful votes, and more.
"""
product_reviews = [
    {
        "name": "EcoSpeaker",
        "category": "Electronics",
        "reviews": [
            {"user": "Nina", "rating": 4.5, "verified": True, "helpful_votes": 12, "date": "2024-06-11"},
            {"user": "Ravi", "rating": 3.0, "verified": False, "helpful_votes": 3, "date": "2024-06-13"},
        ]
    },
    {
        "name": "StepTracker Pro",
        "category": "Fitness",
        "reviews": [
            {"user": "Leah", "rating": 4.8, "verified": True, "helpful_votes": 22, "date": "2024-06-15"},
            {"user": "Derek", "rating": 2.5, "verified": True, "helpful_votes": 5, "date": "2024-06-11"},
            {"user": "Eli", "rating": 3.5, "verified": False, "helpful_votes": 0, "date": "2024-06-09"}
        ]
    }
]

#Average rating by product: {"EcoSpeaker": 3.75,"StepTracker Pro": 3.6}
def average_rating_by_product(data):
    result = {}
    for products in data:
        total_rating = 0
        for ratings in products['reviews']:
            total_rating += ratings['rating']
        avg = total_rating/len(products['reviews'])
        result[products['name']] = round(avg, 2)
    return result

#Most helpful reviews: {"EcoSpeaker": ("Alice", 12),"StepTracker Pro": ("Cara", 20)}
def most_helpful_reviews(data):
    result = {}
    for product in data:
        top = max(product['reviews'], key=lambda x: x['helpful_votes'])
        result[product['name']] = (top['user'], top['helpful_votes'])
    return result

#Verified reviwer count per product: {"EcoSpeaker": 1,"StepTracker Pro": 2}
def verified_reviewer_count(data):
    result = {}
    for products in data:
        count = 0
        for reviews in products['reviews']:
            if reviews['verified']:
                count += 1
        result[products['name']] = count
    return result

#verified reviwer percentage per product: {"EcoSpeaker": 50.0, "StepTracker Pro": 66.67}
def verified_reviewer_percent(data):
    result = {}
    for products in data:
        verified = 0
        total = len(products['reviews'])
        for reviews in products['reviews']:
            if reviews['verified']:
                verified +=1
        result[products['name']] = round((verified/total)*100, 2)
    return result

#Top two rating reviews: {"EcoSpeaker": [("Alice", 4.5), ("Bob", 3.0)],"StepTracker Pro": [("Cara", 4.8), ("Eli", 3.5)]}
def top_2_reviews(data):
    result = {}
    for products in data:
        reviews_list = [(reviews['user'], reviews['rating']) for reviews in products['reviews']] #all users and ratings per product list
        top_reviews = sorted(reviews_list, key=lambda x: x[1], reverse=True)[:2] #get only top2 out of all sorted list of each product
        result[products['name']] = top_reviews
    return result

#Most recent verified reviewer: {"EcoSpeaker": ("Alice", "2024-06-10"),"StepTracker Pro": ("Cara", "2024-06-15")}
def most_recent_review(data):
    result = {}
    for products in data:
        reviews_list = [(reviews['user'], reviews['date']) for reviews in products['reviews'] if reviews['verified']]
        if reviews_list:
            result[products['name']] = max(reviews_list, key=lambda x: x[1])
        else:
            result[products['name']] = None
    return result

if __name__ == "__main__":
    print("📊 Average Rating by Product:")
    print(average_rating_by_product(product_reviews))

    print("\n🌟 Most Helpful Reviews:")
    print(most_helpful_reviews(product_reviews))

    print("\n✅ Verified Reviewer Count:")
    print(verified_reviewer_count(product_reviews))

    print("\n📈 Verified Reviewer Percentage:")
    print(verified_reviewer_percent(product_reviews))

    print("\n🏆 Top 2 Rated Reviews:")
    print(top_2_reviews(product_reviews))

    print("\n🕒 Most Recent Verified Review:")
    print(most_recent_review(product_reviews))

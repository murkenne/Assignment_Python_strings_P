'''
1. Product Review Analysis

Task 1: Keyword Highligther

Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 
We want you to capitalize those keywords then print out each review. 
Print out each review with the keywords in uppercase so they stand out.

So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review.  
The function should return the total count of positive and negative words.

Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
Ensure that the summary does not cut off in the middle of a word.

'''

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ['good', 'excellent', 'bad', 'poor', 'average']

for review in reviews:
    for keyword in keywords:
        if keyword in review:
           review = review.replace(keyword, keyword.upper())
    print(review)
   
positive_words = ['good', 'excellent', 'impressed', 'recommended']
negative_words = ['bad', 'poor', 'disappointed', 'wouldn’t']

def tally_sentiments(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    
    for review in reviews:
        for word in positive_words:
            if word in review.lower():
                positive_count += 1
                
        for word in negative_words:
            if word in review.lower():
                negative_count -= 1
                
    return positive_count, negative_count 

positive_count, negative_count = tally_sentiments(reviews, positive_words, negative_words)
print(f"Total Positive Words: {positive_count}")
print(f"Total Negative Words: {negative_count}")

def create_summary(review):
    if len(review) > 30:
        summary = review[:30].rsplit(' ', 1)[0] + "…"
    else:
        summary = review
    return summary

for review in reviews:
    summary = create_summary(review)
    print(f"Review Summary: {summary}")

    

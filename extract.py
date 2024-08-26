import requests
from bs4 import BeautifulSoup

def extract_reviews(product_link):
    # Get the HTML of the product page
    response = requests.get(product_link)
    html = response.content

    # Parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    # Find the elements that contain the reviews
    reviews = soup.find_all("div", class_="review")

    # Extract the text of each review
    review_texts = []
    for review in reviews:
        review_text = review.text
        review_texts.append(review_text)

    return review_texts

# Example usage:

product_link = "https://www.amazon.in/Benyar-Stainless-Party-Wear-Chronograph-Display/dp/B08425N2XQ/?_encoding=UTF8&pd_rd_i=B08425N2XQ&pd_rd_w=fqu0W&content-id=amzn1.sym.cceb7325-7aaa-45f9-a569-b568205c31a7&pf_rd_p=cceb7325-7aaa-45f9-a569-b568205c31a7&pf_rd_r=NPMTH53P43WK7Y60BT13&pd_rd_wg=0rwbQ&pd_rd_r=7cc4b5e4-3b3e-45c0-9e8a-e8b765dd9d75&ref_=deals"

# Extract the reviews for the product
review_texts = extract_reviews(product_link)

# Print the reviews
for review_text in review_texts:
    print(review_text)

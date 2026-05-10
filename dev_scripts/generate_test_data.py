import requests
import random
import time


API_URL = "http://127.0.0.1:5000/add_produs"
MY_CATEGORIES = ["Electronics", "Furniture", "Clothing", "Books", "Toys", "Food", "Office Supplies", "Home Decor"] 
STRUCTURES = ["Manual", "Textbook", "Pro Edition", "Guide", "Kit", "Basic"]
TOTAL_REQUESTS = 50

def send_live_products():
    print(f"📡 Starting live stream of {TOTAL_REQUESTS} products to {API_URL}...")
    
    for i in range(TOTAL_REQUESTS):
        category_subject = random.choice(MY_CATEGORIES)
        structure = random.choice(STRUCTURES)
        name = f"{category_subject} {structure}"
        price = round(random.uniform(10, 500), 2)
        
        payload = {"name": name, "price": price}
        
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 201:
                print(f"[{i+1}] ✅ Sent: {name}")
            else:
                print(f"[{i+1}] ❌ Error {response.status_code}: {response.text}")
        except Exception as e:
            print(f"[{i+1}] ⚠️ Connection failed: {e}")
            break 
        time.sleep(0.2)

if __name__ == "__main__":
    print("hi")
    send_live_products()
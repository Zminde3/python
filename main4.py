import pprint
store = {
    "name": "E-Shop",
    "categories": ["Electronics", "Books", "Clothing"],
    "products": [
        {"name": "Laptop", "price": 1000, "stock": 10},
        {"name": "Book", "price": 20, "stock": 50},
        {"name": "T-shirt", "price": 15, "stock": 100}
    ],
    "rating": 4.5
}
store["categories"].remove("Clothing")
for product in store["products"]:
    if product["price"] > 50:
        product["price"] *= 0.95
for product in store["products"]:
    if product["name"] == "Laptop":
        product["stock"] = 15
if store["rating"] < 4.6:
    store["rating"] += 0.1
pprint.pprint(store)

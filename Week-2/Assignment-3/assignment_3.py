# Complete the function below by Python which can calculate the average price of all the
# products.
def avg(data):
    priceList = [item["price"] for item in data["products"]]
    average = sum(priceList) / len(priceList)
    return round(average, 3)


# print the average price of all products (round to 3 decimal)
print(avg({"products":
           [{"name": "Product 1", "price": 100},
               {"name": "Product 2", "price": 700},
               {"name": "Product 3", "price": 300}]
           }))

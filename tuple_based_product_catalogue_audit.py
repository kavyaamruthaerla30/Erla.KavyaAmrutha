#Case Study 49: Tuple-Based Product Catalogue Audit
def audit_catalogue(products):
    # Each immutable product record is (product_id, name, price, stock)
    ids = [item[0] for item in products]
    duplicate_ids = sorted({item_id for item_id in ids if ids.count(item_id) > 1})
    invalid = [item for item in products if item[2] < 0 or item[3] < 0]
    total_value = sum(price * stock for _, _, price, stock in products if price >= 0 and stock >= 0)
    return duplicate_ids, invalid, total_value

def main():
    products = []
    count = int(input("Number of products: "))
    for index in range(count):
        print(f"Product {index + 1}")
        product_id = input("ID: ").strip()
        name = input("Name: ").strip()
        price = float(input("Unit price: "))
        stock = int(input("Stock quantity: "))
        products.append((product_id, name, price, stock))
    duplicates, invalid, value = audit_catalogue(products)
    print("\nCatalogue records (tuples):")
    for product in products:
        print(product)
    print("Duplicate product IDs:", duplicates if duplicates else "None")
    print("Invalid records:", invalid if invalid else "None")
    print(f"Total valid inventory value: Rs. {value:.2f}")

if __name__ == "__main__":
    main()

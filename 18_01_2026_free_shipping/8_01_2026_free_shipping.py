def gets_free_shipping(cart, minimum):
    prices = {
        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95
    }

    total = sum(prices[item] for item in cart)
    
    return total >= minimum


if __name__ == "__main__":
    print(gets_free_shipping(["shoes"], 50)) # should return True.
    print(gets_free_shipping(["hat", "socks"], 50)) # should return False.
    print(gets_free_shipping(["jeans", "shirt", "jacket"], 75)) # should return True.
    print(gets_free_shipping(["socks", "socks", "hat"], 75)) # should return False.
    print(gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100)) # should return True.
    print(gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200)) # should return False
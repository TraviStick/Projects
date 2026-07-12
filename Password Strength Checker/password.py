import math, string

def calculate_entropy(password):
    if not password:
        return 0

    # Determine character pool size
    pool_size = 0
    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += 32

    # If the password has custom/other characters
    unique_chars = len(set(password))
    if unique_chars > pool_size:
        pool_size = unique_chars

    # Calculate entropy
    entropy = len(password) * math.log2(pool_size)
    return entropy

pwd = "1aA,a"
print(f"Entropy: {calculate_entropy(pwd):.2f} bits")
print('idk wats next')

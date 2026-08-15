import math, string, hashlib, requests

def password_strength_checker(password):
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

def password_security_checker(password):
    result = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = result[:5]
    suffix = result[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if  response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")

    for line in response.text.splitlines():
        target_suffix, count = line.split(":")
        if target_suffix == suffix:
            return int(count)
    return 0

password = input("Enter password: ")
print(f"Entropy: {password_strength_checker(password):.2f} bits")
print(f"The password appeared \"{password_security_checker(password)}\" times")


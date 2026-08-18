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
    if " " in password:
        pool_size += 1

    

    # Calculate entropy
    entropy = len(password) * math.log2(pool_size)
    return entropy

def password_security_checker(password):
    result = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = result[:5]
    suffix = result[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        # Adding a timeout to keep from hanging indefinitely 
        response = requests.get(url,timeout=5)
        # Raises HTTPError if the response status code is 4xx or 5xx
        response.raise_for_status()
        # Process valid response data
        data = response.json()
        print("Success:", data)

    except requests.exceptions.RequestException as e:
        # Catches ConnectionError, Timeout, HTTPError, etc.
        print(f"An error occurred while handling your request: {e}")



    if  response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")

    for line in response.text.splitlines():
        target_suffix, count = line.split(":")
        if target_suffix == suffix:
            return int(count)
    return 0

password = input("Enter password: ")
entropy = password_strength_checker(password)
if __name__ == "__main__":
    password = input("Enter password: ")
    entropy = password_strength_checker(password)
leaks = password_security_checker(password)

print(f"Entropy: {entropy:.2f} bits")
# I got this password strength from NordVPN
if entropy < 35:
    print("Strength: Very Weak")
elif 36 < entropy < 59:
    print("Strength: Weak")
elif 60 < entropy < 119:
    print("Strength: Strong")
elif 120 < entropy:
    print("Strength: Very Strong")

print(f"Pwned Status: Found in {leaks:,} data breaches.")


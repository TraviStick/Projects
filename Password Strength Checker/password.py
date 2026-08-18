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

    # Fallback if password uses spaces or characters outside the standard pools
    unique_chars = len(set(password))
    if unique_chars > pool_size or pool_size == 0:
        pool_size = max(unique_chars, 1)  # Ensures pool_size is never 0

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


import math, string, hashlib, requests, sys
def validatePassword(password):
    

    # (This ensures database strings remain safe while allowing é, symbols, and emojis)
    for char in password:
        # 'Cc' means Control character (like backspace, null bytes, escape keys)
        # 'Cf' means Format character (invisible directional/hidden marks)
        import unicodedata
        char_type = unicodedata.category(char)
        
        if char_type in ('Cc', 'Cf'):
            raise ValueError("Password contains invalid system control characters.")

    return True



def password_strength_checker(password):
    if not password:
        return 0
    # Determine character pool size
    pool_size = 0
    if " " in password:
            pool_size += 1
    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += 32
    if any(ord(c) >= 128 for c in password):
        pool_size += 128
    else:
        pool_size += 0

    # Calculate entropy 
    if pool_size <= 0:
        raise ValueError ("Entropy is Undefined.")
    else:
        entropy = len(password) * math.log2(pool_size)
    return entropy

def password_security_checker(password):
    try:
        result = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = result[:5]
        suffix = result[5:]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
 
        # Adding a timeout to keep from hanging indefinitely 
        response = requests.get(url,timeout=5)
        # Raises HTTPError if the response status code is 4xx or 5xx
        response.raise_for_status()

        for line in response.text.splitlines():
            target_suffix, count = line.split(":")
            if target_suffix == suffix:
                return int(count)
    except requests.exceptions.RequestException  as e:
        # Catches ConnectionError, Timeout, HTTPError, etc.
        print(f"An error occurred while handling your request: {e}")
    return 0

if __name__ == "__main__":
    password = input("Enter password: ")
    try:
        validatePassword(password)
        entropy = password_strength_checker(password)
    except ValueError as e:
        print(e)
        sys.exit()
    leaks = password_security_checker(password)
    print(f"Entropy: {entropy:.2f} bits")
    # I got this password strength from NordVPN
    roundedEntropy = round(entropy)
    if roundedEntropy <= 35:
        print("Strength: Very Weak")
    elif 36 <= roundedEntropy <= 59:
        print("Strength: Weak")
    elif 60 <= roundedEntropy <= 119:
        print("Strength: Strong")
    elif 120 <= roundedEntropy:
        print("Strength: Very Strong")
    print(f"Pwned Status: Found in {leaks:,} data breaches.")
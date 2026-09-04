entropy = 120
if entropy <= 35:
    print("Strength: Very Weak")
elif 36 <= entropy <= 59:
    print("Strength: Weak")
elif 60 <= entropy <= 119:
    print("Strength: Strong")
elif 120 <= entropy:
    print("Strength: Very Strong")
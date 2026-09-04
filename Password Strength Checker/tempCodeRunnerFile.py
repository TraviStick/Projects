entropy = 35.4
if entropy <= 35.4:
    print("Strength: Very Weak")
elif 35.5 <= entropy <= 59.4:
    print("Strength: Weak")
elif 59.5 <= entropy <= 120.4:
    print("Strength: Strong")
elif 120.5 <= entropy:
    print("Strength: Very Strong")
password = "😀"
pool_size = 0
if any(ord(c) >= 128 for c in password):
    pool_size += 128
else:
    pool_size += 0
print(pool_size)
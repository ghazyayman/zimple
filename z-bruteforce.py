import hashlib

password_hash = "5f4dcc3b5aa765d61d8327deb882cf99"

for i in range(10000):
    input_str = str(i).zfill(4)
    input_bytes = input_str.encode()
    input_hash = hashlib.md5(input_bytes).hexdigest()

    if input_hash == password_hash:
        print("Password found:", input_str)
        break

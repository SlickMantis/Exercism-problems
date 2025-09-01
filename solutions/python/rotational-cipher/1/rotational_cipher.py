def rotate(text, key):
    ciphertext = []

    for char in text:
        if char.isalpha():  # only shift letters
            if char.islower():
                # shift within 'a' to 'z'
                shifted = (ord(char) - ord('a') + key) % 26 + ord('a')
                ciphertext.append(chr(shifted))
            elif char.isupper():
                # shift within 'A' to 'Z'
                shifted = (ord(char) - ord('A') + key) % 26 + ord('A')
                ciphertext.append(chr(shifted))
        else:
            # keep spaces, punctuation, numbers, etc.
            ciphertext.append(char)

    return "".join(ciphertext)



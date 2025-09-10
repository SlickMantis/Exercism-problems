def abbreviate(words):
    # Replace hyphens with spaces
    cleaned = words.replace("-"," ")
    # Remove punctuation (Anything not a letter or space)
    result = ""
    for char in cleaned:
        if char.isalpha() or char.isspace():
            result = result + char
    # Split into words
    word_list = result.split()
    # Build acronym
    acronym = "".join(word[0].upper() for word in word_list)

    return acronym
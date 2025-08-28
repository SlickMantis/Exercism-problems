def is_isogram(string):
    string = string.lower()
    cleaned = [char for char in string if char.isalpha()]
    return len(cleaned) == len(set(cleaned))
    

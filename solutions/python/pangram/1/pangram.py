def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    in_sentence = []
    for letter in alphabet:
        if letter in sentence:
            in_sentence.append(letter)
    return len(in_sentence) == 26


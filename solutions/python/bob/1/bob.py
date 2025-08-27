def response(hey_bob):
    phrase = hey_bob.strip()

    # Rule 1: Silence
    if phrase == "":
        return "Fine. Be that way!"

    # Rule 2: Yelling a question
    if phrase.isupper() and phrase.endswith("?"):
        return "Calm down, I know what I'm doing!"

    # Rule 3: Yelling
    if phrase.isupper():
        return "Whoa, chill out!"

    # Rule 4: Question
    if phrase.endswith("?"):
        return "Sure."

    # Rule 5: Anything else
    else:
        return "Whatever."

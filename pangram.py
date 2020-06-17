def is_pangram(sentence):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    for char in abecedario:
        if char not in sentence.lower():
            return False
    return True


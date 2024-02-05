alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(message, shift):
    if shift < 1 or shift > 25:
        return "Invalid shift"

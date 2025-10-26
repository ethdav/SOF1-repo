ALPHA = "abcdefghijklmnopqrstuvwxyz"

def encrypt(message, shifts, alphabet=ALPHA):
    """Encrypts a message of length k using a shift key also of length k,
    with each index of the shift key representing the shift applied to
    the letter of the original message at the same index.

    Args:
        message (str): plaintext message
        shifts (list): list of integers
        alphabet (str): any string of symbols, not necessarily the
        English alphabet

    Returns:
        An encrypted message
    """
    if len(message) != len(shifts):
        return None
    
    encrypted = ""
    for index in range(len(message)):
        if shifts[index] < 0 or shifts[index] >= len(alphabet) or message[index] not in alphabet:
            return None
        # The new letter index is found by adding the shift to the index of the old letter
        encrypted += alphabet[(alphabet.index(message[index])+shifts[index])%len(alphabet)]
    return encrypted
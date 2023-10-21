'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter="A", shift=0):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    while shift>=26:
        shift -=26
    if (65<=ord(letter)<=90):
        shifted_letter_ini = int(ord(letter)) + shift
        if shifted_letter_ini>90:
            shifted_letter_fin = ord("A") + (shifted_letter_ini - ord("Z") - 1)
        else:
            shifted_letter_fin = shifted_letter_ini
    elif (97<=ord(letter)<=122):
        shifted_letter_ini = int(ord(letter)) + shift
        if shifted_letter_ini>122:
            shifted_letter_fin = ord("a") + (shifted_letter_ini - ord("z") - 1)
        else:
            shifted_letter_fin = shifted_letter_ini
    else:
        print("The character \"" + letter + "\" remains unchanged because it is not a letter")
        return
    print("Original letter: " + letter + "\nShifted letter: " + chr(shifted_letter_fin))

def caesar_cipher(message="I like pancakes",shift=3):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
            if is_upper:
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    print("Original text: " + text + "\nEncrypted text: " + result)

def shift_by_letter(letter="A",letter_shift="A"):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter_shift.isalpha():
        if letter_shift.isupper():
            shift = ord(letter_shift) - ord("A")
        else:
            shift = ord(letter_shift) - ord("a")
    else:
        return "Invalid character"
    if letter.isalpha():
        if letter.isupper():
            result = chr(((ord(letter) - ord("A") + shift) % 26) + ord("A"))
        else:
            result = chr(((ord(letter) - ord("a") + shift) % 26) + ord("a"))
    else:
        print("Original letter: " + letter + "\nResult: " + letter)
        return
    print("Original letter: " + letter + "\nResult: " + result)

def vigenere_cipher(message="I am an ITMGT Student", key="ITE"):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message = message.upper()
    key = key.upper()
    if not key.isalpha():
        return "Invalid. Please do NOT use any spaces or unique characters in your key"
    encrypted_message = ""
    #Split up the message to the length of the key
    split_message = [message[i:i + len(key)] for i in range (0, len(message), len(key))]
    #Translate each letter from each split using the key
    for each_split in split_message:
        i = 0
        for letter in each_split:
            if letter.isalpha():
                shifted_letter = ((((ord(letter) - ord("A")) + (ord(key[i]) - ord("A"))) % 26) + ord("A"))
                encrypted_message += chr(shifted_letter)
            else:
                encrypted_message += letter
            i += 1
    print("Original message: " + message + "\nEncrypted message: " + encrypted_message)

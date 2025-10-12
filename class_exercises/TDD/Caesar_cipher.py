#subprograms -------------------
def to_shift(message,shift):
    #message = message.lower()
    codedMessage = ""
    for letter in message:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            number = ord(letter) + shift%26
            if number > ord("z"):
                number = number - 26
            character = chr(number)
            codedMessage += character

        elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            number = ord(letter) + shift%26
            if number > ord("Z"):
                number = number - 26
            character = chr(number)
            codedMessage += character
        else:
            codedMessage += letter
    return codedMessage

# main program ----------------
'''
user_message = str(input("Enter the message: "))
user_shift = int(input("Enter the shift amount: "))
coded_message = to_shift(user_message,user_shift)
print(f"The message is now: {coded_message}")
'''
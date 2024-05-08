def caesar_cipher(text, shift):
    encrypted_text = ""
    decrypted_text = ""

    for char in text:

        if char.isalpha() and char.islower():
            shifted_char = chr((ord(char) - ord("а") + shift) % 32 + ord("а"))
            encrypted_text += shifted_char

            decrypted_shifted_char = chr(
                (ord(shifted_char) - ord("а") - shift) % 32 + ord("а")
            )
            decrypted_text += decrypted_shifted_char

        elif char.isalpha() and char.isupper():
            shifted_char = chr((ord(char) - ord("А") + shift) % 32 + ord("А"))
            encrypted_text += shifted_char

            decrypted_shifted_char = chr(
                (ord(shifted_char) - ord("А") - shift) % 32 + ord("А")
            )
            decrypted_text += decrypted_shifted_char
        else:

            encrypted_text += char
            decrypted_text += char

    return encrypted_text, decrypted_text


while True:
    shift_input = input("Введите смещение: ")
    if shift_input.isdigit():
        shift = int(shift_input)
        break
    else:
        print("Неверный ввод. Введите целое число.")


message = input("Введите сообщение: ")


encrypted_message, decrypted_message = caesar_cipher(message, shift)


print("Шифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)

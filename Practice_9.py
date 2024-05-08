import crc8


def encode_message(message):
    encoded_message = ""
    for char in message:
        crc = crc8.crc8()
        crc.update(char.encode())
        encoded_crc = bin(crc.digest())[2:].zfill(8)
        encoded_message += char + " " + encoded_crc + " "
    return encoded_message


def decode_message(encoded_message):
    decoded_message = ""
    for char_and_crc in encoded_message.split():
        char, crc = char_and_crc[:1], char_and_crc[1:]
        crc_calculated = crc8.crc8()
        crc_calculated.update(char.encode())
        if bin(crc_calculated.digest())[2:].zfill(8) != crc:
            print(
                f"Ошибка в символе {char} с индексом {encoded_message.index(char_and_crc)}"
            )
        decoded_message += char
    return decoded_message


def main():
    operation_type = input("Введите тип (1 — кодер и декодер, 2 — декодер): ")
    if operation_type == "1":
        message = input("Введите сообщение: ")
        encoded_message = encode_message(message)
        print("Кодированное сообщение:", encoded_message)
        decoded_message = decode_message(encoded_message)
        print("Декодированное сообщение:", decoded_message)
    elif operation_type == "2":
        encoded_message = input("Введите кодированное сообщение: ")
        decoded_message = decode_message(encoded_message)
        print("Декодированное сообщение:", decoded_message)
    else:
        print("Неправильный ввод.")


if __name__ == "__main__":
    main()

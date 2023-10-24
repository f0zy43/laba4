def encrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as file:
        plaintext = file.read()

    encrypted_text = ''
    for char in plaintext:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - start + key) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    with open(output_file, 'w') as file:
        file.write(encrypted_text)


def decrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()

    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - start - key) % 26 + start)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    with open(output_file, 'w') as file:
        file.write(decrypted_text)

input_file = 'C:/Users/HP/Desktop/2 курс/информатика/4 лаба/input.txt' # название исходного файла можно без пути
encrypted_file = 'encrypted.txt' # сохраняется не в папке
decrypted_file = 'decrypted.txt' # сохраняется не в папке
key = 2

# зашифрованный файл
encrypt_file(input_file, encrypted_file, key)

# расшифрованный файл
decrypt_file(encrypted_file, decrypted_file, key)
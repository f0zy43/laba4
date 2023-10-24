key = 2
s = 'Oquv uvctu ctg qdugtxgf vq dg ogodgtu qh dkpctb uvct ubuvgou'

def encrypt(text, key):
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Проверьте, является ли символ буквой
            shift = 65 if char.isupper() else 97  # Установите смещение ASCII для прописных или строчных букв
            encrypted_char = chr((ord(char) - shift + key) % 25 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Если символ не является буквой, оставьте его без изменений

    return encrypted_text

def decrypt(text, key):
    decrypted_text = encrypt(text, -key)
    return decrypted_text

decrypted_s = decrypt(s, key)

print("Исходный текст:")
print(s)
print("Расшифрованный текст:")
print(decrypted_s)

"""функция encrypt принимает текст и ключ в качестве входных данных и возвращает зашифрованный текст. 
Функция сохраняет неалфавитные символы и сохраняет регистр букв во входном тексте.
Чтобы расшифровать зашифрованное сообщение, мы создаем аналогичную функцию, но используем отрицательный ключ для сдвига символов 
в противоположном направлении."""
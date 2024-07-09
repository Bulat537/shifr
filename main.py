def text_to_binary(text):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    return binary_text

def binary_to_text(binary_text):
    text = ''.join(chr(int(char, 2)) for char in binary_text.split())
    return text

choice = input("Выберите операцию: (1) Текст в двоичный код или (2) Двоичный код в текст: ")

if choice == '1':
    text = input("Введите текст для преобразования в двоичный код: ")
    binary_text = text_to_binary(text)
    print("Результат преобразования в двоичный код:", binary_text)
elif choice == '2':
    binary_text = input("Введите двоичный код для преобразования в текст: ")
    text = binary_to_text(binary_text)
    print("Результат преобразования в текст:", text)
else:
    print("Неверный выбор операции. Попробуйте снова.")
input('Успешно')
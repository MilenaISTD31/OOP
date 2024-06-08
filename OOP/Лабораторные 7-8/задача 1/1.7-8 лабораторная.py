import os

class Example:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w'):
                pass
        self.words = self.get_words()

    def get_words(self):
        with open(self.file_path, 'r') as file:
            words = file.read().split()
        return words

    def delete_word(self, word):
        if word in self.words:
            self.words.remove(word)

    def update_source(self):
        with open(self.file_path, 'w') as file:
            for word in self.words:
                file.write(word + " ")

# Проверка:
# 1. Пример использования класса
example = Example("example.txt")
print(f'Слова в файле: {example.words}')

# 2. Удаляем слово (можно написать любое, я брала до этого 'ООП')
example.delete_word('ООП')
print(f'Слова в файле после удаления: {example.words}')

# 3. Обновляем файл
example.update_source()
print('Файл обновлен', example.words)
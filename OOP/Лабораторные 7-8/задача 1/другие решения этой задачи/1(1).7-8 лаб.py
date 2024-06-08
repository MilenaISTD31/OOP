import json, csv, os

path_file = 'example.txt'

class Files:
    def __init__(self, path) -> None:
        self.words = []
        self.path = path
        self.create_file()

    def create_file(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w', encoding='utf-8') as file:
                pass
        else:
            with open(self.path, 'r', encoding='utf-8') as file:
                text = file.read()
                self.words = text.split()

    def delete_word(self, word):
        self.words = [words for words in self.words if words != word]

    def update_file(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(' '.join(self.words))
    def __str__(self) -> str:
        return f'{self.path}, {self.words}'

files = Files(path_file)
files.delete_word('OOP,')
files.update_file()
print(files)


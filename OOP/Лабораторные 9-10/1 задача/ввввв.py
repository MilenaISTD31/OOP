import json

class TemplateFiller:
    def __init__(self):
        self.data = {}
        self.template = "Приветствую тебя, {{ user_name }}! Очень рад тебя видеть! С нашей последней встречи прошло {{ time }} лет... Прими этот {{ item }} и садись {{ place }}"

    def load_data(self):
        try:
            with open('answers.json', 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data["user_name"] = input("Введите ваше имя: ")
            self.data["time"] = input("Введите количество лет с последней встречи: ")
            self.data["item"] = input("Введите предмет, который вы получили: ")
            self.data["place"] = input("Введите место, где вы должны сесть: ")

            with open('answers.json', 'w') as file:
                json.dump(self.data, file)

    def fill_template(self):
        filled_template = self.template.format(user_name=self.data["user_name"], time=self.data["time"], item=self.data["item"], place=self.data["place"])
        return filled_template

    def run(self):
        self.load_data()
        filled_template = self.fill_template()
        print(filled_template)

if __name__ == "__main__":
    template_filler = TemplateFiller()
    template_filler.run()
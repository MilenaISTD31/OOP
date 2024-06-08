class Human:
    def __init__(self, surname, name, patronymic, age = 0, sex = 'M'):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.sex = sex
    
    def get_fio(self):
        return f"{self.surname} {self.name[0]}. {self.patronymic[0]}."

    def get_full_info(self):
        return (
            f"Фамилия: {self.surname}\n"
            f"Имя: {self.name}\n"
            f"Отчество: {self.patronymic}\n"
            f"Пол: {self.sex}\n"
            f"Возраст: {self.age}"
        )

class Student(Human):
    def __init__(self, surname, name, patronymic, group, age = 0, sex = 'M'):
        super().__init__(surname, name, patronymic, age, sex)
        self.group = group

    def get_full_info(self):
        idk = super().get_full_info() + f"\nГруппа: {self.group}"
        return idk
    
student_205026 = Human('Alekseeva', 'Milena', 'Yakovlevna', 21, 'Female')
print(student_205026.get_fio())
print(student_205026.get_full_info())

student_Milena = Student('Alekseeva', 'Milena', 'Yakovlevna', 'ISTD-31', 21, 'Female')
print(student_Milena.get_fio())
print(student_Milena.get_full_info())
print(student_Milena.a)
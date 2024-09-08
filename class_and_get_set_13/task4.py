class Mainclass:
    def __init__(self, text: str):
        self.text = text

    def set_text(self, text: str = ""):
        self.text = text
    
class Subclass(Mainclass):
    def __init__(self, text: str, number: int):
        super().__init__(text)
        self.number = number

#выведит просто текст из главного класса
main_exp = Mainclass("Выввод текста")
print(main_exp.text)
#Обновит текст и вывыедит из главного класаа
main_exp.set_text("Обновить текст")
print(main_exp.text)
#нечегоне выведит потомучто б=мы не указали новый текст
main_exp.set_text()
print(main_exp.text)

#визуальный пробел
print(27 * "-")
#Сначало выведит текст из главного класса а потом из дочернего цифру
sub_exp = Subclass("Ввывод текста", 52)
print(sub_exp.text)
print(sub_exp.number)
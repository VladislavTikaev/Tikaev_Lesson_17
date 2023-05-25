# Описать два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение количества гласных и согласных букв меньше или равно длине слова, то выводить все гласные, иначе согласные;
# если передаю число, то вывести произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.
#Итого - один класс, в нем только ДВА МЕТОДА

class STROKACHISLO:
    def function_1(self, arg):
        if isinstance(arg, str):
            if sum(i in "аёеуяюэиоы" for i in arg.lower()) * sum(i in "бвгджзйклмнпрстфхцчшщ" for i in arg.lower()) <= len(arg):
                return ''.join([i for i in arg if i.lower() in "ауоыиэюяеё"])
            else:
                return ''.join([i for i in arg if i.lower() in "бвгджзйклмнпрстфхцчшщ"])
        elif isinstance(arg, int):
            return sum(int(i) for i in str(arg) if i in "2468") * self.function_2(arg)
    def function_2(self, arg):
        return len(str(arg))
obj= STROKACHISLO()
primer_1 = obj.function_1("Шла Саша по шоссе и сосала сушку")
primer_2 = obj.function_1("Клала Клава лук на полку, Кликнула к себе Николку")
primer_3 = obj.function_1(123456789)
print(primer_1)
print(primer_2)
print(primer_3)

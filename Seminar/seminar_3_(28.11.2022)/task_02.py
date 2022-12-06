# 2. Напишите программу, которая определит позицию второго вхождения строки в 
# списке либо сообщит, что её нет.
# Пример:

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

input_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
input_value = "йцу"

def get_string(string_list, string_value):
    count = 0
    for char in string_list:
        if string_value in char:
            count += 1
            if count == 2:
                return string_list.index(char)
    else:
        return "Второго вхождения нет"
            
print(f'список: {input_list}, ищем: "{input_value}", ответ: {get_string(input_list,input_value)}')
# Импортируем библиотеку
from tkinter import *
from tkinter import font

root = Tk()
# Создаем окно
root.geometry("600x600")
# Создаем заголвок
root.title(" Q&A ")
# Данные по топливу
fuel = {1: 4541,  # o2h2
        2: 3795,  # o2c2h8n2
        3: 3599,  # o2ch4
        4: 3403}  # ch3nnh2
# Данные по космодромам
spaceport = {
    1: 212,  # plesetsk
    2: 317,  # baykonyr
    3: 409,  # kanaveral
    4: 463}  # kyry


# Вызывается оишбка можно было и валидацию сделать
def error():
    error_message = Label(text="Ошибка неверные данные")
    error_message.pack()
    return error_message


# Стиль для надписи
font2 = font.Font(family="Verdana", size=15, weight="bold", slant="roman")


def space_or_fail():
    name = str(entry1.get())
    num1 = int(entry2.get())
    fill = int(entry3.get())
    port = int(entry4.get())
    num4 = int(entry5.get())

    space = spaceport[port]
    get_fuel = fuel[fill]

    m1 = num1 + num4 # 1 и 4 пункт

    # Блок проверок
    if m1 < 10000:
        return error()
    if m1 >= 1000000:
        s = 16
    if 100000 >= m1 >= 818000:
        s = 14
    if 818000 >= m1 >= 616000:
        s = 12
    if 616000 >= m1 >= 414000:
        s = 10
    if 414000 >= m1 >= 212000:
        s = 8
    if 212000 >= m1 >= 10000:
        s = 6

    sym = get_fuel * 2.72 * ((m1 + s) / m1) + space
    # Проверка на то взлетит ли ракета или нет
    if 16000 >= int(sym) >= 11200:
        label.config(height=20,
                     width=200, text=f"Полет возможен!", font=font2)
    else:
        label.config(height=20,
                     width=200, text=f"Ракета взорвалась", font=font2)
    print(sym)


name = Label(text="Ваше имя")
label1 = Label(text="Введите полезную нагрузку не меньше 10000 кг ")
entry1 = Entry(root)
label2 = Label(text="Выберите топливо \n 1. o2h2 \n 2. o2c2h8n2 \n 3. o2ch4 \n 4. ch3nnh2")

entry2 = Entry(root)
label3 = Label(text="Выберите космодром \n 1. plesetsk \n 2. baykonyr \n 3. kanaveral \n 4. kyry")
entry3 = Entry(root)

entry4 = Entry(root)
label4 = Label(text="Введите массу кострукции")
entry5 = Entry(root)

space_or_fail = Button(root, text="Sum", command=space_or_fail)

# Создание метку для отображения результата
label = Label(root)

# Добавьте виджеты в окно
name.pack()
entry1.pack()
label1.pack()
entry2.pack()
label2.pack()
entry3.pack()
label3.pack()
entry4.pack()
label4.pack()
entry5.pack()
space_or_fail.pack()
label.pack()

root.mainloop()

col ={}
d = 1      
with open('phones.txt', 'r', encoding = 'utf-8') as file:
    for l in file:
        l = l.replace('\n', '')
        col[d] = list(l.split(';'))
        d = d + 1

phone_book = col

def findNumber(dict):
    req = str(input("Введите запрос с заглавной буквы: "))
    for i in dict:
        if req in dict[i]:
            print(dict[i])
                
def getBook(dict):
    for i in dict:
        print(dict[i])

def add(dict):
    n = input("\nВведите фамилию, имя и номер телефона через пробел: ").split()
    dict[len(dict)+1] = n
    print(dict)
           
def edit(dict):
    req = str(input("Введите с заглавной буквы фамилию или имя контакта, который нужно отредактировать: "))
    new_dict = {}
    for i in dict:
        if req in dict[i]:
            new_dict[i] = dict[i]
    
    if len(new_dict) < 1:
        print("\nТакого контакта нет!")
    else:
        print("\n", new_dict)
        if len(new_dict) == 1:
            new_cont1 = str(input("\nВведите с заглавной буквы новые фамилию, имя и номер контакта: ")).split()
            dict[i] = new_cont1
            print("\nКонтакт изменен!")
        if len(new_dict) > 1:
            cont = int(input("\nКонтактов с такими данными несколько. Введите уточняющий номер контакта для продолжения редактирования: "))
            print("\n", dict[cont])
            new_cont = str(input("\nВведите с заглавной буквы новые фамилию, имя и номер контакта: ")).split()
            dict[cont] = new_cont
            print("\nКонтакт изменен!")
    
def delete(dict):
    req = str(input("Введите с заглавной буквы фамилию или имя контакта, который нужно удалить: "))
    new_dict = {}
    for i in list(dict):
        if req in dict[i]:
            new_dict[i] = dict[i]
    
    if len(new_dict) < 1:
        print("\nТакого контакта нет!")
    else:
        print("\n", new_dict)
        if len(new_dict) == 1:
            answer = input("\nУдалить данный контакт? Введите да или нет: ")
            if answer == "да":
                del dict[i]
                print("\nКонтакт удален!")
            if answer == "нет":
                print("\nУдаление отменено!")
        
        if len(new_dict) > 1:
            cont = int(input("\nКонтактов с такими данными несколько. Введите уточняющий номер контакта для продолжения редактирования: "))
            print("\n", dict[cont])
            sure = input("\nУдалить данный контакт? Введите да или нет: ")
            if sure == "да":
                del dict[cont]
                print("\nКонтакт удален!")
            if sure == "нет":
                print("\nУдаление отменено!")

def choice(n):
    if n == "1":
        getBook(phone_book)
    if n == "2":
        findNumber(phone_book)
    if n == "3":
        add(phone_book)
    if n == "4":
        edit(phone_book)
    if n == "5":
        delete(phone_book)

print("\nНажмите клавишу 1-3 для выбора пункта меню:")
print("\n1 - Вывод телефонной книги")
print("2 - Поиск номера по имени/фамилии")
print("3 - Добавление записи")
print("4 - изменить контакт")
print("5 - удалить контакт")

choice(input())

with open('phones.txt', 'w', encoding = 'utf-8') as file:
    for k in phone_book:
        file.write(f'{phone_book[k][0]};{phone_book[k][1]};{phone_book[k][2]}\n')

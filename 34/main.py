poem = "парам-пам-пум турум-пам-пам пибим-паб-ням"

# poem = input("Введите стих:")                          по условию ввод с клавиатуры

def rhyme(poem):
    phrase = poem.split(" ")
    vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    list = []
    for i in phrase:
        k = 0
        for item in i:
            if item in vowels:
                k = k + 1
        list.append(k)
    if len(set(list)) == 1:
        return "Парам пам-пам"
    else: return "Пам парам"

print(rhyme(poem))
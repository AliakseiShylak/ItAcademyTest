def get_word(number):
    word = 'слов'
    if number % 10 == 1 and number % 100 != 11:
        word += 'о:'
    elif 2 <= number % 10 <= 4 and not 12 <= number % 100 <= 14:
        word += 'а:'
    else:
        word +=': '
    return word

search_queries = ["watch new movies", "coffee near me", "how to find the determinant", "python",
                  "data science jobs in UK", "courses for data science", "taxi", "google", "yandex",
                  "bing","foreign exchange rates USD/BYN", "Netflix movies watch online free",
                  "Statistics courses online from top universities"]
quantity_list = list(map(lambda x: len(x.split()), search_queries))
length = len(quantity_list)

quantity_dict = {}
for el in quantity_list:
    quantity_dict[el] = quantity_dict.get(el, 0) + 1

for key in sorted(quantity_dict):
    print(f'{key:2} {get_word(key)} {int(round(quantity_dict[key] / length * 100, 0))}%')
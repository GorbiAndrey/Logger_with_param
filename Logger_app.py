from datetime import datetime
from inspect import signature
import os

def param_logger(path):
    logs_file_name = os.path.join(path, 'out.txt')

    def logger(function):
        def log_function(*args, **kwargs):
            now = datetime.now()
            function_name = function.__name__

            sig = signature(function)
            param = sig.bind(*args, **kwargs)
            args = param.args
            kwargs = param.kwargs

            function_return = function(*args, **kwargs)

            f = open(logs_file_name, 'w', encoding='utf-8')
            f.write(str(now) + '\t' + str(function_name) + '\t' + 
                    str(args) + str(kwargs) + '\t' + 
                    str(function_return) + '\t' + '\n')
            f.close()
            return
        return log_function

    return logger


with open('recipes.txt') as f:
    ingredients = []
    cook_book = {}
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        number_of_entries = f.readline()
        ingredients = []
        for ingredient in range(int(number_of_entries)):
            ingredients_dict = {}
            ingredient = f.readline().strip().split('|')
            ingredient_name, quantity, measure = ingredient
            ingredients_dict['ingredient_name'] = ingredient_name
            ingredients_dict['quantity'] = quantity
            ingredients_dict['measure'] = measure
            ingredients.append(ingredients_dict)
        cook_book[dish_name] = ingredients
        f.readline()

@param_logger('')
def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    result_dict = {}
    for dish in dishes:
        for (key, value) in cook_book.items():
            if dish == key:
                for entry in value:
                    a = (entry['ingredient_name']).strip()
                    b = (entry['measure']).strip()
                    c = int((entry['quantity']).strip())
                    if a in result_dict.keys():
                        result_dict[a]['quantity'] = c * person_count + (result_dict[a]['quantity'])
                    else:
                        result_dict[a] = {'measure': b, 'quantity': c * person_count}

if __name__ == '__main__':
    get_shop_list_by_dishes(['Омлет', 'Запеченый картофель', 'Фахитос'], 2)
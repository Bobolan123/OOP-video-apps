from random import randint

import pizza06 as pz
from extra06 import Extra

def get_random_item(dictionary):
    items = list(dictionary)
    random = randint(0, len(items) - 1)
    return items[random]


pizzas = {"margherita": 6.0, "napoletana": 7.0, "marinara": 7.5}
extras = {"mushrooms": 0.5, "cheese": 1.0, "anchovies": 1.5, "sausage": 1.8}

basket = []
n_random_pizzas = randint(2, 5)
for p in range(n_random_pizzas):
    pizza_type = get_random_item(pizzas)
    pizza_price = pizzas[pizza_type]

    pizza = pz.Pizza(pizza_type, pizza_price)

    n_random_extras = randint(1, 3)
    for e in range(n_random_extras):
        extra_type = get_random_item(extras)
        extra_price = extras[extra_type]

        pizza.add_extra(Extra(extra_type, extra_price))

    basket.append(pizza)

total_price = 0.0
for pizza in basket:
    total_price += pizza.price

print(f"Congratulations, you have won £{total_price:.2f} worth of pizzas:")
for pizza in basket:
    print(f" a {pizza.get_description()} worth £{pizza.price:.2f}")

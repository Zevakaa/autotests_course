# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


# Здесь пишем код
def generate_random_name() -> string:
    """ Генератор двух слов из случайных латинских букв разделенных пробелами """
    while 1:
        val = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 15))) + \
              ' ' + ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 15)))
        yield val


gen = generate_random_name()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

import random
from faker import Faker


fake = Faker()
# words = ['пицца', 'вода', 'лимонад', 'стейк', 'дом', 'мясо', "сок", "курятина", "диван", "книги"]
# word = random.choice(words)
word = fake.word()
print('Угадайте символ, который есть в загаданном слове (есть чит-код)')
guesses = ''
fake_chars = ''
turns = 20
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1
    print()
    if failed == 0:
        print('Верно, идите играть в нормальные игры!')
        break
    guess = input('Введи символ:\n')
    guesses += guess
    if guess == '/see_right_word':
        print('Пошёл нафиг, читер тупой!')
    if guess not in word:
        turns -= 1
        print('нет, ошибся ты,')
        print('Осталось поп-иток:', turns)
        fake_chars += guess
        print('Неверные буквы:', fake_chars)
        if turns == 0:
            print('Проигрыш')
            print('Верное слово:', word)
            break
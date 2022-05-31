#числовая игра угадайка
#мини-проект курса для нубов на степике
#загадываем число и просим пользователя его угадать, выводя системные сообщения
#для каждого ответа пользователя
#описываем функцию валидации ответа, интересует только целое число от 1 до 100
def is_valid(ans):
  return ans.isdigit()

#ф-я считывает ответ, в случае валидность - в инт, в ином считывает очередной
def sugg():
  answer = input()
  while not is_valid(answer):
    print("Incorrect value! Please, enter integer from 1 to 100:")
    answer = input()
  else:
    ans = int(answer)
  return ans

    
import random
#загадали число с помощью генератора случайных целых чисел диапазона [1, 100]
n = random.randint(1, 100)
#выводим приглашение к игре
print("GUESS THE INT!")
print("Enter your answer below:")
#считываем первый ответ вне цикла
ans = sugg()
#пока введенное пользователем число не совпадает с загаданным
while ans != n:
  if ans > n:
    print("Too much")
  else:
    print("Too less")
#для любого варианта запрашиваем новый ответ
  print("Try again!") 
  ans = sugg()
#действие на случай штатной отработки цикла - случай, когда значение угадано
else:
  print("Our congratulations! You're right!")

class listType :
  scores = [95, 90, 100]
  print(scores) # 95, 90, 100

  fruits = ["apple", "banana", "cherry"]
  print(fruits) # 'apple', 'banana', 'cherry'

  isPassed = [True, False, True]
  print(isPassed) # True, False, True
  print(isPassed[0]) # True
  print(isPassed[1]) # False
  print(isPassed[2]) # True
  print(isPassed[-1]) # True
  print(isPassed[-2]) # False

  sports = ["soccer", "baseball", "volleyball", "handball", "basketball"]
  print(sports[0:3]) # 'soccer', 'baseball', 'volleyball'
  print(sports[2:]) # 'volleyball', 'handball', 'basketball'
  print(sports[:4]) # 'soccer', 'baseball', 'volleyball', 'handball'
  print(sports[1:-2]) # 'baseball', 'volleyball'

class listAppend :
  fruits = ["apple", "banana", "cherry"]
  print(fruits) # 'apple', 'banana', 'cherry'

  fruits.append("peach")
  print(fruits) # 'apple', 'banana', 'cherry', 'peach'

class listPop :
  fruits = ["apple", "banana", "cherry"]
  print(fruits) # 'apple', 'banana', 'cherry'

  fruits.pop()
  print(fruits) # 'apple', 'banana'

  basket = fruits.pop(0)
  print(fruits) # 'banana'
  print(basket) # 'apple'
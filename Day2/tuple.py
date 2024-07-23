class tupleType :
  scores = (95, 90, 100)
  print(scores) # 95, 90, 100

  fruits = ("apple", "banana", "cherry")
  print(fruits)  # 'apple', 'banana', "'cherry'

  isPassed = (True, True, False)
  print(isPassed)  # True, True, False

  fruits = ("apple", "banana", "cherry")
  print(fruits[0])  # apple
  print(fruits[1])  # banana
  print(fruits[2])  # cherry

class tupleSilcing :
  fruits = ["apple", "banana", "cherry", "peach", "blueberry"]
  print(fruits[0:3])  # 'apple', 'banana', 'cherry'
  print(fruits[2:])  # 'cherry', 'peach', 'blueberry'
  print(fruits[:4])  # 'apple', 'banana', 'cherry', 'peach'
  print(fruits[1:-2])  # 'banana', 'cherry'
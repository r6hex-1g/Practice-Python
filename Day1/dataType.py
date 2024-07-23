class int :
  a = -1
  b = 7

  print(a + b) # 6
  print(a - b) # -8
  print(a * b) # -7
  print(a / b) # -0.14285714285714285
  print(a // b) # -1
  print(a % b) # 6
  print(a ** b) # -1

class str :
  name = "라희"
  firstJobName = "FE 개발자"
  secondJobName = "지망생"
  workingLang = "HTML, CSS"

  print(name) # 라희
  print(firstJobName + secondJobName) # FE 개발자지망생
  print("저는 " + name + "라고 합니다.") # 저는 라희라고 합니다.
  print("제가 하는 언어는 " + workingLang + "을 주로 합니다.") # 제가 하는 언어는 HTML, CSS을 주로 합니다.

class boolean :
  isStudent = True
  isTeacher = False

  print(isStudent) # True
  print(isTeacher) # False

class notBoolean :
  isStudent = "True"
  isTeacher = "False"

  print(isStudent) # True
  print(isTeacher) # False
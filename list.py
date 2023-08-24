

def first_last_number(numberList):
     print(numberList)
     first_number=numberList[0]
     last_number=numberList[-1]

     if first_number == last_number:
          return True
     else:
          return False
     
numbers_x = [10, 20, 30, 40, 10]
print(first_last_number(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
print(first_last_number(numbers_y))
!= #не рівність
== #рівність

num = int(input("enter num: "))

isHasCar = True
# ==, !=, <, >, <=, >=
if num >= 55 or  isHasCar and 5 == 5 or 6 > 7 :
    print("yes")
    if num == 100:
        print("num is 100")
elif num == 40:
    print("num is 40")
elif num == 45:
    print("num is 45")
elif num == 35:
    print("num is 35")
elif num < 4:
    print("num is less than 4")

else:
    print("else")

    isHappy = True
    if not isHappy:
        print("yes, he is happy")

        data = "info"
        # if data == ('info'):
        #   correct = True
        # else:
        #    correct = False

        correct = True if data == "info" else False

        print(correct)

data = ("info")
correct = True if data == 'info' else False
print(correct)

for i in range(5, 16, 1):
    print("el: ", i)

word = "some text"
for i in word:
    if i == 'm':
      print('letter m is on the word ')


work = True
while work:
    user_input = input("enter word stop: ")
    if user_input == 'Stop':
        work = False
print("while loop is done")

for i in range(1, 11):

    if i % 2 == 0:
        continue

    if i == 7:
        break
    print("El:",  i)

    import random

    num = [random.randint(1, 3) for _ in range(1)]
    print(num)

    if num == 1:
        print("scissors")
    elif num == 2:
        print("paper")
    else:
        print("rock")

import time
import random

num = random.randint(1, 3)
#print(num)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)


if num == 1:
  print("scissors")
elif num == 2:
  print("paper")
else:
  print("rock")

nums = [5, 7, -4, 5.54, 6, 6]
nums[0] = 34.98
#print(nums[3])

nums2 = [5, 7, 3, [5, "text", True]]
#print(nums2[-2])

nums.append(45)
nums.insert(1, False)
#nums.extend(nums2)
nums.sort()
nums.reverse()
nums.remove(34.98)
#nums.pop()
#nums.clear()

print(nums)
print(nums.count(6))
print(len(nums))
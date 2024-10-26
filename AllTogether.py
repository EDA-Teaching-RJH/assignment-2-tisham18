import random
list = [random.randint(1, 100) for x in range(10)]
print(f"input: {list}")

i = 0
while i < len(list):
      if list[i] % 2 == 0:
            list.pop(i)
      else:
            i +=1
    
print(f"ouput: {list}")
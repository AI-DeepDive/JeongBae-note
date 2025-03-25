# python study start 

#int 정수
x = 1
print(x)
print(type(x))

# float 
y = 2.5
print(y)
print(type(y))

# string
a = 'hello'
b = "hello2" # 큰 따옴표나 작은 따옴표나 상관 없음. 
print(a)
print(b)
print(type(a))
print(type(b))

# logical / boolean
q1 = True
q2 = False
print(q1)
print(q2)
print(type(q1))
print(type(q2))

# Working with variables

# Arithmetics
A = 10
B = 5 
C = A + B
D = B / A 

print(C)
print(D) # division is different to python 2.7 -> 정수끼리 계산해도 실수가 나올 수 있다. 2.7버전은 정수만 나왔다. 

import math # math 모듈을 import
print(math.sqrt(A)) # math 모듈의 sqrt(제곱근) 기능을 사용
print(math.sqrt(144))
print(round(math.sqrt(A))) # round 함수는 반올림 

greeting = "hello"
name = "Bob"
message = greeting + "  " + name + "2" # 마지막에 2를 넣으면 오류가 난다. 
print(message)

# Boolean variables and operators
# boolean / logical
# True
# False 

print(4 < 5)
print( 4 > 100 )
print( 4 == 5 )
print( 4 != 4 ) 

result = 4 < 5 
print(result)
print(type(result))
result2 = not(5 > 4)
print(result2)
print(type(result2))

print(result or result2)
print(result and result2)


# The While loop  

# while condition:
#   executable code1 해당 코드를 실행 
# condition이 거짓이라고 판단될때까지 executable code1을 반복 

while False: # 조건 자체가 거짓이어서 실행되지 않는다. 
    print("hello")

# while True:
#    print("hello") 무한 루프에 걸린다. 실행하지 말것. ㅋ

counter = 0
while counter < 12:
    print(counter)
    counter = counter + 1 

# The for loop 
for i in range(5):
    print("hello python")
print(range(5)) # 마지막 숫자는 포함하지 않는다. 
print(list(range(5)))

for i in range(5):
    print("hello python", i)

my_list = [10, 100, 1000]
print(my_list)
for jj in my_list:
    print("jj is equal to:", jj)
    print("jj is equal to:", my_list)


# The If statement 

import numpy as np
from numpy.random import randn # random은 임의의 수를 생성해주는 함수
# from np.random import randn 은 안된다. 파이썬은 from 을 써서 그 뒤에 오는 모듈을 찾으려고 하는데,
# 그런 이름의 모듈은 없어서 error가 발생 

x = randn()
if x > 1:
    answer = "Greater than 1"
print(x)
print(answer)

# 또 다른 방식 
from numpy.random import randn # 바로 randn()을 사용 가능하게 함.
# 그렇지 않으면 numpy.random.randn() 과 같이 사용하여야 함.
# 사실상 import numpy as np를 할 필요가 없음. 현재 상황에서 numpy의 다른 함수나 모듈을 사용하는게 아니기 때문.
answer = None # same mean as null 
y = randn()
if y > 1:
    answer = "Greater than 1"
print(y)
print(answer)

answer = None
z = randn()
if z > 1:
    answer = "Greater than 1"
else:
    answer = "less than 1"
print(z)
print(answer)

# Nested statement
answer = None
x = randn()
if x >1:
    answer = "Greater than 1"
else:
    if x >= -1:
        answer = "Between -1 and 1"
    else:
        answer = "less than -1"
print(x)
print(answer)

# chained statement 
answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
elif x >= -1:
    answer = "Between 1 and -1"
else:
    answer = "less than -1"
print(x)
print(answer)
## nested statement와 chain statement를 혼동하는 경우가 있음. 



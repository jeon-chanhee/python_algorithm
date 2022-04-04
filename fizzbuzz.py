'''
1. 1에서 100까지 출력
2. 3의 배수는 Fizz 출력
3. 5의 배수는 Buzz 출력
4. 3과 5의 공배수는 FizzBuzz 출력
'''

# for i in range(1,101):
#     print(i)
#
#     if i % 3 == 0:
#         print('Fizz')
#
#     elif i % 5 == 0:
#         print('Buzz')
#
#     elif (i % 3 == 0) and (i % 5 == 0):
#         print('FizzBuzz')

# 코드 단축 버전
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

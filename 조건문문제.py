
#
# num = int(input('성적을 입력하세요.'))
#
# if (num <= 100) and (num >= 90):
#     print('A')
#
# elif (num < 90) and (num >= 80):
#     print('B')
#
# elif (num < 80) and (num >= 70):
#     print('C')
#
# elif (num < 70) and (num >= 60):
#     print('D')
#
# else:
#     print('F')


'''
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
'''

# year = int(input())
#
# if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
#     print(1)
# else:
#     print(0)


# n = 1000
# m = -1000
#
# while True:
#
#     x = int(input(f'x값을 입력해주세요. ({m}이상 {n}이하의 숫자): '))
#
#     if (x > 1000) or (x < -1000):
#         print('범위를 넘었습니다. 다시 입력해주세요')
#
#     else:
#         while True:
#             y = int(input(f'y값을 입력해주세요. ({m}이상 {n}이하의 숫자): '))
#
#             if (y > 1000) or (y < -1000):
#                 print('범위를 넘었습니다. 다시 입력해주세요')
#
#             else:
#                 break
#         break
#
#
#
# if (x > 0) and (y > 0):
#     print(2)
#
# elif (x < 0) and (y > 0):
#     print(1)
#
# elif (x > 0) and (y < 0):
#     print(3)
#
# elif (x < 0) and (y < 0):
#     print(4)



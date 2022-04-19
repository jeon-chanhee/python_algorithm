
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


'''

"45분 일찍 알람 설정하기"이다.

이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.

현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.
'''

while True:
    hm = input('알람시간 : ')
    a = hm.split(' ')
    h = int(a[0])
    m = int(a[1])

    hours = [b for b in range(24)]
    minutes = [c for c in range(59)]

    if (h < 0) or (h > 23) or (m < 0) or (m > 60):
        print('숫자 입력을 다시 해주세요.')

    else:
        print(hours)





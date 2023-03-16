a = int(input())

if not (1<= a <= pow(10,9)):
    print("범위 밖 입니다.")

b = a*2

if (1<= a <= pow(10,9)):
    if a == 1:
        print(4)
    if (1< a <= pow(10,9)/2):
        print(b)
    if (a > pow(10, 9)/2):
        print(pow(10, 9))

'''
27, 47 검사
'''
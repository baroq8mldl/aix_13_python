def print_n_times(*values,n=1):
    for i in range(n):
        for v in values:
            print(v)
        print()
    return
# ans = print_n_times('안녕','즐거운','파이썬 프로그래밍',n=3,)
# print('ans',ans)
# print_n_times(3,'안녕','즐거운','파이썬 프로그래밍')
# print_n_times(3,10,30,50,70)

# greeting(이름) -> 출력: 안녕하세요 이름님
def greeting(name):
    return "안녕하세요 "+name+"님"

# ans = greeting("홍길동") # -> 안녕하세요 홍길동님
# print(ans)

# 입력받는 숫자들의 평균을 반환하는 함수
def calc_avg(*values):
    tot = 0
    for i in values:
        tot += i # 누적
    return tot / len(values)

ans = calc_avg( 10,20,40,50 )
print(ans)
ans = calc_avg( 10,20, )
print(ans)

# 점수를 입력받아 학점을 반환하는 함수를 작성하시오.
# 함수이름 : get_grade()
"""
90 이상 → A 반환
80 이상 → B 반환
70 이상 → C 반환
나머지 → F 반환
"""
#사용예시
# def get_grade(grade):
#     if grade >= 90 :
#         return 'A'
#     if grade >= 80 :
#         return 'B'
#     if grade >= 70:
#         return 'C'
#     return 'F'
# ans = get_grade(95)
# print(ans)
# ans = get_grade(65)
# print(ans)

# 가위,바위,보 중 하나는 임의로 반환하는 함수
# 이름: get_gbb()
## 사용예시
# def get_gbb():
#     import random
#     r = random.randint(0,2)
#     arr = '가위,바위,보'.split(',')
#     return arr[r]

# ans = get_gbb()
# print(ans)
###############
def fac(n):
    if n==0:
        return 1
    return n * fac(n-1)

ans = fac(3)
print('fac(3)=',ans)

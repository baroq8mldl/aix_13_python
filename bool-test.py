print( 10==100 ) # False
print( 10 != 100 ) # True
print( 10 <= 100 ) # True
print( 10 >= 100 ) # False
a = "가방"
b = "하마"
print( a == b )
print( a < b ) # 글자의 순서. True
print( a > b ) # False
c = 35
print( 10 < c < 30) # Frue
print( 10 < c < 20) # False

if not c < 30:
    print("c는 30보다 작음")
    print("c는 30보다 작음")
else:
    print("c는 30보다 큼")
    print("c는 30보다 큼")
print("END")
######################
score = 68
grade = "" #비워둠
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"{score}의 학점은 {grade}")
################
score = 78
grade =""
if score <= 100 and score >=90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
else:
    grade = "F"
print(f"{score}의 학점은 {grade}")

try:
    list1 = [10,20,30]
    n = list1[3]
    print(n)
except Exception as ex:
    print("오류발생!!")
    print('TYPE',type(ex))
    print('ex',ex)

print("end")
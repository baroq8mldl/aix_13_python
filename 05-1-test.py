# 인사말함수
def hello():
    print("안녕하세요")

def hello_ntimes(msg="안녕하세요",n=1):
    for i in range(n):
        print(msg)

# hello_ntimes("방가방가",3)
# def gugudan(n=2):
#     for i in range(1,10):
#         print(f'{n}*{i}={n*i}')
def gugudan(n=2, n2=-1):
    if n2 == -1:
        for i in range(1,10):
            print(f'{n}*{i}={n*i}')
    else:
        for dan in range(n,n2+1):
            for i in range(1,10):
                print(f'{dan}*{i}={dan*i}')
                

# gugudan(3) #->3단 구구단 출력
# gugudan()  #->2단 구구단 출력
gugudan(2,5) # 2단~5단 까지 출력

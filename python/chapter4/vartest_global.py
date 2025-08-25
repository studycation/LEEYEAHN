#함수 안에서 함수 밖의 변수를 변경하는 방법
#2. global 사용

a = 1 
def vartest():
    global a 
    a = a + 1

vartest()
print(a)
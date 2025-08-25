#함수 안에서 함수 밖의 변수를 변경하는 방법 
#1. return 사용

a =1
def vartest(a):
    a = a + 1
    return a 

a = vartest(a)
print(a)
#1부터 10까지의 숫자 중에서 3의 배수를 뺸 나머지 값을 출력 
a = 0
while a <10:
    a += 1
    if a % 3 == 0: continue
    print(a%3)
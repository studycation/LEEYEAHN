f = open("새파일.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다." % i
    f.write(data)
f.close()
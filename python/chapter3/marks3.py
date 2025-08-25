"""
합격축하문장을 출력하는 예제 
range 함수를 이용하여 
이거 좀 신기함
"""

marks = [ 90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다." %(number + 1))
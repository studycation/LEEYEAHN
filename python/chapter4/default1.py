def say_myself(name, age, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % age)
    if man: 
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself('이예안', 20, False)

#초깃값이 있는 매개변수(man)은 항상 뒤쪽에 놓아야 한다. = 초기화하고 싶은 매개변수는 항상 뒤쪽에 놓아야한다. 

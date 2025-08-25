#주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라
pocket = ['money', 'cellphone']
card = True 
if 'money' in pocket:
    print("택시를 타고 가라")
elif card: #if 조건문에서 money 유무를 따졌으니 money가 pocket에 없다는 조건문은 다시 쓰지 않아도 된다. 
    print("택시를 타고 가라") 
else:
    print("걸어가라")
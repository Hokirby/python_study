a=0
asum=0
while True:
    print("---- Menu ----")
    print("1. 콜라 / 300")
    print("2. 사이다 / 300")
    print("3. 커피 / 200")
    print("4. 돈 넣기")
    print("5. 잔돈 반환")
    print("6. 종료")
    print("----------------")
    print("현재 금액{}".format(asum))
    b=int(input("메뉴 선택 : "))
    print()
    if  b==4:
        a=int(input("돈을 넣어 주세요: "))
        asum=asum+a
    elif b==1 and a>=300:
        print("콜라 맛있게드세요")
        asum=asum-300
    elif b==2 and a>=300:
        print("사이다 맛있게드세요")
        asum=asum-300
    elif b==3 and a>=200:
        print("커피 맛있게 드세요")
        asum=asum-200
    elif b==5:
        print("잔돈이 반환됩니다.")
        asum=0
    elif b==6:
        break
    else:
        print("금액이 부족합니다.")
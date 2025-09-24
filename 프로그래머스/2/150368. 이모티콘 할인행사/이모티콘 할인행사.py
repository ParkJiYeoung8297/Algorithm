# 제일 비싼걸, 가장 크게 할인했을 때 가입자 수가 가장 많을 것이다.
from itertools import product
def solution(users, emoticons):
    answer = [0,0]
    sale_percent=[10,20,30,40] 
    
    # 각 이모티콘 별 할인율 결정
    sales=set(product(sale_percent,repeat=len(emoticons)))

    for sale in sales:
        sign=0 # 가입자 수 
        total_price=0 # 총 구매 가격
        for user in users:
            purchase_price=0 # 한 사용자의 총 구매 가격
            for idx,price in enumerate(emoticons):
                # 사용자 희망 할인율<=할인율 이어야 구매
                if user[0]<=sale[idx]:    
                    purchase_price+=price*(100-sale[idx])*(0.01) # 할인된 가격
            # 만약 예산보다 구매 가격이 크면 가입하기
            if purchase_price>=user[1]:
                purchase_price=0
                sign+=1
            else:
                total_price+=purchase_price            
        # 만약 가입자 수가 증가하면 답안 갱신 (1순위)
        if answer[0]<sign:
            answer=[sign, total_price]
        # 가입자 수가 동일한데, 수입이 증가하면 답안 갱신 (2순위)
        elif answer[0]==sign:
            if answer[1]<total_price:
                answer=[sign, total_price]

    return answer
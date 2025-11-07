from collections import defaultdict
def solution(enroll, referral, seller, amount):
    parentMember = defaultdict()
    memberProfit = defaultdict()
    
    # 부모 표시
    for i in range(len(enroll)):
        parentMember[enroll[i]]=referral[i]
        memberProfit[enroll[i]]=0
    
    # 수익 계산     
    for i in range(len(seller)):
        price=amount[i]*100
        memberProfit[seller[i]]+=price
        curr_member=seller[i]
        curr_profit=price
        
        while parentMember[curr_member]!="-":
            curr_profit=int(curr_profit*0.1)
            if curr_profit==0:
                break
            memberProfit[curr_member]-=curr_profit
            curr_member=parentMember[curr_member]
            memberProfit[curr_member]+=curr_profit

        memberProfit[curr_member]-=int(curr_profit*0.1)
        
    return [memberProfit[i] for i in enroll]
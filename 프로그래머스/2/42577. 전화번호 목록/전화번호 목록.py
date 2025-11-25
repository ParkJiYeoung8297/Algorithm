# string은 sort()하면 사전순 정렬됨, startswith로 시작하는지 확인
# 사전순 정렬이기 때문에 바로 뒤만 검사하면 됨, (abc - adce -abce 이렇게 될 수 없음)
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
            
    return True
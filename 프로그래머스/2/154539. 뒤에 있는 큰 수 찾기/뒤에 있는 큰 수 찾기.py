# 맨 뒤에서부터 update
# stack에 내림차순으로 넣어두고, stack맨뒤랑 numbers[i]랑 비교하기
# stack 맨뒤가 크면 answer 갱신, stack 중 numbers[i] 보다 큰게 없으면 갱신 안함(=-1)
def solution(numbers):
    answer = [-1]*len(numbers)
    stack=[numbers[-1]]
    for i in range(len(numbers)-2,-1,-1):
        if numbers[i]<stack[-1]:
            answer[i]=stack[-1]
            stack.append(numbers[i])
        else:
            while stack and numbers[i]>=stack[-1]:
                stack.pop()
            if stack:
                answer[i]=stack[-1]
            stack.append(numbers[i])
    return answer
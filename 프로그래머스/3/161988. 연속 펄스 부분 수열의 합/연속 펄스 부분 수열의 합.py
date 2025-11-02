def solution(sequence):
    candPlus=sequence.copy()
    candMinus=sequence.copy()
    dpMinus=[0]*len(sequence)
    dpPlus=[0]*len(sequence)
    
    # +1 시작, -1 시작으로 곱해놓고, 누적합 최대 구하기
    for i in range(len(sequence)):
        if i%2==0:
            candMinus[i]=-candMinus[i]
        else:
            candPlus[i]=-candPlus[i]
        if i==0:
            dpMinus[i]=candMinus[i]
            dpPlus[i]=candPlus[i]
        else:
            dpMinus[i]=max(candMinus[i], dpMinus[i-1]+candMinus[i])
            dpPlus[i]=max(candPlus[i], dpPlus[i-1]+candPlus[i])
    
    return max(*dpMinus,*dpPlus)
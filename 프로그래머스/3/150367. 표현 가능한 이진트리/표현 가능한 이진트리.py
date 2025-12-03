# 7 : 111          1+2+4
# 42 : 0101010     2+8+32
# 5 : 101 → 루트 노드가 없음 (불가능)
# 63 : 0111111     1+2+4+8+16+32
# 95 : 1000001     1+2+4+8+16+64
# 규칙 : 부모가 0일때, 자식이 1이면 "불가능" (중요)
def solution(numbers):
    answer = []
    for num in numbers:
        binary_num=bin(num)[2:]
        
        i=1
        length=1
        while len(binary_num)>length:
            i=i*2
            length=length+i
        binary_num=binary_num.rjust(length,"0")
        
        flag=1
        def check(start,end):
            nonlocal flag
            
            if start==end:
                return 
            if flag==0:
                return
            
            mid=(start+end)//2
            left_start,left_end=start,mid-1
            right_start,right_end=mid+1,end

            # 부모가 0인데 자식이 1이면 안됨
            if binary_num[mid]=="0":
                if "1" in binary_num[left_start:left_end+1] or "1" in binary_num[right_start:right_end+1]:
                    flag=0
                    return
            check(left_start,left_end)
            check(right_start,right_end)
                
        check(0,length-1)        
        answer.append(flag)
            
    return answer
def solution(h1, m1, s1, h2, m2, s2):
    count = 0
    # 시간/분을 초로 환산
    start=h1*3600+m1*60+s1
    end=h2*3600+m2*60+s2
    
    if start>end:
        end+=24*3600
    
    # 시/분/초 각도 계산
    def position(t):
        now_h=(t%43200)/120 # 12시간이 한바퀴 (360도 / 43200)
        now_m=(t%3600)/10 # 60분이 한바퀴
        now_s=(t%60)*6 # 60초가 한바퀴
        return now_h,now_m,now_s
    
    # 시작점 따로 처리 (완전 일치한 경우)
    h,m,s=position(start)
    if s==m or s==h:
        count+=1
    
    for t in range(start,end): 
        h,m,s=position(t)
        nh,nm,ns=position(t+1)
        
        # 초침 354도 → 0도 시침 5 → 8도  , 앞지르지 않았는데 초침이 값으로 뒤쳐짐
        # 그래서 초침이 바뀔 때, 0~10도 사이에 분침/시침 있으면 값을 보정해줌
        if ns==0:
            ns=360
            if nm<=10:
                nm+=360
            if nh<=10:
                nh+=360
        
        # 시침 초침
        if s-h<0 and ns-nh>0:
            count+=1
        
        # 분침 초침
        if s-m<0 and ns-nm>0:
            count+=1
        
        # 완전 일치
        if ns==nm or ns==nh:
            count+=1
                
        
    return count
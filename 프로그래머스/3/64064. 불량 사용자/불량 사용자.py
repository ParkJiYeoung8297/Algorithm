def solution(user_id, banned_id):
    answer = set()
    visited=["0"]*len(user_id)
    
    def isBad(user,ban):
        if len(user)!=len(ban):
            return 0
        for i in range(len(user)):
            if ban[i]=="*":
                continue
            if ban[i]!=user[i]:
                return 0
        return 1
    
    stack=[]
    for idx,user in enumerate(user_id):
        if isBad(user,banned_id[0]):
            nvisited=visited.copy()
            nvisited[idx]="1"
            stack.append((1,nvisited))
    while stack:
        idx,nvisited=stack.pop()
        if idx>=len(banned_id):
            answer.add("".join(nvisited))
        else:
            for i, user in enumerate(user_id):
                if nvisited[i]=="0" and isBad(user,banned_id[idx]):
                    newVisited=nvisited.copy()
                    newVisited[i]="1"
                    stack.append((idx+1,newVisited))
    return len(answer)
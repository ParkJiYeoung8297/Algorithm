def solution(word):
    answer = 0
    dict_w={'A':1, 'E':2, 'I':3, 'O':4, 'U':5}
    # [0,5,25,125,625]
    scale = [780, 155, 30, 5, 0]
    word=word.ljust(5," ")
    for i in range(len(word)):
        if word[i]==" ":
            continue
        answer+=scale[i]*(dict_w[word[i]]-1)+dict_w[word[i]]
    
    return answer

"""
이해를  위한 예시
A
    AA
        AAA

            AAAA
                AAAAA
                AAAAE
                AAAAI
                AAAAO
                AAAAU

            AAAE
                AAAEA
                AAAEE
                AAAEI
                AAAEO
                AAAEU

            AAAI
                AAAIA
                AAAIE
                AAAII
                AAAIO
                AAAIU

            AAAO
                AAAOA
                AAAOE
                AAAOI
                AAAOO
                AAAOU

            AAAU
                AAAUA
                AAAUE
                AAAUI
                AAAUO
                AAAUU

        AAE
            AAEA
            AAEE
            AAEI
            AAEO
            AAEU
...

"""
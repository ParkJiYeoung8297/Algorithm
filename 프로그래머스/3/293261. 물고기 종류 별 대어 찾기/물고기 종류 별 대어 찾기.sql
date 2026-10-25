# 물고기 종류 별로 가장 큰 물고기
# 물고기의 ID에 대해 오름차순 정렬
SELECT ID, FISH_NAME, MAX_LENGTH as LENGTH
FROM (
    SELECT 
        fi.ID, 
        fni.FISH_NAME, 
        fi.LENGTH, 
        max(fi.LENGTH) over(partition by fi.FISH_TYPE) as MAX_LENGTH
    FROM FISH_INFO as fi
    JOIN FISH_NAME_INFO as fni
    ON fi.FISH_TYPE = fni.FISH_TYPE) as fish
WHERE LENGTH = MAX_LENGTH
ORDER BY ID;
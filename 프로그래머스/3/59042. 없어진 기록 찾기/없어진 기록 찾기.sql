# 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물
# ID 순으로 오름차순 조회
# LEFT JOIN
SELECT ao.ANIMAL_ID, ao.NAME
FROM ANIMAL_OUTS as ao
LEFT JOIN ANIMAL_INS as ai
ON ao.ANIMAL_ID = ai.ANIMAL_ID
WHERE ai.ANIMAL_ID is null
ORDER BY ao.ANIMAL_ID ASC;
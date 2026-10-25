# 아직 입양을 못 간 동물
# 가장 오래 보호소에 있었던 동물 3마리
# 보호 시작일 순 오름차순
SELECT ai.NAME, ai.DATETIME
FROM ANIMAL_INS as ai
LEFT JOIN ANIMAL_OUTS as ao
ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE ao.ANIMAL_ID is null
ORDER BY DATETIME ASC
LIMIT 3;

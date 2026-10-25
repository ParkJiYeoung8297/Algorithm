# 보호 시작일보다 입양일이 더 빠른 동물
# 보호 시작일이 빠른 순 오름차순
SELECT ai.ANIMAL_ID, ai.NAME
FROM ANIMAL_INS as ai
JOIN ANIMAL_OUTS as ao
WHERE ai.ANIMAL_ID = ao.ANIMAL_ID AND ai.DATETIME > ao.DATETIME
ORDER BY ai.DATETIME ASC;
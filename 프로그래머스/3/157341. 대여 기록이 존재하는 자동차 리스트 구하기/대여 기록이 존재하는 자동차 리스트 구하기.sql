-- 코드를 입력하세요
# 자동차 종류가 '세단'
# 10월에 대여를 시작한 기록이 있는 자동차
# 자동차 ID 리스트는 중복이 없음
# 자동차 ID를 기준으로 내림차순 정렬

SELECT distinct(crcc.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR as crcc
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY as crcrh
ON crcc.CAR_ID = crcrh.CAR_ID
WHERE crcc.CAR_TYPE = '세단' AND crcrh.START_DATE>='2022-10-01'
ORDER BY crcc.CAR_ID DESC;
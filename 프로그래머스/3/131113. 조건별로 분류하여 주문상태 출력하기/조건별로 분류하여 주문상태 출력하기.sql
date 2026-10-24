# 2022년 5월 1일을 기준
# 2022년 5월 1일까지 출고완료로 이 후 날짜는 출고 대기로 미정이면 출고미정으로 출력
# 주문 ID를 기준으로 오름차순 정렬

SELECT 
    ORDER_ID, 
    PRODUCT_ID, 
    DATE_FORMAT(OUT_DATE, '%Y-%m-%d') as OUT_DATE,
    CASE 
        WHEN OUT_DATE is null THEN '출고미정'
        WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
        WHEN OUT_DATE > '2022-05-01' THEN '출고대기'
    END as '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC;
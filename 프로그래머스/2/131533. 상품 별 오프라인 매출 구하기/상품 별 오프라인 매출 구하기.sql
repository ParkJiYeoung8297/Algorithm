# 상품코드 별 매출액(판매가 * 판매량) 합계
# 매출액을 기준으로 내림차순 정렬, 상품코드를 기준으로 오름차순 정렬
SELECT p.PRODUCT_CODE, p.PRICE * sum(os.SALES_AMOUNT) as SALES
FROM PRODUCT as p
JOIN OFFLINE_SALE as os
ON p.PRODUCT_ID	= os.PRODUCT_ID
GROUP BY p.PRODUCT_ID
ORDER BY SALES DESC, p.PRODUCT_CODE ASC;
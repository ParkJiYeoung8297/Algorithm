# 7월 아이스크림 총 주문량 + 상반기의 아이스크림 총 주문량이 큰 순서대로 상위 3개의 맛
SELECT fh.FLAVOR
FROM FIRST_HALF as fh
JOIN JULY as j
ON fh.FLAVOR = j.FLAVOR
GROUP BY fh.FLAVOR
ORDER BY sum(fh.TOTAL_ORDER)+sum(j.TOTAL_ORDER) DESC
LIMIT 3;
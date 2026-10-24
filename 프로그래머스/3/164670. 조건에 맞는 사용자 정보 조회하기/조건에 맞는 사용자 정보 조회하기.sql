# 중고 거래 게시물을 3건 이상 등록한 사용자
# 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력
# 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(-)을 삽입하여 출력
# 회원 ID를 기준으로 내림차순 정렬

SELECT 
    ugu.USER_ID, 
    ugu.NICKNAME, 
    concat_ws(' ', ugu.CITY, ugu.STREET_ADDRESS1, ugu.STREET_ADDRESS2) as 전체주소, 
    concat(
        substring(ugu.TLNO, 1,3), '-',
        substring(ugu.TLNO, 4,4), '-',
        substring(ugu.TLNO, 8,4)
          ) as 전화번호
FROM USED_GOODS_BOARD as ugb
JOIN USED_GOODS_USER as ugu
ON ugb.WRITER_ID = ugu.USER_ID
GROUP BY ugu.USER_ID
HAVING count(*) >= 3
ORDER BY ugb.WRITER_ID DESC;
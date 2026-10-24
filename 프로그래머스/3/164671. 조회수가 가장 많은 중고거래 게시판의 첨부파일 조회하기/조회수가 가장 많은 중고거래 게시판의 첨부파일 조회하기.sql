# 조회수가 가장 높은 중고거래 게시물
# FILE ID를 기준으로 내림차순 정렬
# 파일이름은 파일 ID, 파일 이름, 파일 확장자로 구성되도록 출력
# 게시글 ID를 기준으로 디렉토리가 구분


SELECT concat_ws('/','/home/grep/src', ugf.BOARD_ID, concat(ugf.FILE_ID,FILE_NAME, ugf.FILE_EXT)) as FILE_PATH
FROM USED_GOODS_FILE as ugf
JOIN (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1) as mv
ON mv.BOARD_ID = ugf.BOARD_ID
ORDER BY FILE_ID DESC;

# Write your MySQL query statement below
-- 1) 전체 레코드 수가 홀수일 때 마지막 데이터는 바꾸지 않아도 됨
--    -> id가 레코드 개수와 같을 때 
-- 2) id가 홀수일 때 +1, id가 짝수일 때 -1 에 있는 데이터 출력

# 똑같은 테이블 조인.. 셀프?
# UNION / CASE WHEN / id 를 바꿔도 됨... 
# MAX()

-- SELECT
--     CASE
--     WHEN MOD(id,2)=0 THEN id-1
--     WHEN ((MOD(id,2)=1) AND (id+1 != MAX(id))) THEN id+1
--     ELSE id END id
--     ,student
-- FROM Seat
-- ORDER BY id asc

SELECT
       CASE 
        WHEN MOD(id, 2) = 1 AND id + 1 <= (SELECT MAX(id) FROM Seat)
        THEN id + 1
        WHEN MOD(id, 2) = 0
        THEN id - 1
        ELSE id
    END AS id
    ,student
FROM Seat
ORDER BY id asc

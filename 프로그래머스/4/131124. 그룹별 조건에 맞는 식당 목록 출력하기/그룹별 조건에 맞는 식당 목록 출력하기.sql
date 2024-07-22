SELECT
    MEMBER_NAME
    ,REVIEW_TEXT
    ,DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d') REVIEW_DATE
FROM REST_REVIEW
JOIN MEMBER_PROFILE 
USING (MEMBER_ID) 
#개수가 MAX 개수인 모든 MEMBER_ID를 구하는 서브쿼리
WHERE MEMBER_ID IN (SELECT MEMBER_ID
                    FROM REST_REVIEW
                    GROUP BY MEMBER_ID
                    #MAX 개수를 구하는 서브쿼리
                    HAVING COUNT(REVIEW_ID) = (SELECT COUNT(REVIEW_ID) CNT 
                                                FROM REST_REVIEW
                                                GROUP BY MEMBER_ID
                                                ORDER BY COUNT(REVIEW_ID) DESC
                                                LIMIT 1))
ORDER BY 3,2
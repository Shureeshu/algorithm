-- 주문량이 많은 아이스크림들 조회하기

# SELECT FLAVOR
# FROM
#     SELECT * FROM FIRST_HALF
#     UNION ALL
#     SELECT * FROM JULY
# GROUP BY FLAVOR
# ORDER BY SUM(TOTAL_ORDER) DESC LIMIT 3

SELECT FLAVOR
FROM 
(SELECT * FROM FIRST_HALF
UNION ALL
SELECT * FROM JULY) AS T
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC LIMIT 3
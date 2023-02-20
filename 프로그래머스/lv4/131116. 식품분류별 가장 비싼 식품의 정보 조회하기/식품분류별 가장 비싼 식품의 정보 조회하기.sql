-- 식품분류별 가장 비싼 식품의 정보 조회하기
SELECT CATEGORY, MAX_PRICE, PRODUCT_NAME
FROM 
    FOOD_PRODUCT AS A
    CROSS JOIN
    (
    SELECT 
         CATEGORY,
         MAX(PRICE) AS MAX_PRICE
     FROM FOOD_PRODUCT
     GROUP BY CATEGORY
    ) B
    USING (CATEGORY)
WHERE
    MAX_PRICE = PRICE
    AND CATEGORY REGEXP "과자|국|김치|식용유"
ORDER BY MAX_PRICE DESC

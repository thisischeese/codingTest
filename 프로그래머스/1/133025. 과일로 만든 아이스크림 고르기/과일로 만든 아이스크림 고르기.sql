-- 코드를 입력하세요
SELECT F.FLAVOR
FROM FIRST_HALF F
    JOIN ICECREAM_INFO I
    ON F.FLAVOR = I.FLAVOR and I.INGREDIENT_TYPE = "fruit_based"
GROUP BY FLAVOR
HAVING SUM(TOTAL_ORDER) >= 3000
ORDER BY FLAVOR ASC



SELECT ROUND(AVG(CASE WHEN CAR_TYPE="SUV" then DAILY_FEE else null end)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
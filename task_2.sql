SELECT 
    track AS "Трекер заказа",
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS "Статус"
FROM "Orders";
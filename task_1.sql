SELECT 
    c.login AS "Логин курьера",
    COUNT(o.id) AS "Количество заказов в доставке"
FROM "Couriers" c
LEFT JOIN "Orders" o ON c.id = o."courierId" AND o."inDelivery" = true
GROUP BY c.login
ORDER BY c.login;
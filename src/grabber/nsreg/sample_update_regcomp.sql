INSERT INTO regcomp (name, nic_handle1, nic_handle2, city, website, price_reg, price_prolong, price_change) 
VALUES ('name', 'nic_handle1', 'nic_handle2', 'city', 'website', 'price_reg', 'price_prolong', 'price_change') 
ON CONFLICT (name) DO UPDATE
SET ( nic_handle1, nic_handle2, city, website, price_reg, price_prolong, price_change) =    (
    COALESCE('nic_handle1', regcomp.nic_handle1),
    COALESCE('nic_handle2', regcomp.nic_handle2),
    COALESCE('city', regcomp.city),
    COALESCE('website', regcomp.website),
    COALESCE('price_reg', regcomp.price_reg),
    COALESCE('price_prolong', regcomp.price_prolong),
    COALESCE('price_change', regcomp.price_change)
    )
RETURNING id;
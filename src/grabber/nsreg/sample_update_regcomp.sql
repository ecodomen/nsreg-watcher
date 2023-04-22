INSERT INTO regcomp (name, note1, note2, city, website, pricereg, priceprolong, pricechange) 
VALUES ('name', 'note1', 'note2', 'city', 'website', 'pricereg', 'priceprolong', 'pricechange') 
ON CONFLICT (name) DO UPDATE
SET ( note1, note2, city, website, pricereg, priceprolong, pricechange) =    (
    COALESCE('note11', regcomp.note1),
    COALESCE('note2', regcomp.note2),
    COALESCE('city', regcomp.city),
    COALESCE('website', regcomp.website),
    COALESCE('pricereg', regcomp.pricereg),
    COALESCE('priceprolong', regcomp.priceprolong),
    COALESCE('pricechange', regcomp.pricechange)
    )
RETURNING id;
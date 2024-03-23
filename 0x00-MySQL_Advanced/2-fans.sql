-- SQL script that ranks the country origins of bands based
-- on the number of non-unique fans.

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

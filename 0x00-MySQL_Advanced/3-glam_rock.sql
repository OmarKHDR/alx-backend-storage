-- hello world please answer my call
-- lists all bands with Glam rock as their main style,
-- ranked by their longevity
SELECT band_name, IFNULL(split, 2022) - formed AS lifespan 
FROM metal_bands
WHERE style LIKE '%glam rock%'
ORDER BY fans DESC;

SELECT
    database,
    name
FROM system.tables
WHERE database NOT IN ('system')
ORDER BY database, name;

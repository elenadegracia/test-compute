SELECT
    owner,
    table_name
FROM all_tables
WHERE owner NOT IN ('SYS', 'SYSTEM')
ORDER BY owner, table_name;

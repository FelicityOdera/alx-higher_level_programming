-- lists all records of table second_table of database hbtn_0c_0 in my DB.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` !=""
ORDER BY `score` DESC

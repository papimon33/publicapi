-- API: GET /flight/schedule/taxfree-dom
SELECT *
FROM
(SELECT
	TO_CHAR (A.DOMESTIC_STDATE, 'YYYYMMDD')||A.DOMESTIC_IDX AS "fid",
	A.CRUD_TP_CD AS "fgenType",
	to_char (A.DOMESTIC_REGDATE , 'YYYYMMDDHH24MISS') AS "fgentime",
    A.DOMESTIC_NUM AS "flightid",
    A.DOMESTIC_START_TIME AS "st",
    to_char(A.DOMESTIC_STDATE, 'YYYYMMDD') AS "firstdate",
    to_char(A.DOMESTIC_EDDATE, 'YYYYMMDD') AS "lastdate",
    A.DOMESTIC_MON AS "ynmon",
    A.DOMESTIC_TUE AS "yntue",
    A.DOMESTIC_WED AS "ynwed",
    A.DOMESTIC_THU AS "ynthu",
    A.DOMESTIC_FRI AS "ynfri",
    A.DOMESTIC_SAT AS "ynsat",
    A.DOMESTIC_SUN AS "ynsun",
    B.AIRLINE_KOREAN AS "airline",
    B.AIRLINE_CODE2 AS "airlineCode",
    A.DOMESTIC_START_CITY AS "depcitycode",
    C.CITY_KOR AS "depcity",
	A.DOMESTIC_ARRIVAL_CITY AS "arrvcitycode",
	D.CITY_KOR AS "arrvcity"
FROM
    AIRPORT_SCHEDULE_DOME_HIST A,
    AIRPORT_AIRLINE_CODE B,
    AIRPORT_CITY_CODE C,
    AIRPORT_CITY_CODE D
WHERE B.AIRLINE_CODE2=SUBSTR(A.DOMESTIC_NUM,0,2)
AND C.CITY_CODE = A.DOMESTIC_START_CITY
AND D.CITY_CODE = A.DOMESTIC_ARRIVAL_CITY
AND DOMESTIC_START_TIME != 'null'
AND FST IN ('11', '13', '14', '15')
UNION ALL
SELECT
	TO_CHAR (A.DOMESTIC_STDATE, 'YYYYMMDD')||A.DOMESTIC_IDX AS "fid",
	'I' AS "fgenType",
	to_char (A.DOMESTIC_REGDATE , 'YYYYMMDDHH24MISS') AS "fgentime",
    A.DOMESTIC_NUM AS "flightid",
    A.DOMESTIC_START_TIME AS "st",
    to_char(A.DOMESTIC_STDATE, 'YYYYMMDD') AS "firstdate",
    to_char(A.DOMESTIC_EDDATE, 'YYYYMMDD') AS "lastdate",
    A.DOMESTIC_MON AS "ynmon",
    A.DOMESTIC_TUE AS "yntue",
    A.DOMESTIC_WED AS "ynwed",
    A.DOMESTIC_THU AS "ynthu",
    A.DOMESTIC_FRI AS "ynfri",
    A.DOMESTIC_SAT AS "ynsat",
    A.DOMESTIC_SUN AS "ynsun",
    B.AIRLINE_KOREAN AS "airline",
    B.AIRLINE_CODE2 AS "airlineCode",
    A.DOMESTIC_START_CITY AS "depcitycode",
    C.CITY_KOR AS "depcity",
	A.DOMESTIC_ARRIVAL_CITY AS "arrvcitycode",
	D.CITY_KOR AS "arrvcity"
FROM
    AIRPORT_SCHEDULE_DOME A,
    AIRPORT_AIRLINE_CODE B,
    AIRPORT_CITY_CODE C,
    AIRPORT_CITY_CODE D
WHERE B.AIRLINE_CODE2=SUBSTR(A.DOMESTIC_NUM,0,2)
AND C.CITY_CODE = A.DOMESTIC_START_CITY
AND D.CITY_CODE = A.DOMESTIC_ARRIVAL_CITY
AND DOMESTIC_START_TIME != 'null'
AND FST IN ('11', '13', '14', '15')
AND to_char(A.DOMESTIC_STDATE, 'YYYYMMDD') <= SYSDATE
AND to_char(A.DOMESTIC_EDDATE, 'YYYYMMDD') >= SYSDATE)
WHERE 1=1
-- [동적 조건] fid         → AND "fid" = ?
--             fgenTime    → AND "fgentime" >= ?
--             flightId    → AND "flightid" = UPPER(?)
--             depCityCode → AND "depcitycode" = UPPER(?)
--             depCity     → AND "depcity" LIKE '%'||?||'%'
--             arrvCityCode→ AND "arrvcitycode" = UPPER(?)
--             arrvCity    → AND "arrvcity" LIKE '%'||?||'%'
--             fgenType    → AND "fgenType" = UPPER(?)
--             schAirLine  → AND "airlineCode" = UPPER(?)
ORDER BY "fgentime" desc

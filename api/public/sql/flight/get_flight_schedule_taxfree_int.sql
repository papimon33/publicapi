-- API: GET /flight/schedule/taxfree-int
SELECT *
FROM
(SELECT
	TO_CHAR (A.INTERNATIONAL_STDATE , 'YYYYMMDD')||A.INTERNATIONAL_IDX AS "fid",
	A.CRUD_TP_CD AS "fgenType",
	to_char (A.INTERNATIONAL_REGDATE , 'YYYYMMDDHH24MISS') AS "fgentime",
    A.INTERNATIONAL_NUM AS "flightid",
    A.INTERNATIONAL_TIME AS "st",
    to_char(A.INTERNATIONAL_STDATE, 'YYYYMMDD') AS "firstdate",
    to_char(A.INTERNATIONAL_EDDATE, 'YYYYMMDD') AS "lastdate",
    A.INTERNATIONAL_MON AS "ynmon",
    A.INTERNATIONAL_TUE AS "yntue",
    A.INTERNATIONAL_WED AS "ynwed",
    A.INTERNATIONAL_THU AS "ynthu",
    A.INTERNATIONAL_FRI AS "ynfri",
    A.INTERNATIONAL_SAT AS "ynsat",
    A.INTERNATIONAL_SUN AS "ynsun",
    B.AIRLINE_KOREAN AS "airline",
    B.AIRLINE_CODE2 AS "airlinecode",
    A.INTERNATIONAL_AIRPORT_DOME AS "depcitycode",
    (SELECT CITY_KOR FROM AIRPORT_CITY_CODE WHERE CITY_CODE = A.INTERNATIONAL_AIRPORT_DOME) AS "depcity",
    A.INTERNATIONAL_AIRPORT_INTE AS "arrvcitycode",
    (SELECT CITY_KOR FROM AIRPORT_CITY_CODE WHERE CITY_CODE = A.INTERNATIONAL_AIRPORT_INTE) AS "arrvcity"
FROM
    AIRPORT_SCHEDULE_INTE_HIST A,
    AIRPORT_AIRLINE_CODE B
WHERE B.AIRLINE_CODE2=SUBSTR(A.INTERNATIONAL_NUM,0,2)
AND INTERNATIONAL_TIME != 'null'
AND FST IN ('11', '13', '14', '15')
AND INTERNATIONAL_AIRPORT_DOME NOT IN 'ICN' and INTERNATIONAL_AIRPORT_INTE NOT in 'ICN')
WHERE 1=1
-- [동적 조건] fid         → AND "fid" = ?
--             fgenTime    → AND "fgentime" >= ?
--             flightId    → AND "flightid" = UPPER(?)
--             depCityCode → AND "depcitycode" = UPPER(?)
--             depCity     → AND "depcity" LIKE '%'||?||'%'
--             arrvCityCode→ AND "arrvcitycode" = UPPER(?)
--             arrvCity    → AND "arrvcity" LIKE '%'||?||'%'
--             fgenType    → AND "fgenType" = UPPER(?)
--             schAirLine  → AND "airlinecode" = UPPER(?)
ORDER BY "fgentime" ASC

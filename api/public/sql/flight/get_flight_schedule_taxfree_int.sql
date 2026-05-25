-- API: GET /flight/schedule/taxfree-int
SELECT *
FROM
(SELECT 
	TO_CHAR (A.INTERNATIONAL_STDATE , 'YYYYMMDD')||A.INTERNATIONAL_IDX AS fid,
	A.CRUD_TP_CD AS fgenType,
	to_char (A.INTERNATIONAL_REGDATE , 'YYYYMMDDHH24MISS') AS fgenTime,
    A.INTERNATIONAL_NUM AS flightId, 
    A.INTERNATIONAL_TIME AS st, 
    to_char(A.INTERNATIONAL_STDATE, 'YYYYMMDD') AS firstdate, 
    to_char(A.INTERNATIONAL_EDDATE, 'YYYYMMDD') AS lastdate,  
    A.INTERNATIONAL_MON AS ynMon, 
    A.INTERNATIONAL_TUE AS ynTue, 
    A.INTERNATIONAL_WED AS ynWed, 
    A.INTERNATIONAL_THU AS ynThu, 
    A.INTERNATIONAL_FRI AS ynFri, 
    A.INTERNATIONAL_SAT AS ynSat, 
    A.INTERNATIONAL_SUN AS ynSun, 
    B.AIRLINE_KOREAN AS airline,
    B.AIRLINE_CODE2 AS airlinecode, 
    A.INTERNATIONAL_AIRPORT_DOME AS depCityCode,
    (SELECT CITY_KOR FROM AIRPORT_CITY_CODE WHERE CITY_CODE = A.INTERNATIONAL_AIRPORT_DOME) AS depCity,
    A.INTERNATIONAL_AIRPORT_INTE AS arrvCityCode,
    (SELECT CITY_KOR FROM AIRPORT_CITY_CODE WHERE CITY_CODE = A.INTERNATIONAL_AIRPORT_INTE) AS arrvCity	
FROM 
    AIRPORT_SCHEDULE_INTE_HIST A,
    AIRPORT_AIRLINE_CODE B
WHERE B.AIRLINE_CODE2=SUBSTR(A.INTERNATIONAL_NUM,0,2) 
AND INTERNATIONAL_TIME != 'null' 
AND FST IN ('11', '13', '14', '15') 
AND INTERNATIONAL_AIRPORT_DOME NOT IN 'ICN' and INTERNATIONAL_AIRPORT_INTE NOT in 'ICN')
WHERE 1=1
-- [동적 조건] fid         → AND FID = ?
--             fgenTime    → AND fgenTime >= ?
--             flightId    → AND flightId = UPPER(?)
--             depCityCode → AND depCityCode = UPPER(?)
--             depCity     → AND depCity LIKE '%'||?||'%'
--             arrvCityCode→ AND arrvCityCode = UPPER(?)
--             arrvCity    → AND arrvCity LIKE '%'||?||'%'
--             fgenType    → AND fgenType = UPPER(?)
--             schAirLine  → AND airlinecode = UPPER(?)
ORDER BY fgenTime ASC
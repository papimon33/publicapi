SELECT *
FROM (
SELECT
    T1.FID AS "fid",
    TO_CHAR(CASE WHEN (T1.MARK='I' AND T1.DEL='N') THEN T1.ACT_DATE
         ELSE T1.MOD_DATE
         END,'YYYYMMDDHH24MISS') AS "fgentime",
    DECODE(T1.DEL,'N',T1.MARK,'Y','D') AS "fgenType",
    T2.AIRLINE_KOREAN AS "airline",
    CASE WHEN T1.IO = 'O' THEN (SELECT CITY_CODE FROM AIRPORT_CITY_CODE CITYCODE WHERE CITYCODE.CITY_CODE = T1.AIRPORT )
         WHEN T1.IO = 'I' THEN (SELECT CITY_CODE FROM AIRPORT_CITY_CODE CITYCODE WHERE CITYCODE.CITY_CODE = T1.CITY)  END AS "depairportcode",
    CASE WHEN T1.IO = 'O' THEN (SELECT CITY_KOR FROM AIRPORT_CITY_CODE CITYCODE WHERE CITYCODE.CITY_CODE = T1.AIRPORT )
         WHEN T1.IO = 'I' THEN (SELECT CITY_KOR FROM AIRPORT_CITY_CODE CITYCODE WHERE CITYCODE.CITY_CODE = T1.CITY)  END AS "depairport",
    CASE WHEN T1.IO = 'O' THEN (SELECT CITY_CODE FROM AIRPORT_CITY_CODE CITYCODE WHERE CITYCODE.CITY_CODE = T1.CITY)
         WHEN T1.IO = 'I' THEN (SELECT CITY_CODE FROM AIRPORT_CITY_CODE CITYCODE WHERE CITYCODE.CITY_CODE = T1.AIRPORT) END AS "arrvairportcode",
    CASE WHEN T1.IO = 'O' THEN (SELECT CITY_KOR FROM AIRPORT_CITY_CODE CITYCODE WHERE CITYCODE.CITY_CODE = T1.CITY)
         WHEN T1.IO = 'I' THEN (SELECT CITY_KOR FROM AIRPORT_CITY_CODE CITYCODE WHERE CITYCODE.CITY_CODE = T1.AIRPORT) END AS "arrvairport",
    T1.CDSR_YN AS "codeshare",
    T1.CDSR_MST_FL_NM AS "masterflightid",
    T2.AIRLINE_CODE2||T1.FLN AS "flightid",
    T1.ACT_C_DATE||T1.STD AS "scheduledatetime",
    CASE WHEN T1.ETD IS NULL THEN T1.ACT_C_DATE||T1.STD WHEN T1.ETD IS NOT NULL THEN T1.ACT_C_DATE||T1.ETD END AS "estimateddatetime",
    T1.IO AS "io",
    CASE WHEN T1.LINE = 'D' THEN '국내' WHEN T1.LINE = 'I' THEN '국제' END AS "line"
FROM
    AIRPORT_FIDS_SCHEDULE T1 LEFT JOIN AIRPORT_AIRLINE_CODE T2 ON T1.ICAO = T2.AIRLINE_CODE3 AND T1.IATA = T2.AIRLINE_CODE2
    LEFT JOIN FIDS_STATUS T3 ON T1.RMK = T3.RMK_CODE
WHERE T1.FST IN ('11', '13', '15') AND T1.PPC IN ('00', '08') AND (T1.DEL != 'Y' OR (T1.DEL='Y' AND T1.RMK='SNL'))
  AND T1.ACT_C_DATE||T1.STD BETWEEN TO_CHAR(SYSDATE-3, 'YYYYMMDD') AND TO_CHAR(SYSDATE+7, 'YYYYMMDD')
)
WHERE 1=1
-- [동적 조건] searchDate   → AND SUBSTR("scheduledatetime",1,8) = ?
--             searchFrom   → AND SUBSTR("scheduledatetime",9,4) >= ?
--             searchTo     → AND SUBSTR("scheduledatetime",9,4) <= ?
--             fid          → AND "fid" = ?
--             flightId     → AND "flightid" = UPPER(?)
--             depCityCode  → AND "depairportcode" = UPPER(?)
--             depCity      → AND "depairport" LIKE '%'||?||'%'
--             arrvCityCode → AND "arrvairportcode" = UPPER(?)
--             arrvCity     → AND "arrvairport" LIKE '%'||?||'%'
--             fgenType     → AND "fgenType" = UPPER(?)
--             fgenTime     → AND "fgentime" >= ?
ORDER BY "estimateddatetime" ASC

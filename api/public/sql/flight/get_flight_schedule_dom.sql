-- API: GET /flight/schedule/dom
SELECT 
    A.DOMESTIC_NUM          AS "domesticNum",
    A.DOMESTIC_START_TIME   AS "domesticStartTime",
    A.DOMESTIC_ARRIVAL_TIME AS "domesticArrivalTime",
    A.DOMESTIC_MON          AS "domesticMon",
    A.DOMESTIC_TUE          AS "domesticTue",
    A.DOMESTIC_WED          AS "domesticWed",
    A.DOMESTIC_THU          AS "domesticThu",
    A.DOMESTIC_FRI          AS "domesticFri",
    A.DOMESTIC_SAT          AS "domesticSat",
    A.DOMESTIC_SUN          AS "domesticSun",
    A.DOMESTIC_STDATE       AS "domesticStdate",
    A.DOMESTIC_EDDATE       AS "domesticEddate",
    B.AIRLINE_KOREAN        AS "airlineKorean",
    B.AIRLINE_ENGLISH       AS "airlineEnglish",
    B.AIRLINE_HOMEPAGE_URL  AS "airlinehomepageUrl",
    A.DOMESTIC_START_CITY   AS "startcityCode",
    (SELECT CITY_KOR FROM AIRPORT_CITY_CODE WHERE CITY_CODE = A.DOMESTIC_START_CITY) AS "startcity",
    A.DOMESTIC_ARRIVAL_CITY AS "arrivalcityCode",
    (SELECT CITY_KOR FROM AIRPORT_CITY_CODE WHERE CITY_CODE = A.DOMESTIC_ARRIVAL_CITY) AS "arrivalcity",
    CASE WHEN FST IN ('11', '13', '14', '15') THEN '여객기'
         WHEN FST IN ('21', '22', '23') THEN '화물기'
         ELSE '기타' END AS "flightPurpose"
FROM 
    AIRPORT_SCHEDULE_DOME A, 
    AIRPORT_AIRLINE_CODE B
WHERE B.AIRLINE_CODE2=SUBSTR(A.DOMESTIC_NUM,0,2) and FST != '12'
-- [동적 조건] schDate         → AND TO_CHAR(DOMESTIC_STDATE,'yyyymmdd') <= ?
--             schDate         → AND TO_CHAR(DOMESTIC_EDDATE,'yyyymmdd') >= ?
--             schDeptCityCode → AND A.DOMESTIC_START_CITY = ?
--             schArrvCityCode → AND A.DOMESTIC_ARRIVAL_CITY = ?
--             schAirLine      → AND SUBSTR(DOMESTIC_NUM,0,2) = ?
--             schFlightNum    → AND DOMESTIC_NUM LIKE '%'||?||'%'
ORDER BY A.DOMESTIC_START_TIME ASC
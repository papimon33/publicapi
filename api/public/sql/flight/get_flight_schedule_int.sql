-- API: GET /flight/schedule/int
SELECT
    A.INTERNATIONAL_IO_TYPE    AS "internationalIoType",
    A.INTERNATIONAL_NUM        AS "internationalNum",
    A.INTERNATIONAL_TIME       AS "internationalTime",
    A.INTERNATIONAL_MON        AS "internationalMon",
    A.INTERNATIONAL_TUE        AS "internationalTue",
    A.INTERNATIONAL_WED        AS "internationalWed",
    A.INTERNATIONAL_THU        AS "internationalThu",
    A.INTERNATIONAL_FRI        AS "internationalFri",
    A.INTERNATIONAL_SAT        AS "internationalSat",
    A.INTERNATIONAL_SUN        AS "internationalSun",
    A.INTERNATIONAL_STDATE     AS "internationalStdate",
    A.INTERNATIONAL_EDDATE     AS "internationalEddate",
    B.AIRLINE_KOREAN           AS "airlineKorean",
    B.AIRLINE_ENGLISH          AS "airlineEnglish",
    B.AIRLINE_HOMEPAGE_URL     AS "airlinehomepageUrl",
    A.INTERNATIONAL_AIRPORT_DOME AS "airportCode",
    (SELECT CITY_KOR FROM AIRPORT_CITY_CODE WHERE CITY_CODE = A.INTERNATIONAL_AIRPORT_DOME) AS "airport",
    A.INTERNATIONAL_AIRPORT_INTE AS "cityCode",
    (SELECT CITY_KOR FROM AIRPORT_CITY_CODE WHERE CITY_CODE = A.INTERNATIONAL_AIRPORT_INTE) AS "city",
    CASE WHEN FST IN ('11', '13', '14', '15') THEN '여객기'
         WHEN FST IN ('21', '22', '23') THEN '화물기'
         ELSE '기타' END AS "flightPurpose"
FROM
    AIRPORT_SCHEDULE_INTE A,
    AIRPORT_AIRLINE_CODE B
WHERE B.AIRLINE_CODE2=SUBSTR(A.INTERNATIONAL_NUM,0,2) AND INTERNATIONAL_TIME != 'null' AND FST != '12'
-- [동적 조건] schDate         → AND TO_CHAR(INTERNATIONAL_STDATE,'yyyymmdd') <= ?
--             schDate         → AND TO_CHAR(INTERNATIONAL_EDDATE,'yyyymmdd') >= ?
--             schDeptCityCode → AND DECODE(A.INTERNATIONAL_IO_TYPE,'IN',A.INTERNATIONAL_AIRPORT_INTE,A.INTERNATIONAL_AIRPORT_DOME) = UPPER(?)
--             schArrvCityCode → AND DECODE(A.INTERNATIONAL_IO_TYPE,'IN',A.INTERNATIONAL_AIRPORT_DOME,A.INTERNATIONAL_AIRPORT_INTE) = UPPER(?)
--             schAirLine      → AND SUBSTR(INTERNATIONAL_NUM,0,2) = ?
--             schFlightNum    → AND UPPER(INTERNATIONAL_NUM) LIKE '%'||?||'%'
ORDER BY A.INTERNATIONAL_TIME ASC
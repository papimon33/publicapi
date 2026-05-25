-- API: GET /airport/bus/info
SELECT
    REPLACE(REPLACE(REPLACE(REPLACE(a.BUS_CATEGORY_KOR_NAME,'<br/>',''),'<br>',''),'</br>',''),'<bold>','')                             AS BUS_CATEGORY_KOR_NAME,
    REPLACE(REPLACE(REPLACE(REPLACE(b.BUS_DATA_GETON_KOR,'<br/>',''),'<br>',''),'</br>',''),'<bold>','')                                AS BUS_DATA_GETON_KOR   ,
    REPLACE(REPLACE(REPLACE(REPLACE(b.BUS_DATA_BUS_NUM,'<br/>',''),'<br>',''),'</br>',''),'<bold>','')                                  AS BUS_DATA_BUS_NUM     ,
    REPLACE(REPLACE(REPLACE(REPLACE(b.BUS_DATA_MONEY,'<br/>',''),'<br>',''),'</br>',''),'<bold>','')                                    AS BUS_DATA_MONEY       ,
    REPLACE(REPLACE(REPLACE(REPLACE(b.BUS_DATA_CARD,'<br/>',''),'<br>',''),'</br>',''),'<bold>','')                                     AS BUS_DATA_CARD        ,
    REPLACE(REPLACE(REPLACE(REPLACE(TO_NCHAR (SUBSTR (b.BUS_DATA_ROUTE_KOR, 0, 2000)),'<br/>',''),'<br>',''),'</br>',''),'<bold>','')   AS BUS_DATA_ROUTE_KOR   ,
    REPLACE(REPLACE(REPLACE(REPLACE(BUS_DATA_FIRST_TIME || ':' || BUS_DATA_FIRST_MINUTE,'<br/>',''),'<br>',''),'</br>',''),'<bold>','') AS BUS_DATA_FIRST_TIME  ,
    REPLACE(REPLACE(REPLACE(REPLACE(BUS_DATA_END_TIME || ':' || BUS_DATA_END_MINUTE,'<br/>',''),'<br>',''),'</br>',''),'<bold>','')     AS BUS_DATA_END_TIME    ,
    REPLACE(REPLACE(REPLACE(REPLACE(b.BUS_DATA_COMNAME_KOR,'<br/>',''),'<br>',''),'</br>',''),'<bold>','')                              AS BUS_DATA_COMNAME_KOR ,
    REPLACE(REPLACE(REPLACE(REPLACE(TO_NCHAR (SUBSTR (b.BUS_DATA_ETC_KOR, 0, 2000)),'<br/>',''),'<br>',''),'</br>',''),'<bold>','')     AS BUS_DATA_ETC_KOR
FROM
    kacweb2.AIRPORT_BUS_CATEGORY a,
    kacweb2.AIRPORT_BUS_DATA     b,
    kacweb2.SITE_INFO            c
WHERE
    a.BUS_CATEGORY_IDX  = b.BUS_DATA_CATEGORY_IDX
AND b.BUS_DATA_SITE_IDX = c.LOGIN_STR
-- [동적 조건] schAirport → AND c.SITE_NAME2 = UPPER(?)
order by
    BUS_CATEGORY_KOR_NAME,
    BUS_DATA_BUS_NUM asc
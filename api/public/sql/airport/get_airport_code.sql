SELECT
    CITY_CODE,
    CITY_KOR ,
    CITY_ENG ,
    CITY_JPN ,
    CITY_CHN
FROM
    AIRPORT_CITY_CODE
WHERE
    1 = 1
    -- [동적 조건] cityCode → AND CITY_CODE = ?
    --             cityKor  → AND CITY_KOR = ?
    --             cityEng  → AND CITY_ENG = ?
    --             cityJpn  → AND CITY_JPN = ?
    --             cityChn  → AND CITY_CHN = ?
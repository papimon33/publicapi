-- API: GET /airport/code/info
SELECT
    CITY_CODE  AS "cityCode",
    CITY_KOR   AS "cityKorean",
    CITY_ENG   AS "cityEnglish",
    CITY_JPN   AS "cityJapan",
    CITY_CHN   AS "cityChina"
FROM
    AIRPORT_CITY_CODE
WHERE
    1 = 1
    -- [동적 조건] cityCode → AND CITY_CODE = ?
    --             cityKor  → AND CITY_KOR = ?
    --             cityEng  → AND CITY_ENG = ?
    --             cityJpn  → AND CITY_JPN = ?
    --             cityChn  → AND CITY_CHN = ?
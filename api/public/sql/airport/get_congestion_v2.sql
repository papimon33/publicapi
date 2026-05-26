-- API: GET /airport/congestion/v2
SELECT
    IATA_APCD,
    PRC_HR,
    CGDR_A_LVL,
    CGDR_B_LVL,
    CGDR_C_LVL,
    CGDR_ALL_LVL
FROM M_WT_CGDR_LST
WHERE 1=1
-- [동적 조건] schAirportCode → AND IATA_APCD = ?
ORDER BY PRC_HR ASC

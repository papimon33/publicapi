-- ============================================================
-- 프로젝트에서 사용하는 모든 테이블의 컬럼 정보 조회
-- Oracle ALL_TAB_COLUMNS 기준
-- ============================================================
SELECT
    OWNER,
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE,
    DATA_LENGTH,
    DATA_PRECISION,
    DATA_SCALE,
    NULLABLE,
    COLUMN_ID
FROM ALL_TAB_COLUMNS
WHERE (OWNER, TABLE_NAME) IN (
    -- airport
    (USER, 'AIRPORT_CITY_CODE'),
    (USER, 'AIRPORT_DAILY_EXPECT'),
    (USER, 'AIRPORT_T'),
    (USER, 'ORDER_T'),
    (USER, 'CMS_LEASE_CONTRACT_STATUS'),
    (USER, 'CMS_CMN_CODE'),
    (USER, 'AIRPORT_LOW_VISIBLITY'),
    (USER, 'W_FY_CONGESTION_TAXI_SSIJ_RCV'),
    -- airport (kacweb2 schema)
    ('KACWEB2', 'AIRPORT_BUS_CATEGORY'),
    ('KACWEB2', 'AIRPORT_BUS_DATA'),
    ('KACWEB2', 'SITE_INFO'),
    ('KACWEB2', 'AIRPORT_PARKING'),
    -- epi_gh
    ('NGHG_KAC', 'TB_GHG_EM_STAT'),
    -- flight
    (USER, 'AIRPORT_FIDS_SCHEDULE'),
    (USER, 'AIRPORT_AIRLINE_CODE'),
    (USER, 'FIDS_STATUS'),
    (USER, 'AIRPORT_SCHEDULE_DOME'),
    (USER, 'AIRPORT_SCHEDULE_DOME_HIST'),
    (USER, 'AIRPORT_SCHEDULE_INTE'),
    (USER, 'AIRPORT_SCHEDULE_INTE_HIST'),
    (USER, 'AIRPORT_CPAIR'),
    -- noise
    (USER, 'T_NS_MONTH_WECP'),
    (USER, 'TL_NS_MSRSTN'),
    (USER, 'SI_NOISE_MASTER'),
    -- parking
    (USER, 'AIRPORT_PARKINGLIVE'),
    (USER, 'W_PARK_GMP_VALET'),
    (USER, 'VW_PARKING_CELL')
)
ORDER BY OWNER, TABLE_NAME, COLUMN_ID;

-- API: GET /airport/taxi-wait/cju
SELECT 
    PRC_DTM       AS "prcdtm",
    WIT_TAXI_CT   AS "witTaxiCT",
    WIT_PAX_CT    AS "witPaxCT",
    XPT_BDG_MI    AS "xptBdgMi"
FROM W_FY_CONGESTION_TAXI_SSIJ_RCV
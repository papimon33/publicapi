-- API: GET /parking/valet-congestion/gmp-dom
SELECT CRT_DT   AS "crtDt",
CRT_TIME AS "crtTime",
CAM1     AS "cam1",
CAM2     AS "cam2",
CAM3     AS "cam3",
TOTAL    AS "total",
CASE WHEN cam3 <= 7 THEN '여유(원활)'
     WHEN cam3 = 8 THEN '혼잡(정체)'
     WHEN cam3 >= 9 THEN '만차'
     END AS "cdgr"
FROM W_PARK_GMP_VALET
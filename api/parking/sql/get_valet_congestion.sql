SELECT CRT_DT ,
CRT_TIME ,
CAM1 ,
CAM2 ,
CAM3 ,
TOTAL ,
CASE WHEN cam3 <= 7 THEN '여유(원활)'
     WHEN cam3 = 8 THEN '혼잡(정체)'
     WHEN cam3 >= 9 THEN '만차'
     END AS CDGR
FROM W_PARK_GMP_VALET
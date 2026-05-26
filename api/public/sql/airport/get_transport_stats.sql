-- API: GET /airport/transport-stats/info
SELECT 
    DECODE(OD.KOR_N, '', AP.A_AIRPORT, OD.KOR_N)        AS "Airport"        ,
    IOC                                                 AS "Arrflgt"        ,
    OOC                                                 AS "depflgtn"       ,
    SUBOC                                               AS "Subflgt"        ,
    ArrPassenger                                        AS "Arrpassenger"   ,
    DepPassenger                                        AS "Deppassenger"   ,
    TotalPassenger                                      AS "subpassenger"   ,
    ArrCargo                                            AS "Arrcargo"       ,
    DepCargo                                            AS "Depcargo"       ,
    TotalCargo                                          AS "subcargo"
FROM 
(
    SELECT 
        A_AIRPORT, 
        SUM(A_IOC)IOC, 
        SUM(A_OOC) OOC, 
        SUM(A_IOC+ A_OOC) SUBOC, 
        SUM(ArrPassenger) ArrPassenger, 
        SUM(DepPassenger) DepPassenger, 
        SUM(ArrPassenger+ DepPassenger) TotalPassenger, 
        SUM(ArrCargo) ArrCargo, 
        SUM(DepCargo) DepCargo, 
        SUM(ArrCargo+ DepCargo) TotalCargo 
    FROM 
   ( 
        SELECT 
            A_AIRPORT, 
            SUM(A_OC) A_IOC, 0 A_OOC, 
            DECODE(?, '0', SUM(A_FP + A_TS), '1', SUM(A_NP), SUM(A_FP + A_TS+A_NP)) ArrPassenger, 0 DepPassenger, 
            DECODE(?, '0', SUM(A_FF), '1',SUM(A_BF), '2', SUM(A_MF), '3', SUM(A_FF + A_MF), SUM(A_FF + A_BF + A_MF)) ArrCargo, 0 DepCargo 
        FROM AIRPORT_T 
        WHERE A_YYYYMM BETWEEN DECODE(?, '', TO_CHAR(SYSDATE, 'YYYYMM'), ?)  AND DECODE(?, '', TO_CHAR(SYSDATE, 'YYYYMM'), ?)
            AND A_IO = 'I' 
            AND A_AIRPORT = ?
        GROUP BY A_AIRPORT 
        UNION ALL 
        SELECT 
            A_AIRPORT, 
            0 A_IOC, SUM(A_OC) A_OOC, 
            0 ArrPassenger, DECODE(?, '0', SUM(A_FP + A_TS), '1', SUM(A_NP), SUM(A_FP + A_TS+A_NP)) DepPassenger, 
            0 ArrCargo, DECODE(?, '0', SUM(A_FF), '1',SUM(A_BF), '2', SUM(A_MF), '3', SUM(A_FF + A_MF), 
            SUM(A_FF + A_BF + A_MF)) DepCargo 
        FROM AIRPORT_T 
        WHERE A_YYYYMM BETWEEN DECODE(?, '', TO_CHAR(SYSDATE, 'YYYYMM'), ?)  AND DECODE(?, '', TO_CHAR(SYSDATE, 'YYYYMM'), ?)
            AND A_IO = 'O' 
            AND A_AIRPORT = ?
        GROUP BY A_AIRPORT 
    )
    GROUP BY A_AIRPORT
)AP, ORDER_T OD
WHERE AP.A_AIRPORT = OD.NAME(+)
-- [동적 조건] routeBe       → AND A_LINE = ?
--             pasngrCargoBe → AND A_USE = ?
--             nvgBe         → AND a_REGULAR = ?
-- (base_param: pasngrBe, cargoBe, startDePd, endDePd, airPort 가 서브쿼리 내 ? 에 바인딩)
ORDER BY OD.ORDER_N
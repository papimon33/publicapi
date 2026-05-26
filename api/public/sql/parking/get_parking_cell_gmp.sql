-- API: GET /parking/available-spaces/gmp-int-indoor
SELECT
    CELL_ID      AS "cellId",
    PARKING_NAME AS "parkingName",
    LEVEL_NAME   AS "levelName",
    CELL_NAME    AS "cellName",
    CELL_TYPE    AS "cellType",
    CELL_STATUS  AS "cellStatus",
    UPD_DTTM     AS "updDttm"
FROM VW_PARKING_CELL
ORDER BY UPD_DTTM DESC

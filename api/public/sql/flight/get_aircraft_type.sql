-- API: GET /flight/aircraft-status/info
SELECT 
    CELL_ID         AS cell_id         ,
    PARKING_NAME    AS parking_name    ,
    LEVEL_NAME      AS level_name      ,
    CELL_NAME       AS cell_name       ,
    CELL_TYPE       AS cell_type       ,
    CELL_STATUS     AS cell_status     ,
    CELL_LOCATION   AS cell_location   ,
    UPD_DTTM        AS upd_dttm
FROM VW_PARKING_CELL 
ORDER BY UPD_DTTM DESC
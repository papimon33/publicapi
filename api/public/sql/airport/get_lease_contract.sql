-- API: GET /airport/lease-contract/info
SELECT 
    A.ETP_NM                                AS "storeName",
    CASE
        WHEN A.APCD = 'A1101' THEN 'GMP'
        WHEN A.APCD = 'A1102' THEN 'PUS'
        WHEN A.APCD = 'A1103' THEN 'CJU'
        WHEN A.APCD = 'A1104' THEN 'TAE'
        WHEN A.APCD = 'A1108' THEN 'KWJ'
        WHEN A.APCD = 'A1109' THEN 'RSU'
        WHEN A.APCD = 'A1105' THEN 'USN'
        WHEN A.APCD = 'A1113' THEN 'KUV'
        WHEN A.APCD = 'A1114' THEN 'WJU'
        WHEN A.APCD = 'A1106' THEN 'CJJ'
        WHEN A.APCD = 'A1111' THEN 'YNY'
        WHEN A.APCD = 'A1110' THEN 'KPO'
        WHEN A.APCD = 'A1112' THEN 'HIN'
        WHEN A.APCD = 'A1107' THEN 'MWX'
    END                                     AS "airportCode",
    B.CMN_NAME                              AS "airportName",
    A.LSE_LOC                               AS "leaseLocation",
    A.BZTP_NM                               AS "typeOfBusiness",
    CONCAT(A.LSE_SQM, '㎡')                 AS "space",
    CONCAT(A.LSE_PRICE, '백만원')            AS "rental",
    TO_CHAR(A.LSE_CTR_ST_DT, 'YYYY-MM-DD')  AS "contractStartDate",
    TO_CHAR(A.LSE_CTR_ED_DT, 'YYYY-MM-DD')  AS "contractEndDate",
    CASE
        WHEN TO_CHAR(A.LSE_CTR_ED_DT, 'YYYY-MM-DD') >= TO_CHAR(SYSDATE, 'YYYY-MM-DD') THEN '진행중'
        ELSE '만료'
    END                                     AS "contractStatus"
FROM CMS_LEASE_CONTRACT_STATUS A INNER JOIN CMS_CMN_CODE B ON A.APCD = B.CMN_CODE
WHERE 1=1
    -- [동적 조건] schAirportCode → AND A.APCD = ? (GMP→A1101, PUS→A1102, CJU→A1103 등 코드 변환)
    --             contactStatus  → ON  : AND TO_CHAR(A.LSE_CTR_ED_DT,'YYYY-MM-DD') >= TO_CHAR(SYSDATE,'YYYY-MM-DD')
    --                            → EXP : AND TO_CHAR(SYSDATE,'YYYY-MM-DD') > TO_CHAR(A.LSE_CTR_ED_DT,'YYYY-MM-DD')
ORDER BY A.APCD ASC
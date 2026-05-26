-- API: GET /noise/affected-area/info
SELECT "city1", "city2", "dong", "li", "jibun", "street", "build", "buildno", "hosu", "yn"

FROM ( SELECT
  CASE WHEN ? IS NULL OR ? IS NULL OR ? IS NULL THEN TO_CHAR('검색된 주소가 없습니다.')

ELSE TO_CHAR(CTP_NM)
  END AS "city1",
  CASE WHEN ? IS NULL OR ? IS NULL OR ? IS NULL THEN TO_CHAR('')

ELSE TO_CHAR(SIG_NM)
  END AS "city2",
  CASE WHEN ? IS NULL OR ? IS NULL OR ? IS NULL THEN TO_CHAR('')

ELSE TO_CHAR(HEMD_NM)
  END AS "dong",
  CASE WHEN ? IS NULL OR ? IS NULL OR ? IS NULL THEN TO_CHAR('')

ELSE TO_CHAR(LI_NM)
  END AS "li",
  CASE WHEN ? IS NULL OR ? IS NULL OR ? IS NULL THEN TO_CHAR('')
    ELSE TO_CHAR(DECODE(TO_CHAR(LNBR_SLNO), TO_CHAR('0'), TO_CHAR(LNBR_MNNM), CONCAT(TO_CHAR(LNBR_MNNM), CONCAT('-' , TO_CHAR(LNBR_SLNO)))))

  END AS "jibun",
  CASE WHEN ? IS NULL OR ? IS NULL OR ? IS NULL THEN TO_CHAR('')
    ELSE TO_CHAR(RN)
  END AS "street",
  CASE WHEN ? IS NULL OR ? IS NULL OR ? IS NULL THEN TO_CHAR('')
    ELSE TO_CHAR(BULD_NM)
  END AS "build",
  CASE WHEN ? IS NULL OR ? IS NULL OR ? IS NULL THEN TO_CHAR('')
    ELSE TO_CHAR(DECODE(TO_CHAR(BULD_SLNO), TO_CHAR('0'), TO_CHAR(BULD_MNNM), CONCAT(TO_CHAR(BULD_MNNM), CONCAT('-' , TO_CHAR(BULD_SLNO)))))
  END AS "buildno",
  CASE WHEN ? IS NULL OR ? IS NULL OR ? IS NULL THEN TO_CHAR('')
    ELSE TO_CHAR(BULD_HOSU)
  END AS "hosu",
  CASE WHEN ? IS NULL OR ? IS NULL OR ? IS NULL THEN TO_CHAR('')
    ELSE TO_CHAR('Y')
  END AS "yn",
SOUND_BIZ_AT,
AIR_BIZ_AT,
TV_BIZ_AT,
ELEC_BIZ_AT
FROM SI_NOISE_MASTER T1
WHERE 1=1
    -- [동적 조건] city1   → AND T1.CTP_NM LIKE '%'||?||'%'
    --             city2   → AND T1.SIG_NM LIKE '%'||?||'%'
    --             dong    → AND T1.HEMD_NM LIKE '%'||?||'%'
    --             li      → AND T1.LI_NM LIKE '%'||?||'%'
    --             jibun   → AND TO_CHAR(DECODE(...LNBR_MNNM...)) LIKE '%'||?||'%'
    --             street  → AND T1.RN LIKE '%'||?||'%'
    --             build   → AND T1.BULD_NM LIKE '%'||?||'%'
    --             buildno → AND TO_CHAR(DECODE(...BULD_MNNM...)) LIKE '%'||?||'%'
    --             hosu    → AND T1.BULD_HOSU LIKE '%'||?||'%'
    -- (base_param: city1, city2, dong 가 SELECT 내 CASE WHEN ? IS NULL 에 바인딩)
    
    
    
    
    
    
    
    
    
)
WHERE SOUND_BIZ_AT = 'O' OR AIR_BIZ_AT = 'O' OR TV_BIZ_AT = 'O' OR ELEC_BIZ_AT = 'O'
ORDER BY CITY1, CITY2, DONG, LI, JIBUN, STREET, BUILD, BUILDNO, HOSU ASC
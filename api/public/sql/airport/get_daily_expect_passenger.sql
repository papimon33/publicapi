SELECT 
    ARP,
    AOD,
    SDT,
    HH,
    PCT,
    PCG,
    NVL(TOF,'N') AS TOF,
    CASE WHEN ARP = 'CJU' AND (PCT + PCG) >= 2500 THEN 'Y' 
         WHEN ARP = 'GMP' AND (PCT + PCG) >= 2000 THEN 'Y'
         WHEN ARP = 'PUS' AND (PCT + PCG) >= 1000 THEN 'Y'
         WHEN ARP = 'CJJ' AND (PCT + PCG) >= 500 THEN 'Y'
         WHEN ARP = 'TAE' AND (PCT + PCG) >= 500 THEN 'Y'
         ELSE 'N' 
    END AS CONGEST_YN
FROM AIRPORT_DAILY_EXPECT
WHERE 1 = 1
    -- [동적 조건] schDate    → AND SDT = ?
    --             schAirport → AND ARP = ?
    --             schTof     → AND TOF = ?
    --             schHH      → AND HH = ?
    --             schAOD     → AND AOD = ?
       
       
  
  
  
  
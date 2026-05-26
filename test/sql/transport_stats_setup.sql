-- ============================================================
-- 테스트 테이블 생성 및 샘플 데이터
-- 대상 API : GET /public/airport/transport-stats/info
-- 접속 정보 : system/oracle@localhost:1521/XE
-- ============================================================

-- ────────────────────────────────────────────────
-- 1. 기존 테이블 삭제 (재실행 대비)
-- ────────────────────────────────────────────────
BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE AIRPORT_T';
EXCEPTION WHEN OTHERS THEN NULL;
END;
/

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ORDER_T';
EXCEPTION WHEN OTHERS THEN NULL;
END;
/

-- ────────────────────────────────────────────────
-- 2. AIRPORT_T 생성
--    A_IO     : I(입항/도착) / O(출항/출발)
--    A_LINE   : N(국내) / I(국제)  → routeBe 파라미터
--    A_USE    : 1(여객) / 2(화물)  → pasngrCargoBe 파라미터
--    A_REGULAR: Y(정기) / N(부정기) → nvgBe 파라미터
--    A_OC     : 운항횟수
--    A_FP     : 유임여객
--    A_TS     : 환승여객
--    A_NP     : 무임여객
--    A_FF     : 국제화물
--    A_BF     : 수화물
--    A_MF     : 우편물
-- ────────────────────────────────────────────────
CREATE TABLE AIRPORT_T (
    A_AIRPORT   VARCHAR2(10)    NOT NULL,   -- 공항코드 (GMP, ICN, CJU ...)
    A_YYYYMM    VARCHAR2(6)     NOT NULL,   -- 연월 (YYYYMM)
    A_IO        CHAR(1)         NOT NULL,   -- I:입항 / O:출항
    A_LINE      CHAR(1)         NOT NULL,   -- N:국내 / I:국제
    A_USE       CHAR(1)         NOT NULL,   -- 1:여객 / 2:화물
    A_REGULAR   CHAR(1)         NOT NULL,   -- Y:정기 / N:부정기
    A_OC        NUMBER(10)      DEFAULT 0,  -- 운항횟수
    A_FP        NUMBER(15)      DEFAULT 0,  -- 유임여객
    A_TS        NUMBER(15)      DEFAULT 0,  -- 환승여객
    A_NP        NUMBER(15)      DEFAULT 0,  -- 무임여객
    A_FF        NUMBER(15)      DEFAULT 0,  -- 국제화물(kg)
    A_BF        NUMBER(15)      DEFAULT 0,  -- 수화물(kg)
    A_MF        NUMBER(15)      DEFAULT 0   -- 우편물(kg)
);

-- ────────────────────────────────────────────────
-- 3. ORDER_T 생성 (공항명 한글 매핑 + 정렬 순서)
-- ────────────────────────────────────────────────
CREATE TABLE ORDER_T (
    NAME        VARCHAR2(10)    NOT NULL,   -- AIRPORT_T.A_AIRPORT 와 JOIN
    KOR_N       VARCHAR2(50),              -- 공항 한글명
    ORDER_N     NUMBER(5)                  -- 정렬 순서
);

-- ────────────────────────────────────────────────
-- 4. ORDER_T 샘플 데이터
-- ────────────────────────────────────────────────
INSERT INTO ORDER_T VALUES ('GMP', '김포공항',   1);
INSERT INTO ORDER_T VALUES ('ICN', '인천공항',   2);
INSERT INTO ORDER_T VALUES ('CJU', '제주공항',   3);
INSERT INTO ORDER_T VALUES ('PUS', '김해공항',   4);
INSERT INTO ORDER_T VALUES ('TAE', '대구공항',   5);
INSERT INTO ORDER_T VALUES ('KWJ', '광주공항',   6);
INSERT INTO ORDER_T VALUES ('CJJ', '청주공항',   7);
INSERT INTO ORDER_T VALUES ('RSU', '여수공항',   8);
INSERT INTO ORDER_T VALUES ('USN', '울산공항',   9);
INSERT INTO ORDER_T VALUES ('YNY', '양양공항',  10);

-- ────────────────────────────────────────────────
-- 5. AIRPORT_T 샘플 데이터 (2025년 1~3월, 주요 공항)
--    각 공항 × 입/출항 × 국내/국제 × 여객/화물 × 정기/부정기 조합
-- ────────────────────────────────────────────────

-- GMP 국내여객 정기 입항
INSERT INTO AIRPORT_T VALUES ('GMP','202501','I','N','1','Y', 1200, 85000, 3500, 1200, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('GMP','202502','I','N','1','Y', 1150, 80000, 3200, 1100, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('GMP','202503','I','N','1','Y', 1300, 92000, 3800, 1300, 0, 0, 0);
-- GMP 국내여객 정기 출항
INSERT INTO AIRPORT_T VALUES ('GMP','202501','O','N','1','Y', 1210, 84000, 3400, 1150, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('GMP','202502','O','N','1','Y', 1160, 79000, 3100, 1050, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('GMP','202503','O','N','1','Y', 1310, 91000, 3700, 1250, 0, 0, 0);
-- GMP 국제여객 정기 입항
INSERT INTO AIRPORT_T VALUES ('GMP','202501','I','I','1','Y',  420, 45000, 2800,  800,  50000,  30000, 500);
INSERT INTO AIRPORT_T VALUES ('GMP','202502','I','I','1','Y',  390, 42000, 2600,  750,  48000,  28000, 480);
INSERT INTO AIRPORT_T VALUES ('GMP','202503','I','I','1','Y',  450, 50000, 3100,  900,  55000,  32000, 520);
-- GMP 국제여객 정기 출항
INSERT INTO AIRPORT_T VALUES ('GMP','202501','O','I','1','Y',  418, 44500, 2750,  790,  49000,  29000, 490);
INSERT INTO AIRPORT_T VALUES ('GMP','202502','O','I','1','Y',  388, 41500, 2550,  740,  47000,  27000, 470);
INSERT INTO AIRPORT_T VALUES ('GMP','202503','O','I','1','Y',  448, 49500, 3050,  890,  54000,  31000, 510);

-- ICN 국제여객 정기 입항
INSERT INTO AIRPORT_T VALUES ('ICN','202501','I','I','1','Y', 3500,420000,25000, 8000,1200000, 800000, 15000);
INSERT INTO AIRPORT_T VALUES ('ICN','202502','I','I','1','Y', 3300,400000,23000, 7500,1150000, 780000, 14000);
INSERT INTO AIRPORT_T VALUES ('ICN','202503','I','I','1','Y', 3700,450000,27000, 8500,1280000, 850000, 16000);
-- ICN 국제여객 정기 출항
INSERT INTO AIRPORT_T VALUES ('ICN','202501','O','I','1','Y', 3520,418000,24500, 7900,1190000, 790000, 14800);
INSERT INTO AIRPORT_T VALUES ('ICN','202502','O','I','1','Y', 3320,398000,22500, 7400,1140000, 775000, 13800);
INSERT INTO AIRPORT_T VALUES ('ICN','202503','O','I','1','Y', 3720,448000,26500, 8400,1270000, 845000, 15800);
-- ICN 국제화물 정기 입항
INSERT INTO AIRPORT_T VALUES ('ICN','202501','I','I','2','Y',  800,     0,    0,    0,2500000,1800000, 30000);
INSERT INTO AIRPORT_T VALUES ('ICN','202502','I','I','2','Y',  780,     0,    0,    0,2400000,1750000, 29000);
INSERT INTO AIRPORT_T VALUES ('ICN','202503','I','I','2','Y',  850,     0,    0,    0,2650000,1900000, 32000);
-- ICN 국제화물 정기 출항
INSERT INTO AIRPORT_T VALUES ('ICN','202501','O','I','2','Y',  810,     0,    0,    0,2480000,1780000, 29500);
INSERT INTO AIRPORT_T VALUES ('ICN','202502','O','I','2','Y',  790,     0,    0,    0,2380000,1730000, 28500);
INSERT INTO AIRPORT_T VALUES ('ICN','202503','O','I','2','Y',  860,     0,    0,    0,2630000,1880000, 31500);

-- CJU 국내여객 정기 입항
INSERT INTO AIRPORT_T VALUES ('CJU','202501','I','N','1','Y', 2100,180000, 8000, 3000, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('CJU','202502','I','N','1','Y', 2000,170000, 7500, 2800, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('CJU','202503','I','N','1','Y', 2300,200000, 9000, 3300, 0, 0, 0);
-- CJU 국내여객 정기 출항
INSERT INTO AIRPORT_T VALUES ('CJU','202501','O','N','1','Y', 2110,179000, 7900, 2950, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('CJU','202502','O','N','1','Y', 2010,169000, 7400, 2750, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('CJU','202503','O','N','1','Y', 2310,199000, 8900, 3250, 0, 0, 0);
-- CJU 국내여객 부정기 입항
INSERT INTO AIRPORT_T VALUES ('CJU','202501','I','N','1','N',  150, 12000,  500,  200, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('CJU','202502','I','N','1','N',  140, 11000,  480,  190, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('CJU','202503','I','N','1','N',  160, 13000,  520,  210, 0, 0, 0);

-- PUS 국내여객 정기 입항
INSERT INTO AIRPORT_T VALUES ('PUS','202501','I','N','1','Y',  800, 65000, 2800, 1100, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('PUS','202502','I','N','1','Y',  760, 61000, 2600, 1000, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('PUS','202503','I','N','1','Y',  850, 70000, 3000, 1200, 0, 0, 0);
-- PUS 국내여객 정기 출항
INSERT INTO AIRPORT_T VALUES ('PUS','202501','O','N','1','Y',  810, 64500, 2750, 1080, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('PUS','202502','O','N','1','Y',  770, 60500, 2550,  980, 0, 0, 0);
INSERT INTO AIRPORT_T VALUES ('PUS','202503','O','N','1','Y',  860, 69500, 2950, 1180, 0, 0, 0);
-- PUS 국제여객 정기 입항
INSERT INTO AIRPORT_T VALUES ('PUS','202501','I','I','1','Y',  280, 28000, 1800,  500, 80000, 50000, 1000);
INSERT INTO AIRPORT_T VALUES ('PUS','202502','I','I','1','Y',  260, 26000, 1600,  470, 75000, 47000,  950);
INSERT INTO AIRPORT_T VALUES ('PUS','202503','I','I','1','Y',  300, 31000, 2000,  530, 88000, 55000, 1100);
-- PUS 국제여객 정기 출항
INSERT INTO AIRPORT_T VALUES ('PUS','202501','O','I','1','Y',  282, 27500, 1750,  490, 78000, 49000,  980);
INSERT INTO AIRPORT_T VALUES ('PUS','202502','O','I','1','Y',  262, 25500, 1550,  460, 73000, 46000,  930);
INSERT INTO AIRPORT_T VALUES ('PUS','202503','O','I','1','Y',  302, 30500, 1950,  520, 86000, 54000, 1080);

COMMIT;

-- ────────────────────────────────────────────────
-- 6. 결과 확인 쿼리
-- ────────────────────────────────────────────────
SELECT A_AIRPORT, A_IO, A_LINE, A_USE, A_REGULAR, COUNT(*) CNT
FROM AIRPORT_T
GROUP BY A_AIRPORT, A_IO, A_LINE, A_USE, A_REGULAR
ORDER BY A_AIRPORT, A_IO, A_LINE;

-- API: GET /airport/retail-contract/info

/*comment 
홈페이지 DB가 아님
접속정보
시스템명 : prod
DB종류 : oracle
IP : 172.25.4.167
port : 1521
SID : eis
id : hvc
pw : hvc
*/

--query
SELECT
  GTEXT      AS "Gtext",
  NAME1      AS "Name1",
  SANGHO     AS "Sangho",
  CONF_DATE  AS "ConfDate",
  CONT_DATE  AS "ContDate",
  TYPE3_TEXT AS "Type3Text",
  TYPE4_TEXT AS "Type4Text"
  FROM OA_CONTRACTNO


-- 공통 API 파라미터
pageindex integer(default = 1)
perPage integer(default = 10)
returntype string(default = JSON)
    /*API 파라미터*/



-- 공통 리턴 파라미터
page integer
perPage integer
totalCount integer
currentCount integer
matchCount integer

-- 리턴 파라미터
GTEXT  string
NAME1  string
SANGHO  string
CONF_DATE  string
CONT_DATE  string
TYPE3_TEXT  string
TYPE4_TEXT string

-- 리턴
<items>
    <item>
        <confDate>20140101</confDate>
        <contDate>20151231</contDate>
        <gtext>서울지역본부</gtext>
        <name1>롯데리아</name1>
        <sangho>롯데리아</sangho>
        <type3Text>01층</type3Text>
        <type4Text>국내선</ type4Text>				
    </item>
/**
 * 기존 API 비교 매핑 설정
 *
 * newBaseUrl   : 신규(현재) API 서버 주소 (기본값: "http://localhost:8000")
 * legacyBaseUrl : 기존 API 서버 주소 (예: "https://old-api.example.go.kr")
 * endpoints     : { "현재 API 경로": "기존 API 경로" }
 *
 * - 값이 없는 항목은 비교 패널이 표시되지 않습니다.
 * - 파라미터는 현재 API와 동일한 값이 그대로 전달됩니다.
 *   파라미터 이름이 기존 API와 다를 경우 paramMap을 사용하세요.
 *
 * paramMap 예시:
 *   "/public/airport/bus": {
 *     legacyPath: "/getGroundFacilities",
 *     paramMap: { "schAirport": "airport" }  // 현재파라미터명: 기존파라미터명
 *   }
 */
const API_MAPPING = {
  newBaseUrl:    "http://localhost:8000",
  legacyBaseUrl: "https://old-api.example.go.kr",

  endpoints: {
    // airport
    "/public/airport/lease-contract":         "/service/rest/AirportLeaseInfo/airportLeaseContract",
    "/public/airport/transport-stats":        "/service/rest/totalAirportStatsService/getAirportStats",
    "/public/airport/airport-code":           "/service/rest/AirportCodeList/getAirportCodeList",
    "/public/airport/bus":                    "/service/rest/AirportBusInfo/businfo",
    "/public/airport/taxi-wait-cju":          "/service/rest/taxiWaitInfo/getJejuTaxiWaitInfo",
    "/public/airport/daily-expect-passenger": "/service/rest/dailyExpectPassenger/dailyExpectPassenger",
    "/public/airport/low-visibility/idx":     "/service/rest/airportLowVisibility/getAirportLowVisibilityIdx",
    "/public/airport/epi-gh":                 "/service/rest/EpiDataService/getEpiGhDataService",
    "/public/airport/low-visibility":         "/service/rest/airportLowVisibility/getAirportLowVisibility",
    "/public/airport/low-visibility/latest":  "/service/rest/airportLowVisibility/getAirportLowVisibilityLast",
    "/public/airport/retail-contract":        "/service/rest/contractService/getContractNo",
    "/public/airport/congestion/v1":          "/api/getAPRTPsgrCongestion/v1/aprtPsgrCongestion",
    "/public/airport/congestion/v2":          "/api/getAPRTPsgrCongestion_v2/v1/aprtPsgrCongestionV2",
    "/public/airport/monthly-inout/cju":      "/service/rest/jejuOutStats/getJejuOutCntMonth",
    "/public/airport/wait-time/v1":           "/api/getAPRTWaitTime/v1/aprtWaitTime",
    "/public/airport/wait-time/v2":           "/api/getAPRTWaitTime_v2/v1/aprtWaitTimeV2",

    // flight
    "/public/flight/routes-info":                  "/service/rest/serviceLine/serviceLines",
    "/public/flight/aircraft-type":                "/service/rest/FlightStatusAPLList/getFlightStatusAPLList",
    "/public/flight/flight-status":                "/service/rest/FlightStatusList/getFlightStatusList",
    "/public/flight/flight-status/taxfree":        "/service/rest/statusofPaxSeasonalFlight/getFlightStatusList",
    "/public/flight/flight-status/depart":         "/service/rest/StatusOfFlights/getDepFlightStatusList",
    "/public/flight/flight-status/arrival":        "/service/rest/StatusOfFlights/getArrFlightStatusList",
    "/public/flight/flight-schedule/taxfree-int":  "/service/rest/statusofPaxSeasonalFlight/getIPaxSfitSched",
    "/public/flight/flight-schedule/taxfree-dom":  "/service/rest/statusofPaxSeasonalFlight/getDPaxSfitSched",
    "/public/flight/apron/pus":                    "/service/rest/FlightApronStateList/getFlightApronStatusList",
    "/public/flight/apron/gmp":                    "/service/rest/FlightApronStateList/getGMPFlightApronStatusList",
    "/public/flight/apron/cju":                    "/service/rest/FlightApronStateList/getCJUFlightApronStatusList",
    "/public/flight/flight-schedule/dom":          "/service/rest/FlightScheduleList/getDflightScheduleList",
    "/public/flight/flight-schedule/int":          "/service/rest/FlightScheduleList/getIflightScheduleListt",
    "/public/flight/flight-status/detail":         "/api/FlightStatusListDTL/v1/getFlightStatusListDetail",

    // noise
    "/public/noise/noise-stats":           "/service/rest/noiseMeasureService/getNoiseMeasure",
    "/public/noise/noise-affected-area":   "/service/rest/noise/noiseAffectedArea",
    "/public/noise/noise-realtime/gmp":    "/api/getNoiseMeasureRT/v1/noiseMeasureRT",
    "/public/noise/noise-realtime/pus":    "/api/getNoiseMeasurePUS/v1/noiseMeasurePUS",

    // parking
    "/public/parking/valet-congestion":   "/service/rest/ValetParking/getGmpDValetParking",
    "/public/parking/parking-congestion": "/service/rest/AirportParkingCongestion/airportParkingCongestionRT",
    "/public/parking/parking-fee":        "/service/rest/AirportParkingFee/parkingfee",
    "/public/parking/airport-parking":    "/service/rest/AirportParking/airportparkingRT",
    "/public/parking/parking-cell/gmp":   "/service/rest/airportParkingCell/getGMPParkingCell",
  }
};
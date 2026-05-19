import logging
import logging.handlers
import datetime
from pathlib import Path

KST = datetime.timezone(datetime.timedelta(hours=9))

class KSTFormatter(logging.Formatter):
    """로그 타임스탬프를 한국 표준시(KST, UTC+9)로 출력"""
    def formatTime(self, record, datefmt=None):
        ct = datetime.datetime.fromtimestamp(record.created, tz=KST)
        return ct.strftime(datefmt or "%Y-%m-%d %H:%M:%S")

LOG_DIR = Path("/app/logs")

# 로그 종류별 디렉토리
LOG_DIRS = {
    "access": LOG_DIR / "access",
    "app":    LOG_DIR / "app",
    "error":  LOG_DIR / "error",
}
for d in LOG_DIRS.values():
    d.mkdir(parents=True, exist_ok=True)

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

formatter = KSTFormatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)

def _timed_handler(subdir: str, filename: str, level: int) -> logging.Handler:
    """
    자정마다 rotation, 파일명 예시: access.log.2026-05-15
    backupCount=90 → 90일치 보관
    """
    handler = logging.handlers.TimedRotatingFileHandler(
        LOG_DIRS[subdir] / filename,
        when="midnight",
        interval=1,
        backupCount=90,
        encoding="utf-8",
        utc=False,
    )
    handler.suffix = "%Y-%m-%d"
    handler.setLevel(level)
    handler.setFormatter(formatter)
    return handler

def setup_logging() -> None:
    """
    로그 디렉토리 구성:
      logs/access/access.log   - HTTP 요청/응답
      logs/app/app.log         - 애플리케이션 전반 이벤트
      logs/error/error.log     - WARNING 이상 오류
    """
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    # 콘솔 핸들러 (docker logs)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    root.addHandler(console)

    root.addHandler(_timed_handler("app",   "app.log",   logging.INFO))
    root.addHandler(_timed_handler("error", "error.log", logging.WARNING))

    # access 로그 — 전용 로거 (루트 로거로 중복 전파 차단)
    access_logger = logging.getLogger("api.access")
    access_logger.propagate = False
    access_logger.setLevel(logging.INFO)
    access_logger.addHandler(_timed_handler("access", "access.log", logging.INFO))

    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("aioodbc").setLevel(logging.WARNING)


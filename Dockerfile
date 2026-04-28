FROM python:3.12-slim

WORKDIR /app

RUN chmod 1777 /tmp

RUN apt-get update && apt-get install -y \
    build-essential \
    unixodbc \
    unixodbc-dev \
    alien \
    libaio1 \
    && rm -rf /var/lib/apt/lists/*

COPY db/drivers/oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm /tmp/
COPY db/drivers/oracle-instantclient12.2-odbc-12.2.0.1.0-2.x86_64.rpm /tmp/

RUN alien -i /tmp/oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm \
    && alien -i /tmp/oracle-instantclient12.2-odbc-12.2.0.1.0-2.x86_64.rpm \
    && rm /tmp/*.rpm

ENV LD_LIBRARY_PATH=/usr/lib/oracle/12.2/client64/lib
ENV ORACLE_HOME=/usr/lib/oracle/12.2/client64

RUN echo "[Oracle]\nDescription=Oracle ODBC\nDriver=/usr/lib/oracle/12.2/client64/lib/libsqora.so.12.1" \
    > /etc/odbcinst.ini

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
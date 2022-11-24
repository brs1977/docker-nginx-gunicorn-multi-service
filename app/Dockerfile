FROM python:3.9.15-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && \ 
    pip3 install --no-cache-dir numpy==1.20.3 pandas==1.2.4 gunicorn==20.1.0 Werkzeug==2.0.1 dash==1.20.0 dash-html-components==1.1.3

COPY . /app

# CMD ["gunicorn", "-b", "0.0.0.0:8015", "--workers", "2", "app:server"]
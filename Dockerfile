# UpMarket
# Version: 1.0
FROM python:3.10.3

COPY ./back /upmarket

COPY ./back/requirements.txt /upmarket/requirements.txt

WORKDIR upmarket

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
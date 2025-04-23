FROM python:3.11

WORKDIR /container

COPY . .

RUN pip install --no-cache-dir -r /container/requirements.txt

EXPOSE 8000

CMD ["uvicorn","app.api:app", "--host", "0.0.0.0", "--port", "8000"]
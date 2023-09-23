FROM python:3.9-slim
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
RUN pip3 install uvicorn

ENTRYPOINT ["uvicorn", "main:app", "--root-path", "/api", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11-slim

WORKDIR /version_1

COPY requirements.txt .

RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

COPY ./v1.py ./v1.py

EXPOSE 5000

CMD ["python", "v1.py"]

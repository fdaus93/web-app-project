FROM python:3.11-slim

WORKDIR /version_3

COPY requirements.txt .

RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

# Copy v1.py into /version_1
COPY ./v3.py ./v3.py

EXPOSE 5000

CMD ["python", "v3.py"]

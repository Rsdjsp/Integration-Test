FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev iputils-ping curl \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY src/ src/

EXPOSE 5000


ENV DB_NAME=postgres
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
ENV DB_HOST=db
ENV DB_PORT=5432

CMD ["python","-u", "src/app.py"]

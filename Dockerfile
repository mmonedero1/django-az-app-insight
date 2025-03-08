FROM python:3.10-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /api

# RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc

# RUN curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | tee /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update -y

# RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17

# RUN apt-get install -y unixodbc-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["bash", "-c", "python manage.py runserver 0.0.0.0:8000"]

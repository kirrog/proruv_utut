FROM python:3.9
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --upgrade pip -r requirements.txt
COPY ./src /app/src
COPY ./static /app/static
COPY ./templates /app/templates
COPY ./main.py /app
COPY ./main.py /app
EXPOSE 5000
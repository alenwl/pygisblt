FROM python:3.6 as python-base
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . /opt/app-root/src/
WORKDIR /opt/app-root/src/
RUN pip3 install -r requirements.txt && rm -rf /root/.cache

CMD gunicorn wsgi:application -b 0.0.0.0:8080
EXPOSE 8080 
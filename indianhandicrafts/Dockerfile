FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /app
#COPY ./requirements.txt /app/requirements.txt
COPY  indianhandicrafts/requirements.txt /app/requirements.txt
#COPY ./app.py /app/app.py
COPY  indianhandicrafts/app.py  /app/app.py
#COPY ./adminscript.py /app/adminscript.py
COPY  indianhandicrafts/adminscript.py /app/adminscript.py
#COPY ./images/ app/images
COPY  indianhandicrafts/images app/images
#COPY ./static/ app/static
COPY  indianhandicrafts/static app/static
#COPY ./templates/ app/templates
COPY   indianhandicrafts/templates app/templates
#COPY ./samples/ app/samples
COPY   indianhandicrafts/samples app/samples
#WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python3", "app.py"]

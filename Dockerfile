FROM czpfirst/dx-ubuntu1804-py380
COPY . /opt/play-backend
WORKDIR /opt/play-backend
RUN pip3 install -r requirements.txt
ENV ENV_NAME=$ENV_NAME
EXPOSE 80
CMD uvicorn application:app --host 0.0.0.0 --port 80
FROM python:3.7
#RUN python -m ensurepip
#RUN python -m pip install -U pip
RUN pip install --upgrade pip
RUN python -m pip install "rasa==2.1.2"
WORKDIR /app
COPY . .
RUN rasa train
USER 1001
ENTRYPOINT [ "rasa" ]
CMD [ "run", "--enable-api","--port","5005","--cors","*" ]

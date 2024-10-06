FROM python:3.9.11
RUN apt update
RUN apt install -y postgresql-client

WORKDIR /inspectr_test

COPY ./src/requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt

COPY ./entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT ["/entrypoint"]

EXPOSE 8003

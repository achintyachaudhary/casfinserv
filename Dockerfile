FROM python:3.6-alpine

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /casfinserv

WORKDIR /casfinserv

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD ["./docker_run_script.sh"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
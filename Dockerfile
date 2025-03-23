FROM python:3.11

RUN mkdir src
WORKDIR src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./myapp/requirements.txt /src/
RUN pip install -r requirements.txt

ADD ./myapp /src/

ENTRYPOINT ./entrypoint.sh
#CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
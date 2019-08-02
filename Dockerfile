FROM python:3.7-alpine

ADD . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system --deploy

CMD ["python", "__init__.py"]

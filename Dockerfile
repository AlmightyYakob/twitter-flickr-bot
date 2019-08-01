FROM kennethreitz/pipenv as build

ADD . /app
WORKDIR /app

RUN pipenv install --system --deploy

# Do More
CMD ["python", "__init__.py"]

# Another Bot for Sam

## Installation
Requirements:
* Pipenv

To install, Pipenv, run:
```
pip install pipenv
```

After Pipenv is installed, to setup the project simply run:
```
pipenv install
```

To access the newly created virtualenv, run:
```
pipenv shell
```

## Configuration
This project uses expects a .env file to be present in the project root, containing values for the following environment variables:
* FLICKR_API_KEY
* FLICKR_API_SECRET
* FLICKR_USERNAME
* TWITTER_CONSUMER_API_KEY
* TWITTER_CONSUMER_API_SECRET
* TWITTER_ACCESS_TOKEN
* TWITTER_ACCESS_TOKEN_SECRET

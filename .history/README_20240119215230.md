# Sapphire Demo

## Pre-requisites

- create a virtual env `virtualenv venv`
- activate virtualenv: `source venv/bin/activate`
- install requirements: `pip install -r requirements.txt`
- install Vertex LLM SDK: `pip install setup_files/google_cloud_aiplatform-1.23.0.llm.alpha.23.03.28-py2.py3-none-any.whl "shapely<2.0.0"`
- add a looker.ini file to the config directory

## Running with Docker (using your application default credentials)
- build with docker: `docker build -t sapphire-backend .`
- run the container: `docker run -v "$HOME/.config/gcloud/application_default_credentials.json":/gcp/creds.json:ro --env GOOGLE_APPLICATION_CREDENTIALS=/gcp/creds.json -e PORT=5000 -p 5000:5000 sapphire-backend`

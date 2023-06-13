FROM ubuntu:22.04

RUN apt-get update && \
    apt-get -y install gcc g++ python3-dev wget curl python3-pip nodejs npm && \
    rm -rf /var/lib/apt/lists/*

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
ENV HNSWLIB_NO_NATIVE=1

# Install gcloud
RUN curl -sSL https://sdk.cloud.google.com | bash

ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin



# Copy local files to the container image.
COPY requirements.txt ./
COPY ./config ./config
COPY ./sapphire_web ./
COPY ./setup_files ./
COPY ./sapphire_llm/ ./sapphire_llm
#COPY ./config/gcp_creds.json ./
COPY ./config/cortex-demo-genai-dc05304b1e79.json ./gcp_creds.json
#COPY sapphire_frontend sapphire_frontend

RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install pexpect
#RUN pip install google_cloud_aiplatform-1.25.dev20230502+language.models-py2.py3-none-any.whl "shapely<2.0.0"
RUN cd sapphire_llm && python3 setup.py install && cd ..
ENV GOOGLE_APPLICATION_CREDENTIALS=./gcp_creds.json
#RUN cd sapphire_frontend && npm i && npm run build

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

# Redis-Pipeline
 NoSQL databases are gaining mass adoption with the increasing production of large amounts of unstructured data. In this project we create an ingestion pipeline from scrapy framework crawlers as the data source into a redis database which will then make the data available for consumption upon request by the user.
# How To:
- Clone the file 
  + git clone https://github.com/Obuya-Nyang/Redis-Pipeline.git
- Change directory
  + cd producer
- Docker and docker compose installation is necessary to run the project 
  + Create docker network
    + docker network create rednet
  + Run docker compose
    + docker compose up
  + Build docker image 
    + docker build -t redispipeline:v001 .
  + Run image container 
    + docker run -it --network rednet --name pipelinecontainer --rm redispipeline:v001 /bin/bash
- Run crawlers
  + python run.py

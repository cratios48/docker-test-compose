FROM python:3.6-alpine
ENV appDir="/app"
ENV appFile="fromIP.py"
WORKDIR ${appDir}
RUN pip install Flask redis
COPY ${appFile} .
EXPOSE 80/tcp
CMD python ${appFile}
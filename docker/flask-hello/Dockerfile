FROM python:3.6-alpine
ENV appDir="/app"
WORKDIR ${appDir}
RUN pip install Flask
COPY hello.py .
EXPOSE 80/tcp
CMD FLASK_APP=hello.py flask run 
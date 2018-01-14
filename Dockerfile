FROM alpine:latest
MAINTAINER Matt Lisivick "lisivickmatt@gmail.com"
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*
COPY /src /src
WORKDIR /src
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 8080
CMD ["oauth-flow.py"]
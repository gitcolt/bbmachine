FROM alpine:3.10

RUN apk --no-cache add  python3 \
                        git \
                        go \
                        musl-dev

RUN pip3 install    django \
                    django-dotenv \
                    gunicorn

RUN mkdir /home/go

ENV GOPATH="/home/go"
ENV PATH="${PATH}:${GOPATH}/bin"

RUN go get -u github.com/tomnomnom/assetfinder

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN python3 manage.py migrate

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "bbmachine.wsgi"]


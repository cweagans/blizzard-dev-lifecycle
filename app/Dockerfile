FROM alpine:3.17 AS base
WORKDIR /app
ENV TZ=Etc/UTC
ENV LANG C.UTF-8
RUN --mount=type=cache,target=/var/cache/apk apk update
RUN --mount=type=cache,target=/var/cache/apk apk add python3

# We don't need pip in the final image, so run the pip installation in an
# intermediate container and copy the resulting download to the final container
# afterwards.
FROM base AS builder
RUN --mount=type=cache,target=/var/cache/apk apk add py3-pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

FROM base
RUN adduser --system app
USER app
COPY . .
COPY --from=builder /usr/lib/python3.10/site-packages /usr/lib/python3.10/site-packages
ENTRYPOINT python3 th3-server.py

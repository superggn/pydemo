# FROM fluent/fluentd:v1.17-debian-arm64-1
FROM fluent/fluentd:v1.17-debian-amd64-1
USER root
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.4.3"]
USER fluent

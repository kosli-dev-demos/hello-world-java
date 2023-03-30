ARG ARCH=
FROM ${ARCH}openjdk:17-alpine
ARG TARGETARCH

COPY ./target/hello-world-java-1.0.0.jar /app/
WORKDIR /app

EXPOSE 80

CMD ["java", "-jar", "hello-world-api.jar"]
FROM openjdk:11 AS buildstage
COPY . /app
WORKDIR /app
RUN javac Hello.java

FROM openjdk:11-jre-slim
COPY --from=buildstage /app/Hello.class /app/
WORKDIR /app
CMD java Hello

FROM swift:5.0 AS buildstage
COPY . /app
WORKDIR /app
RUN swift build -c release
RUN cp .build/x86_64-unknown-linux/release/ContainerizedSwift .

FROM swift:5.0-slim
COPY --from=buildstage /app/ContainerizedSwift /app/
WORKDIR /app
CMD ./ContainerizedSwift

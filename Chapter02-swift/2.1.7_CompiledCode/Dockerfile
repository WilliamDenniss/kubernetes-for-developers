FROM swift:5.0
COPY . /app
WORKDIR /app
RUN swift build -c release
RUN cp .build/x86_64-unknown-linux/release/ContainerizedSwift .
CMD ./ContainerizedSwift

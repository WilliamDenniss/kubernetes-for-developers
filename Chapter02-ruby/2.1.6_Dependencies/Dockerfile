FROM ruby
RUN apt-get update -qq
RUN apt-get install -y mariadb-client
COPY . /app
WORKDIR /app
CMD ruby helloworld.rb

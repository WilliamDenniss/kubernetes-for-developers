FROM ruby
RUN apt-get update -qq
RUN apt-get install -y bsdtar
RUN mkdir -p ~/.fonts; cd ~/.fonts
RUN curl "https://noto-website-2.storage.googleapis.com/pkgs/Noto-hinted.zip" | bsdtar -xvf-
RUN fc-cache -f -v #D
COPY . /app
WORKDIR /app
CMD ruby helloworld.rb

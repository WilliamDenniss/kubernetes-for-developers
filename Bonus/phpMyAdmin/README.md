How to use this phpMyAdmin Docker Compose setup:

1. Edit the `config/config.user.inc.php` file and add your own server details.
2. Add your SSL certs to the `config/` directory, and check the names in the config to ensure they're pointing at the right files.
3. Run `docker-compose build; docker-compose up`
4. Connect to http://localhost:8079

About:

The phpMyAdmin config is about the thing you'd change with a custom installation. This docker image shows how you inherit from the base phpMyAdmin image and change just the configuration that you need. I find it convenient to bundle the SSL certs in this image, and using docker-compose to run everything to make this portable, and repeatable.
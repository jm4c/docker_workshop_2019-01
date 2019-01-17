# Docker Compose Example

This Example contains:
 * A reverse proxy using nginx server with different locations (2 Python apps)
 * A Redis server
 * 2 Python apps. One that write a random key/value (for example date / timestamp) into your Redis server and the other app that read and print all keys from your database.


# Intructions

- Go into the challenge directory;
- Run `docker-compose up`;
- Go to `<address>/write` to write the current timestamp/datetime on redis;
- Go to `<address>/read` to read the last written value on redis.
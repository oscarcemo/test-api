# TEST-API

## Requirements

* docker-compose
* docker

## How to run

* In the folder execute:

```bash
docker-compose up --build -d 
```

* Query the API ignoring self-signed certificate: `curl -k -L http://127.0.0.1/hello`

```bash
curl -k -L http://127.0.0.1/hello
{
    "Hello": "world"
}
```

## Explanation
 
 * I choose docker and docker-compose because it's easy to deploy.
 
 * I choose python language because with `flask` it's easy to create a simple api.

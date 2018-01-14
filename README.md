# Clover OAuth2 Workflow

#### This is a simple example of how to authenticate against the Clover OAuth2 sandbox and retrieve an access token.

The setup is a simple Bottle web server that connects to the Clover sandbox.

### Requirements

- Docker or pip (Python's package manager)

### Setup 

##### Docker

Build the container from the Dockerfile
```commandline
docker build -t clover-auth .
```

Run the container. Expose the HTTP port and define the environment variables.
Replace the application_id and application_secret with your dev credentials.

```commandline
docker run -p 8080:8080 -e application_id='XXXXXXXXXX' -e application_secretion='XXXXXXXXXX' -t clover-auth
```

##### pip

Install bottle using pip:
```commandline
pip install bottle
```

Then, set your application_id and application_secret:

```python
os.environ["application_id"] = "XXXXXXX"
os.environ["application_secret"] = "XXXXXXX"
```

Run the HTTP server
```commandline
python src/oauth-flow.py
```

## Usage

Navigate to your [localhost](localhost:8080) .

You will see a hyperlink to begin the OAuth2 workflow.



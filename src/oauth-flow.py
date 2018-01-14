from bottle import get, request, static_file, run
import httplib, json, os

# Your application's ID and secret, available from your application dashboard.
# application_id from environment
application_id = os.getenv('application_id', "world")
#application_secret from environment
application_secret = os.getenv('application_secret', "world")
# Headers to provide to OAuth API endpoints
oauth_request_headers = { 'Authorization': 'Client ' + application_secret,
                          'Accept': 'application/json',
                          'Content-Type': 'application/json'}

# Serves the link that merchants click to authorize your application
@get('/')
def authorize():
  return '''<a href="https://sandbox.dev.clover.com/oauth/authorize?client_id={0}">Click here</a>
            to authorize the application.'''.format(application_id)

# Serves requests to your application's redirect URL
# Note that you need to set your application's Redirect URL to
# http://localhost:8080/callback from your application dashboard
@get('/oauth_callback')
def callback():

  # Extract the returned authorization code from the URL
  authorization_code = request.query.get('code')
  if authorization_code:

    # Provide the code in a request to the Obtain Token endpoint
    oauth_request_body = {
      'client_id': application_id,
      'client_secret': application_secret,
      'code': authorization_code
    }
    connection = httplib.HTTPSConnection('sandbox.dev.clover.com')
    connection.request('POST', '/oauth/token', json.dumps(oauth_request_body), oauth_request_headers)

    # Extract the returned access token from the response body
    oauth_response_body = json.loads(connection.getresponse().read())
    if oauth_response_body['access_token']:

      # Here, instead of printing the access token, your application server should store it securely
      print 'Access token: ' + oauth_response_body['access_token']
      return 'Authorization succeeded!'

    # The response from the Obtain Token endpoint did not include an access token. Something went wrong.
    else:
      return 'Code exchange failed!'

  # The request to the Redirect URL did not include an authorization code. Something went wrong.
  else:
    return 'Authorization failed!'

# Start up the server
run(host='0.0.0.0', port=8080)


from flask import Flask, request, session, g
from flask_oidc import OpenIDConnect
app = Flask(__name__)

app.config.update({
    'SECRET_KEY': "TEST",
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_TOKEN_TYPE_HINT': 'access_token',
})
oidc = OpenIDConnect(app)
@app.route('/')
def index():
    if oidc.user_loggedin:
        return 'Welcome %s' % oidc.user_getfield('email')
    else:
        return "Logged in"
        #oidc.redirect_to_auth_server(None, request.values)

@app.route('/oidc_callback')
#@oidc.require_login
def callback(data):
    return 'Hello. You submitted %s' % data

@app.route('/test')

#@oidc.require_keycloak_role('keycloak-test', 'user')
@oidc.accept_token(True, [])
#, #scopes_required=["openid"])
#@oidc.require_login
def test():
    #    for key, val in session.iteritems():
    #print(key, val)
    #oidc.re
    #print(g.oidc_id_token)
    
    try:
        roles = g.oidc_token_info['resource_access']['keycloak-test']['roles']
    except Exception as ex:
        return ex
    else:     
        if "user" in roles:
            return 'Du darfst \n'
        else:
            return "Du darfst nicht\n"
    
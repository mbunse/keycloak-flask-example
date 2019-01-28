# Keycloak: New Client "keycloak-test", Access Type "bearer-only"
# Keycloak: New Role "api_user"
# Keycloak: new user tester, rolemapping "user" for client keycloak-test
# Keycloak: New client "curl", access type "public"

RESULT=`curl --data "grant_type=password&client_id=curl&username=tester&password=test" http://localhost:8080/auth/realms/master/protocol/openid-connect/token`
TOKEN=`echo $RESULT | sed 's/.*access_token":"//g' | sed 's/".*//g'`
#curl http://localhost:5000/test -H "Authorization: bearer $TOKEN"
curl http://localhost:5000/test?access_token=$TOKEN

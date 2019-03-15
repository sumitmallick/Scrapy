# dec: VWgy8w~zyk7ub2Q5EVf6J~pxUT_i__Eq

# id:dc7161be3d@mobilyte-solutions.accelo.com



import requests
import os

params = {
  'client_id': 'VWgy8w~zyk7ub2Q5EVf6J~pxUT_i__Eq',
}


r = requests.get(
    'https://mobilyte-solutions.api.accelo.com/api/v0',
    params=params)
print(r)


# POST /oauth2/v0/authorize HTTP/1.1
# Host: planet-express.api.accelo.com
# Content-Type: application/x-www-form-urlencoded

# client_id=a17c78ao@planet-express.accelo.com
# response_type=code
# scope=read(companies,contacts),write(staff)
# redirect_uri=https//planet-express.com/oauth-callback
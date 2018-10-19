from meraki import meraki
from passwords import key


myOrgs = meraki.myorgaccess(key)
print(myOrgs)
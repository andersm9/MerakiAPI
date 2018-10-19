from meraki import meraki
from passwords import key

#apikey = "024d502123bedfdb77b1b3fc0d189a39786f13b4"
myOrgs = meraki.myorgaccess(key)
print(myOrgs)
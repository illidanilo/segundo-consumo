import json
import requests

import conf
sandbox = ("https://sandboxapicdc.cisco.com")

def obtener_token(usuario, clave):


    url = sandbox + "/api/aaaLogin.json"
    body = {
        "aaaUser":{
            "attributes":{
                "name":usuario,
                "pwd":clave

            }
        }
    }
    cabecera = {
    "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False)
    token = respuesta.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]
    return token
obtener_token(conf.usuario, conf.clave)


def aaalistDomains():
    cabecera = {
        "Content-Type": "application/json"
    }
    lagalleta = {
        "APIC-Cookie": obtener_token(conf.usuario, conf.clave)
    }

    respuesta = requests.get(sandbox+"/api/aaaListDomains.json", headers=cabecera, cookies=lagalleta, verify=False)
    total = int(respuesta.json()["totalCount"])

    respuesta = respuesta.json()["imdata"]



    print(respuesta)

aaalistDomains()

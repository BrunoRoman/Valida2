from network.models import Resultado
import json
def save(router,requests):
    try:
        comandos = json.loads(requests.data['comandos'])
        for key in list(comandos.keys()):
            r = Resultado(ambiente=requests.data['ambiente'],hostname=requests.data['hostname'],ip=requests.data['ip'],comandos=comandos[key],output=getattr(router,key))
            r.save()
        return 'sucesso'
    except Exceptions as ident:
        return ident
from abc import ABC, abstractmethod
import re

class Equipamento(ABC):
    def __init__(self,hostname,ip,netmiko,comandos):
        super().__init__()
        self._hostaname = hostname
        self._ip = ip
        self._netmiko = netmiko
        with ConnectHandler(device_type=netmiko,ip=ip,username='bruno',password='bruno',secret='bruno',timeout=10) as conn:
            self._ospf_int = conn.send_command(comandos['ospf_int'])
            self._ospf_neighbor = conn.send_command(comandos['ospf_neighbor'])
    
    @property
    def ospf_int(self):
        return self._ospf_int
    
    
    @ospf_int.setter
    @abstractmethod
    def ospf_int(self,val):
        pass

    @property
    def ospf_neighbor(self):
        return self._ospf_neighbor
    
    
    @ospf_neighbor.setter
    @abstractmethod
    def ospf_neighbor(self,val):
        pass
                                                                                      
class Router(Equipamento):
    
    

    @Equipamento.ospf_int.setter
    def ospf_int(self,val):
        self._ospf_int
    
    @Equipamento.ospf_neighbor.setter
    def ospf_neighbor(self,val):
        pattern  = r'eighbor\s(?P<neighbor>\d+\.\d+\.\d+\.\d+)\,.*\n.*interface\s(?P<interface>\w+/\d+)\s+\n.*\n.*\n.*\n.*\n.*\n.*for\s+(?P<uptime>\S+)'
        list_ospf_neighbor = re.split('\n\s[A-Z]',val)
        print('agora chamou')
        neighbors = []
        for neighbor in list_ospf_neighbor:
            m = re.match(pattern, neighbor)
            try:
                neighbors.append(m.groupdict())
            except AttributeError:
                continue
        self._ospf_neighbor = neighbors
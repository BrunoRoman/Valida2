import re
import netmiko
from netmiko import ConnectHandler
from network.network_templates.Abstracts import Equipamento

class Router(Equipamento):
    
    def __init__(self,hostname,ip,netmiko,comandos):
        super().__init__(hostname,ip,netmiko,comandos)
        with ConnectHandler(device_type=netmiko,ip=ip,username='bruno',password='bruno',secret='bruno',timeout=10) as conn:
            self._ospf_int = conn.send_command(comandos['ospf_int'],use_textfsm=True)
            self._ospf_neighbor = conn.send_command(comandos['ospf_neighbor'],use_textfsm=True)
            self._interfaces = conn.send_command(comandos['interfaces'],use_textfsm=True)

    @Equipamento.interfaces.setter
    def interfaces(self,val):
        self._interfaces

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

    @Equipamento.bgp.setter
    def bgp(self,val):
        self._bgp = val

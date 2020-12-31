from abc import ABC, abstractmethod

class Equipamento(ABC):
    def __init__(self,hostname,ip,netmiko,comandos):
        self.__hostaname = hostname
        self.__ip = ip
        self.__netmiko = netmiko
    

    @property
    def interfaces(self):
        return self._ospf_int
    
    
    @interfaces.setter
    @abstractmethod
    def interfaces(self,val):
        pass

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
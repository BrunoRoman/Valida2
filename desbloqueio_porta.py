from netmiko import ConnectHandler
import re

cisco = {
    'device_type': 'cisco_ios_telnet',
    'host':   '192.168.0.2',
    'username': 'admin',
    'password': 'cisco',        # optional, defaults to 22
    'secret': 'cisco',     # optional, defaults to ''
}

with ConnectHandler(**cisco) as conn:
    result = conn.send_command('show interface status err-disable')
    conn.enable()
    pattern = '\n(\S+)'
    interfaces = re.findall(pattern,result)
    if len(interfaces)>1:
        print(re.findall(pattern,result))
        if 'Port' in interfaces:
            interfaces.remove('Port')
        for i in interfaces:
            commands = [f'interface {i}',' shutdown','no shutdown']
            result = conn.send_config_set(commands)
        result = conn.send_command('clear port-security all')
        print(f'interfaces retiradas de err-disable {interfaces}' )
    else:
        print('Não há interfaces em err-disable')

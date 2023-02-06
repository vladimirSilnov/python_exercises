# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


"""

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)
        self.topology_dict = topology_dict


    def _normalize(self, topology_dict):
        self._normalize = {}
        for local, remote in topology_dict.items():
            if not self._normalize.get(remote) == local:
                self._normalize[local] = remote
        return self._normalize


    def del_node(self, l_node, r_node):
        if self.topology_dict.get(l_node):
            del self.topology_dict[l_node]
        if self.topology_dict.get(r_node):
            del self.topology_dict[r_node]

    def delete_node(self, node):
        origin_size = len(self.topology)
        for src, dst in list(self.topology.items()):
            if node in src or node in dst:
                del self.topology[src]
        if origin_size == len(self.topology):
            print('Такого устройства нет')

    def add_link(self, link_src, link_dst):
        if self.topology.get(link_src) == None:
            self.topology[link_src] = link_dst
        else:   
            for sorc, dest in self.topology.items():
                if sorc == link_src and dest != link_dst:
                    print('Cоединение с одним из портов существует')
                elif sorc == link_src and dest == link_dst:
                    print('Такое соединение существует')

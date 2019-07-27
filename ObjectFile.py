class RowCsv:
    def __init__(self, eth_src, eth_dst, ip_src, ip_dst, ip_len, ip_proto, time):
        self.eth_src = eth_src
        self.eth_dst = eth_dst
        self.ip_src = ip_src
        self.ip_dst = ip_dst
        self.ip_len = ip_len
        self.ip_proto = ip_proto
        self.time = time

    def get_eth_src(self):
        return self.eth_src

    def get_eth_dst(self):
        return self.eth_dst

    def get_ip_src(self):
        return self.ip_src

    def get_ip_dst(self):
        return self.ip_dst

    def get_ip_len(self):
        return self.ip_len

    def get_ip_proto(self):
        return self.ip_proto

    def get_time(self):
        return self.time


class Sample(object):
    def __init__(self, send ,receive):
        self.send = send
        self.receive=receive

    def set_send(self,len):
        self.send = len

    def get_send(self):
        return self.send

    def set_receive(self,len):
        self.receive = len

    def get_receive(self):
        return self.receive


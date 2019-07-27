import csv
import math
import pandas as pd


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
    def __init__(self, send ,receive=None):
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


bulb = '00:17:88:7c:96:3c'
camera = '00:62:6e:6c:6f:36'

data = pd.read_csv("/home/gilad/Downloads/testlast.csv")
count_rows = data.shape[0]
tel = {}

for x in range(count_rows):

    r = RowCsv(data.iloc[x,0],data.iloc[x,1],data.iloc[x,2],data.iloc[x,3],data.iloc[x,4],data.iloc[x,5],data.iloc[x,6])
    iplen = float(r.get_ip_len())
    if not math.isnan(iplen):
        if data.iloc[x, 0] == camera or data.iloc[x, 0] == bulb: # only camera & bulb
            if data.iloc[x, 0] not in tel:
                tel[data.iloc[x, 0]] = []
            tel[data.iloc[x, 0]].append(r)
        if data.iloc[x, 1] == camera or data.iloc[x, 1] == bulb: # only camera & bulb
            if data.iloc[x, 1] not in tel:
                tel[data.iloc[x, 1]] = []
            tel[data.iloc[x, 1]].append(r)


ls = {camera: {}, bulb: {}}

for k, v in tel.items():
    for row in v:
        scur = row.get_time()
        scur = scur[5: 13]+"0"
        if row.get_eth_src() == k:
            if scur not in ls[k]:
                ls[k][scur]=Sample(float(row.get_ip_len()), 0)
            else:
                (ls[k][scur]).set_send(float((ls[k][scur]).get_send()) + float(row.get_ip_len()))
        else:
            if scur not in ls[k]:
                ls[k][scur] = Sample(0,float(row.get_ip_len()))
            else:
                (ls[k][scur]).set_receive(float((ls[k][scur]).get_receive()) + float(row.get_ip_len()))

for k,v in ls.items():
    for ke,va in v.items():
        print(str("receive - "+str(va.get_receive())) + "  send - " + str(va.get_send()) + "     "+str(ke) + "   "+str(k))

w = csv.writer(open("/home/gilad/Downloads/output.csv", "w"))
for key, val in ls.items():
    if key == camera:
        str_type = "camera"
    else:
        str_type = "bulb"
    for ke, va in val.items():
        w.writerow([str_type, va.get_send(), va.get_receive()])


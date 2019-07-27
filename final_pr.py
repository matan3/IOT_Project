import csv
import math
import pandas as pd
import ObjectFile as obj


bulb = '00:17:88:7c:96:3c'
camera = '00:62:6e:6c:6f:36'

data = pd.read_csv("/home/gilad/Downloads/testfile - testfile.csv", index_col=False)
count_rows = int(int(data.shape[0])/1)
tel = {}
print(count_rows)
# w = csv.writer(open("/home/gilad/Downloads/hand.csv", "w"))
for x in range(count_rows):

    # w.writerow( [data.iloc[x, 0], data.iloc[x, 1], data.iloc[x, 2], data.iloc[x, 3], float(data.iloc[x, 4]), data.iloc[x, 5],data.iloc[x, 6]])
    r = obj.RowCsv(data.iloc[x,0],data.iloc[x,1],data.iloc[x,2],data.iloc[x,3],float(data.iloc[x,4]),data.iloc[x,5],data.iloc[x,7])
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
                ls[k][scur]=obj.Sample(float(row.get_ip_len()), 0)
            else:
                (ls[k][scur]).set_send(float((ls[k][scur]).get_send()) + float(row.get_ip_len()))
        else:
            if scur not in ls[k]:
                ls[k][scur] = obj.Sample(0,float(row.get_ip_len()))

            else:
                (ls[k][scur]).set_receive(float((ls[k][scur]).get_receive()) + float(row.get_ip_len()))

for k,v in ls.items():
    for ke,va in v.items():
        print(str("receive - "+str(va.get_receive())) + "  send - " + str(va.get_send()) + "     "+str(ke) + "   "+str(k))

w = csv.writer(open("/home/gilad/Downloads/output2.csv", "w"))
#w.writerow(['Type', 'Send', 'Receive'])
for key, val in ls.items():
    if key == camera:
        str_type = "camera"
    else:
        str_type = "bulb"
    for ke, va in val.items():
        w.writerow([str_type, va.get_send(), va.get_receive()])




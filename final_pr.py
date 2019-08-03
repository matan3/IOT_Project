from datetime import datetime
import csv
import math
import pandas as pd
import ObjectFile as obj

FMT = '%H:%M:%S.%f'
bulb = '00:17:88:7c:96:3c'
camera = '00:62:6e:6c:6f:36'
N=10


'''
Read data from CSV to Data-Structure Map 
'''
data = pd.read_csv("C:\\Program Files\\Wireshark\\testfile - testfile.csv",encoding='latin-1')
#data = pd.read_csv("/home/gilad/Downloads/testfile - testfile.csv", index_col=False)
count_rows = int(int(data.shape[0])/2)
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
        time_stamp = row.get_time()
        time_stamp = time_stamp[5: 12] + "0"
        time = row.get_time()
        time = str(time[5: 20])


        size_msg=float(row.get_ip_len())
        if row.get_eth_src() == k:
            if time_stamp not in ls[k]:
                ls[k][time_stamp]=obj.Sample_big(size_msg, 0, 1, 0)
                (ls[k][time_stamp]).set_last_time_send(time)
            else :
                if (ls[k][time_stamp]).get_count_send() < N :
                    (ls[k][time_stamp]).set_send(float((ls[k][time_stamp]).get_send()) + size_msg)
                    (ls[k][time_stamp]).increase_count_send()
                    last_time=str((ls[k][time_stamp]).get_last_time_send())
                    if last_time !='0' :
                        tdelta = datetime.strptime(time, FMT) - datetime.strptime(last_time, FMT)
                        (ls[k][time_stamp]).get_time_send_ls().append(tdelta.total_seconds())

                    (ls[k][time_stamp]).set_last_time_send(time)
        else:
            if time_stamp not in ls[k]:
                ls[k][time_stamp] = obj.Sample_big(0, size_msg, 0, 1)
                (ls[k][time_stamp]).set_last_time_receive(time)

            else:
                if (ls[k][time_stamp]).get_count_receive() < N:
                    (ls[k][time_stamp]).set_receive(float((ls[k][time_stamp]).get_receive()) + size_msg)
                    (ls[k][time_stamp]).increase_count_receive()
                    last_time = str((ls[k][time_stamp]).get_last_time_receive())
                    if last_time != '0':
                        tdelta = datetime.strptime(time, FMT) - datetime.strptime(last_time, FMT)
                        (ls[k][time_stamp]).get_time_receive_ls().append(tdelta.total_seconds())

                    (ls[k][time_stamp]).set_last_time_receive(time)


for k,v in ls.items():
    for ke,va in v.items():
        print(str("receive - "+str(va.get_receive())) + "  send - " + str(va.get_send()) + "     "+str(ke) + "   "+str(k) + "   "+str(va.get_time_receive_ls())+ "   "+str(va.get_time_send_ls()))

#w = csv.writer(open("/home/gilad/Downloads/output2.csv", "w"))
with open("C:\\Users\\Matan\\Downloads\\output.csv", 'w') as output_file:

    for key, val in ls.items():
        if key == camera:
            str_type = "camera"
        else:
            str_type = "bulb"
        for ke, va in val.items():

            output_file.write(str_type+', '+str(va.get_send())+', '+ str(va.get_receive()))
            # for elements in (va.get_time_send_ls()):
            #     output_file.write(', '+str(elements))
            # for elements in (va.get_time_receive_ls()):
            #     output_file.write(', ' + str(elements))
            #output_file.write(', ' + str(next(iter(va.get_time_send_ls()))))
            #output_file.write(', ' + str(next(iter(va.get_time_receive_ls()))))
            output_file.write('\n ')


# ls = {camera: [], bulb: []}
#
# for k, v in tel.items():
#     for row in v:
#         scur = row.get_time()
#         scur = scur[5: 12]+"0"
#         (ls[k]).append(obj.Sample(0, 0, 1, 0))
#
# print(ls.items())
# for k,v in ls.items():
#     for va in v:
#         print(str("receive - "+str(va.get_receive())) + "  send - " + str(va.get_send()) + "   "+str(k) + "   "+str(va.get_count_receive())+ "   "+str(va.get_count_send()))

#

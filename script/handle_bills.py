
# coding: utf-8

dic = {

}

import datetime
with open(u'/Users/ashu/Downloads/concel.csv') as concel_fd:
    for line in concel_fd:
        # print line
        line = line.strip()
        if line == '':
            continue
        items = line.split(',')

        if len(items) < 8:
            continue
        user_id, s_id, adress, create_time = items[1], items[4], items[2], items[7]

        try:
            create_time = datetime.datetime.strptime(create_time, '%Y/%m/%d %H:%M')
        except:
            create_time = datetime.datetime.strptime('2017/1/1 1:1', '%Y/%m/%d %H:%M')

        key = (user_id, s_id)

        dic[key] = (items, line)


output_file = '/Users/ashu/PycharmProjects/daypy/script/output.csv'

output = file(output_file, 'w')

cnt = 0

with open(u'/Users/ashu/Downloads/f.csv') as fd:
    for line in fd:
        line = line.strip()
        if line == '':
            continue
        items = line.split(',')

        if len(items) < 8:
            continue

        user_id, s_id, adress, create_time = items[1], items[4], items[2], items[7]
        # adress = adress.decode('utf-8')
        # print adress


        key = (user_id, s_id)
        # print user_id, s_id

        try:
            create_time = datetime.datetime.strptime(create_time, '%Y/%m/%d %H:%M')
        except:
            create_time = datetime.datetime.strptime('2017/1/1 1:1', '%Y/%m/%d %H:%M')


        if key in dic:
            # print 'key', key
            concel_address, concel_time = dic[key][0][2], dic[key][0][7]
            try:
                concel_time = datetime.datetime.strptime(concel_time, '%Y/%m/%d %H:%M')
            except:
                continue
            if concel_address != adress and (create_time - concel_time).seconds < 3600:
                # output.csv.write(str(dic[key]))
                # output.csv.write(str(items))

                output.write(line + '\n')
                output.write(dic[key][1] + '\n')
                cnt += 1

            # if concel_address != adress:
            #
            #     cnt += 1
            #     print 'target1', items
            #     print 'target2', dic[key]
            #     # print key
            #     # output.csv.write(dic[key])
            #     # output.csv.write(items)


output.close()
print cnt









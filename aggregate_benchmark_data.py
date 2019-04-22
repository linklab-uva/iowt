import os


def main():
    #root_dir = '/home/brandon/Codes/iowt/videos/'

    root_dir = '/home/brandon/Projects/darknet/waste_data/combine videos/brandon + owen videos2'
    distances = [3,5,10,15]
    objs = ['Coke_Can', 'gatorade_bottle', 'water_bottle','Sprite_Can', 'MountainDew_bottle']
    write_file = os.path.join(root_dir, 'all_data.csv')
    num_cams = 3
    write_arr = [["" for _ in range(2)] for j in range(len(distances))]
    detect_objs = ['cup','bottle','person']
    write_str = ""
    write_str += ',' + (str(detect_objs)[1:-1] +',') * len(objs) + '\n'
    header = [[","] for _ in range(3)]
    for j, dist in enumerate(distances):
        dist_str = 'dist_'+str(dist)
        for i in range(num_cams):
            cam_str ='cam_'+str(i)
            header[0].append(cam_str)
            cur_dir = os.path.join(root_dir, cam_str+'/')
            cur_dir =  os.path.join(cur_dir, dist_str+'/')
            for obj in objs:
                header[0].append(',')
                header[1].append(obj + ',')
                file_name = os.path.join(cur_dir, cam_str+'-'+dist_str+'-name_'+obj+'..csv')
                with open(file_name, 'r') as rf:
                    lines = [line for line in rf]
                    line_head = lines[0]
                    lines = lines[1:]
                    for k, line in enumerate(lines):
                        header[0].append(',')
                        header[1].append(',')
                        header[2].append(line_head.rstrip('\n'))
                        line = ",".join(line.split(',')[1:])
                        write_arr[j][k] += line.rstrip('\n')+','
        with open(write_file, 'a+') as wf:
            wf.write(str(dist))
            row_tag = [',mean', ',max']
            for idx, line in enumerate(write_arr[j]):
                wf.write(row_tag[idx] +','+line +'\n')
    with open(write_file, 'r+') as wf:
        wf.seek(0,0)
        content = wf.read()
        wf.seek(0,0)
        num_cols = len(write_arr[0][0].split(','))
        for i,line in enumerate(header):
            line = line[:num_cols]
            join_str = ""
            if i == 2:
                nl = []
                for l in line: nl.extend(l.split(',')[1:])
                line = nl[:num_cols]
                join_str = ','
                wf.write(','+join_str.join(line) + '\n')
            else:
                line.insert(0,',')
                wf.write(join_str.join(line) + '\n')
        wf.write(content)









if __name__ == '__main__':
    main()

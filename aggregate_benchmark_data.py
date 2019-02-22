import os


def main():
    root_dir = '/home/brandon/Codes/iowt/videos/'
    distances = [3,5,10,15]
    objs = ['Coke_Can', 'Gatorade_bottle', 'water_bottle','Sprite_Can', 'MountainDew_bottle']
    write_file = os.path.join(root_dir, 'all_data.csv')
    num_cams = 3
    write_arr = [["" for _ in range(2)] for j in range(len(distances))]
    detect_objs = ['cup','bottle','person']
    write_str = ""
    write_str += ',' + (str(detect_objs)[1:-1] +',') * len(objs) + '\n'
    for j, dist in enumerate(distances):
        dist_str = 'dist_'+str(dist)
        for i in range(num_cams):
            cam_str ='cam_'+str(i)
            cur_dir = os.path.join(root_dir, cam_str+'/')
            cur_dir =  os.path.join(cur_dir, dist_str+'/')
            for obj in objs:
                print(obj)
                file_name = os.path.join(cur_dir, cam_str+'-'+dist_str+'-name_'+obj+'..csv')
                with open(file_name, 'r') as rf:
                    lines = [line for line in rf][1:]
                    for k, line in enumerate(lines):
                        line = ",".join(line.split(',')[1:])
                        write_arr[j][k] += line.rstrip('\n')+','
        with open(write_file, 'a+') as wf:
            wf.write(str(dist))
            for line in write_arr[j]:
                wf.write(','+line +'\n')









if __name__ == '__main__':
    main()
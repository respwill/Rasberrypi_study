
filename = '/home/pi/python_output/myfile.txt'

with open(filename, mode='a') as f:
    f.write('\n is happy!')

with open(filename, mode='r') as f:
    for line in f:
        print(line)

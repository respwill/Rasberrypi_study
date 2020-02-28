# memo.txt 파일 생성 프로그램

with open('memo.csv', 'w') as fo:
    fo.write('kim,'+'10,'+ '20'+ '\n')
    fo.write('lee,'+ '30,'+ '40'+ '\n')
    fo.write('park,'+ '30,'+ '50'+ '\n')



with open('memo.csv', 'r') as fi:
    lines=fi.readlines()
    for line in lines:
        print(line)

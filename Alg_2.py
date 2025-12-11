#Рената Бибишева, алгоритмы ДЗ№2, задание 12

#Идея в том, что сначала все бочки разделены на по группам (какую-то бочку не пьет никто, какую-то один раб, какую-то определенный набор рабов). Одна группа 0-го типа (их не пьет ни один раб), пять групп 1-го типа (ее пьют по одному рабу), 10 групп второго типа (там одну бочку пьет два раба), 10 групп третьего типа (там на одну бочку три раба) и т.д. Поэтому в самом начале я вручную распределяю бочки по рабам.
#Если например отравлена бочка в нулевой группе, то в живых осталось 5 рабов, и на следующий день они способны проанализировать 32 бочки. Если в первой группе - 4 живых раба могут проанализировать 16 бочек и т.д. Поэтому для каждого случая снова распределяю бочки по рабам.


r1 = '1-16; 81-88; 89-96; 97-104; 105-112; 177-180; 181-184; 185-188; 189-192; 193-196; 197-200; 203-204; 205-206; 207-208; 209-210'.split('; ')
r2 = '17-32; 81-88; 113-120; 121-128; 129-136; 165-168; 169-172; 173-176; 189-192; 193-196; 197-200; 201-202; 205-206; 207-208; 209-210'.split('; ')
r3 = '33-48; 89-96; 113-120; 137-144; 145-152; 161-164; 169-172; 173-176; 181-184; 185-188; 197-200; 201-202; 203-204; 207-208; 209-210'.split('; ')
r4 = '49-64; 97-104; 121-128; 137-144; 153-160; 161-164; 165-168; 173-176; 177-180; 185-188; 193-196; 201-202; 203-204; 205-206; 209-210'.split('; ')
r5 = '65-80; 105-112; 129-136; 145-152; 153-160; 161-164; 165-168; 169-172; 177-180; 181-184; 189-192; 201-202; 203-204; 205-206; 207-208'.split('; ')
r = [r1, r2, r3, r4, r5]
for i in r:
    for j in i:
        for k in range(int(j.split('-')[0]), int(j.split('-')[1]) + 1):
            print(k, end = ' ')
    print('')

d = input().split()
dead = []
bochki = []
alive = []
for i in range(5):
    if d[i] == 'D':
        dead.append(r[i])
    else:
        for j in r[i]:
            alive.append(j)
if len(dead) == 0:
    n = 30
    bochki.append('211-240')
if len(dead) == 1:
    n = 16
    for i in dead[0]:
        if i not in alive:
            bochki.append(i)
if len(dead) == 2:
    n = 8
    for i in dead[0]:
        if i in dead[1] and i not in alive:
            bochki.append(i)
if len(dead) == 3:
    n = 4
    for i in dead[0]:
        if i in dead[1] and i in dead[2] and i not in alive:
            bochki.append(i)
if len(dead) == 4:
    n = 2
    for i in dead[0]:
        if i in dead[1] and i in dead[2] and i in dead[3] and i not in alive:
            bochki.append(i)
bochki = range(int(bochki[0].split('-')[0]), int(bochki[0].split('-')[1]) + 1)
if n == 30:
    r1 = [bochki[0], bochki[1], bochki[6], bochki[7], bochki[8], bochki[9], bochki[20], bochki[21], bochki[22], bochki[23], bochki[24], bochki[25], bochki[27], bochki[28]]
    r2 = [bochki[0], bochki[2], bochki[6], bochki[10], bochki[11], bochki[12], bochki[17], bochki[18], bochki[19], bochki[23], bochki[24], bochki[25], bochki[26], bochki[28]]
    r3 = [bochki[0], bochki[3], bochki[7], bochki[10], bochki[13], bochki[14], bochki[16], bochki[18], bochki[19], bochki[21], bochki[22], bochki[25], bochki[26], bochki[27]]
    r4 = [bochki[0], bochki[4], bochki[8], bochki[11], bochki[13], bochki[15], bochki[16], bochki[17], bochki[19], bochki[20], bochki[22], bochki[24], bochki[26], bochki[27], bochki[28]]
    r5 = [bochki[0], bochki[5], bochki[9], bochki[12], bochki[14], bochki[15], bochki[16], bochki[17], bochki[18], bochki[20], bochki[21], bochki[23], bochki[26], bochki[27], bochki[28]]
    r = [r1, r2, r3, r4, r5]
if n == 16:
    r1 = [bochki[0], bochki[1], bochki[5], bochki[6], bochki[7], bochki[12], bochki[13], bochki[14]]
    r2 = [bochki[0], bochki[2], bochki[5], bochki[8], bochki[9], bochki[11], bochki[13], bochki[14]]
    r3 = [bochki[0], bochki[3], bochki[6], bochki[8], bochki[10], bochki[11], bochki[12], bochki[14]]
    r4 = [bochki[0], bochki[4], bochki[7], bochki[9], bochki[10], bochki[11], bochki[12], bochki[13]]
    r = [r1, r2, r3, r4]
if n == 8:
    r1 = [bochki[0], bochki[1], bochki[4], bochki[5]]
    r2 = [bochki[0], bochki[2], bochki[4], bochki[6]]
    r3 = [bochki[0], bochki[3], bochki[5], bochki[6]]
    r = [r1, r2, r3]
if n == 4:
    r1 = [bochki[0], bochki[1]]
    r2 = [bochki[0], bochki[2]]
    r = [r1, r2]
if n == 2:
    r1 = [bochki[0]]
    r = [r1]
    
for i in r:
    for j in i:
        print(j, end = ' ')
    print('')
    
d_new = input().split()
dead_new = []
itog_bochka = None
alive_new = []
for i in range(len(d_new)):
    if d_new[i] == 'D':
        dead_new.append(r[i])
    else:
        for j in r[i]:
            alive_new.append(j)
if len(dead_new) == 0:
    itog_bochka = bochki[-1]

if len(dead_new) == 1:
    for i in dead_new[0]:
        if i not in alive_new:
            itog_bochka = i
if len(dead_new) == 2:
    for i in dead_new[0]:
        if i in dead_new[1] and i not in alive_new:
            itog_bochka = i
if len(dead_new) == 3:
    for i in dead_new[0]:
        if i in dead_new[1] and i in dead_new[2] and i not in alive_new:
            itog_bochka = i
if len(dead_new) == 4:
    for i in dead_new[0]:
        if i in dead_new[1] and i in dead_new[2] and i in dead_new[3] and i not in alive_new:
            itog_bochka = i
            
print(itog_bochka)
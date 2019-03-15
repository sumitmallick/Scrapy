print('Target Impression,  Range: >=1')
target_impressions = int(input("Enter the Input:"))
print('Achieved Impression Range: >=0')
imp_ressions = int(input("Enter the Input: "))
print('Date Range:')
days = int(input("Enter the Input: "))

if target_impressions>0 and target_impressions and imp_ressions:
    get_percent = (imp_ressions/target_impressions)*100
    print(get_percent)
    if get_percent>250:
        status = 'co'
    elif (get_percent>=150 and days>=0 and days<=7) or (get_percent>=50 and days>=22) or (get_percent>=100 and days>=15 and days<=21) or (get_percent>=125 and days>=8 and days<=14):
        status = 'ov'
    elif (get_percent>=120 and get_percent<=150 and days>=0 and days<=7) or (get_percent<=50 and get_percent>=0 and days>=22) or (get_percent>=30 and get_percent<=100 and days>=15 and days<=21) or (get_percent>=100 and get_percent<=125 and days>=8 and days<=14):    
        status = 'ot'
    elif (get_percent<=120 and days>=0 and days<=7) or (get_percent>=50 and get_percent<=119 and days>=8 and days<=14) or (get_percent>=10 and get_percent<=29 and days>=15 and days<=21) or (get_percent<10 and days>=22):
        status = 'un'
    elif (get_percent<100 and days>=0 and days<=7) or (get_percent<=90 and days==8) or (get_percent<=80 and days==9) or (get_percent<=70 and days==10) or (get_percent<=60 and days==11) or (get_percent<=50 and days==12) or (get_percent<=40 and days==13) or (get_percent<=30 and days==14) or (get_percent<=20 and days==15) or (get_percent<=10 and days==16) or (get_percent<=1 and days>=17 and days<=21):
        status = 'cu'
    else:
        status = 'na'
else:
    get_percent = 0
    status = 'na'
print(status)
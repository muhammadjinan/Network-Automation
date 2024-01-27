import csv
# with open('firstcsv.csv','at')as F:
#     csv1 = csv.reader(F)              # Created csv file 'firstscv.scv'
#     print(csv1)
# with open('firstcsv.csv','r')as J:
#     Csv1 = csv.reader(J)
#     for row in Csv1:
#         print(row)                    # Printing csv file in terminal
with open('firstcsv.csv','a',newline='')as H:
    wr=csv.writer(H)
    H = ('Nov','112','223','334')
    wr.writerow(H)  
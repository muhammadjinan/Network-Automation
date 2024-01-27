import csv
with open('csvloop.csv','a',newline='')as A:
    wr = csv.writer(A)
    wr.writerow(['Col1','Col2','Col3'])
    for r in range(1,20):
        wr.writerow([r,r**2,r**3])
    
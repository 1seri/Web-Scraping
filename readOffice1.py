import csv
csvfile1 = 'skedar.csv'
csvfile2 = 'skedarStatik.csv'
def csv_lazy_get(csvfile):
    with open('skedar.csv') as f:
        r = csv.reader(f)
        for row in r:
            yield row

def csv_cmp_lazy(csvfile1, csvfile2):
    gen_2 = csv_lazy_get(csvfile2)

    for row_1 in csv_lazy_get(csvfile1):
        row_2 = gen_2.next()

        print("row_1: ", row_1)
        print("row_2: ", row_2)

        if row_2 == row_1:
            print("row_1 is equal to row_2.")
        else:
            print("row_1 is not equal to row_2.")

    gen_2.close()


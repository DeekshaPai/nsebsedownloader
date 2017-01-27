""" converts the general csv file downloaded from NSE website and BSE website to get the stock names ,which is used as a list
for downloading the relevant csv files of stocks """


""" to do - have to generalize the output file name """

""" input - python ripper.py source_filename """

import csv,sys
with open(sys.argv[1],"rb") as source:
    rdr= csv.reader( source )
    with open("result.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow((r[1],))
print "saved as result"
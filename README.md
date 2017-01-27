# nsebsedownloader


ripper.py - takes the source csv file and extracts the stock name and we use this as a list to download the individal files 
nsebsedownloader - takes the stock names from the ripper.py and downloads the individual file and saves it in a different directory 

how to run :
  go to the directory 
  python ripper.py source_csv_file.csv  ( in this case , source.csv and source1.csv)
  python nsebsedownloader.csv

dependencies :
  urllib (download from anaconda reps)
  os (exists)
  csv (exists)
  sys (exists)

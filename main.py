import datetime

from DuplicateRemover import DuplicateRemover

dirname = "images"
print("Started Time {}".format(datetime.datetime.now()))
# Remove Duplicates
dr = DuplicateRemover(dirname)
dr.find_duplicates()
dr.find_similar(dirname,100)
print("End Time {}".format(datetime.datetime.now()))
# Find Similar Images
############################################################# dr.find_similar("IMG-20110704-00007.jpg", 70)

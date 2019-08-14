rm outfile.csv #remove old
wget http://www.jamessawyer.co.uk/outfile.csv #download sample
#run the downloader to generate your own
#cameras, cameras and more cameras
grep "DVR" outfile.csv > DVR.txt
#search for index of files
grep "Index of" outfile.csv > index_of.txt
#Scary stuff!! Industrial Control systems, France has LOADS!!!
grep "Schneider" outfile.csv > Schneider.txt
grep "Industrial" outfile.csv > industrial.txt
#loads of printers!!!
grep "HP" outfile.csv > printers.txt
#Elastic(search)
grep "search" outfile.csv > search.txt

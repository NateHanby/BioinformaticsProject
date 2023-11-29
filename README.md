# BioinformaticsProject
Code for a project written for BIOL4324 Bioninformatics class

This code is designed to estimate the mutation rate using data from the 1000 Genomes Project. 

import.py: A failed attempt to write code to download and then unzip the data from the FTP site. 
mutation_finder.py: The main code that sorts through the data looking for alleles present in children but not in either of their parents, assumed to be de novo mutations.
output.txt: The output of mutation_finder, a human readable text file with a wealth of information, some of which I used to write my paper.

Workbook:

Steps:

1: I attempted to download and unzip the data files using import.py. 

    This didn't actually work. I don't know why.  The script gave no errors but it also never finished!!
    
2: Since step #1 didn't work, I downloaded FileZilla FTP client and downloaded the file in windows then unzipped it in windows.

3: Identified five sets of family trios (mother, father, child) and listed them at the top of the mutation_finder.py file. 

3: Run mutation_finder.py. 

4: output.txt was generated from mutation_finder, which created all the data that I needed to write my thesis and create the graphs. 

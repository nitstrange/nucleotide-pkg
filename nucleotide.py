from information import table, return_seq

"""Translate a string containing a nucleotide sequence 
into a string containing the corresponding sequence of 
amino acids . Nucleotides are translated in triplets 
using the table dictionary; each amino acid 4 is encoded
 with a string of length 1. """

def nucleotide(filename, location):
    inputfile  =  open(location+filename,"r")
    txt_str =  inputfile.read()

    ## Replace unwanted character
    txt_str = txt_str.replace("\n","")
    txt_str = txt_str.replace("\r","")

    ## Read nucleotide 

    nucleotide  = []
    for i in range(0, len(txt_str), 3):
        #Three letter sequence 
        print(txt_str[i:i+3])
        #Nucleotide 
        if i+3 > len(txt_str):
            print("...")
        else:    
            print(return_seq(txt_str[i:i+3].upper()))
            nucleotide.append(return_seq(txt_str[i:i+3].upper()))
    ## Read nucleotide sequence 
    return nucleotide

#print(nucleotide('sequence.txt','./seq/'))

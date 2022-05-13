#!/usr/bin/python3

import os
import subprocess
import argparse

def infernal(infernal_input,infernal_rfam_db,infernal_output):
	print("Indexing Rfam db to run infernal")
	subprocess.check_output(["cmpress", infernal_rfam_db]) 
	print("Infernal running the cmscan program to annotate RNAs represented in Rfam")
	subprocess.check_output(["cmscan", "--rfam", "--noali", "--tblout", "infernal.tblout", "--fmt", "2", "--clanin", "Rfam.clanin", "Rfam.cm", infernal_input])
	print("Converting infernal tabular output to gff")
	gff = "perl infernal-tblout2gff.pl --cmscan --fmt2 infernal.tblout > {inf}".format(inf = infernal_output)
	os.popen(gff)
	#subprocess.check_output(["perl","infernal-tblout2gff.pl", "--cmscan", "--fmt2", "infernal.tblout", ">", infernal_output])

	return True

parser=argparse.ArgumentParser(description="GenePrediction helper functions which runs individual tools")
parser.add_argument("-i", required=True, help="Path to input file")
parser.add_argument("-o", required=True, help="Path to output folder")
parser.add_argument("-d", required=True, help="Path to Rfam database input")
args=parser.parse_args()

infernal_input = args.i #this takes contigs.fasta as input
infernal_rfam_db = args.d #Rfam.cm is the database input
infernal_output = args.o #converted gff output

infernal(infernal_input,infernal_rfam_db,infernal_output)	

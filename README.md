# Gene Prediction

#### TOOLS USED: 
Prodigal\
Glimmer\
GeneMark-S2\
Infernal\
Blast\
bedtools\
EMBOSS
 
##### Git clone the repository and activate the environment:
```
conda env create -f T1G2_geneprediction.yml
conda activate T1G2_genepred_trial
```
This will activate the required environment for all the tools combined

#####  Download the Rfam CM database to run Infernal for RNA prediction
```
wget ftp://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/Rfam.cm.gz
gunzip Rfam.cm.gz
wget ftp://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/Rfam.clanin
```
### Directory Structure    
```
├── gene_prediction.py
├── bed_tools_merge.py
├── infernal.py
├── data_dir
│   ├── CGT1005
│   │   ├── CGT1005.fasta
│   │   └── CGT1005.fasta.fai
│   └── CGT1029
│       ├── CGT1029.fasta
│       └── CGT1029.fasta.fai
|
├── README.md
├── res
│   ├── blast_final.py
│   ├── g3-from-scratch.csh
│   ├── Glimmer_GFF_conversion.py
│   ├── GlimmerPredict2Gff3.pl
│   ├── infernal.tblout
│   ├── infernal-tblout2gff.pl
│   ├── prodigal.linux
│   ├── run_FragGeneScan.pl
│   └── train
└── T1G2_geneprediction.yml
```
        
Inputs:
```
-i: Path to input file directory (required)
-o: Path to output directory (required)
-refseq: Path to reference sequence file (required)
-db: Path to Rfam database input for infernal tool (required)
-db_blast: Path to store database for blast (required)
```
#### Example:
##### This will run the three ab-initio tools for coding regions we have integrated: GeneMark, Glimmer and Prodigal along with the non coding RNA regions' Infernal.
```
./gene_prediction.py -i data_dir -o <path> -refseq <path> -db <path> -db_blast <path>
```

##### For merging the gff and create the consensus fasta files from them:
```
./bed_tools_merge.py -i data_dir -o <path>
```
This will create the consensus files in the output directory you mention.

#### Files created:
- `final_gene_prediction/`: The output directory which will contains every contigs' assembled genomes.
- `gff_files/`: All gff files from all the tools for each contigs.
- `tmp/`: Temporary files that were created.
- `sorted_gff_files`: Sorted gff files that were created using Bed tools
- `consensus_and_fasta/`: The final consensus files (Ab-initio coding+ non coding RNA) from all the tools.
- `contigs_blast.txt`: Blast result from each contig file.

### Important Files:
- `contigs_consensus.gff` : A .gff file containing a list of all consensus predicted coding genes.
- `contigs_consensus.fna` : A .fna file containing the nucleotide sequence of every predicted gene. 
- `contigs_consensus.faa` : A .faa file containing the translated amino acid sequence of every predicted protein-coding gene. 
- `infernal.fasta` : A fasta file containing nucleotide of all non coding RNA regions using infernal
- `infernal.gff` : A .gff file containing a list of all predicted non-coding RNA regions using infernal

#### The gff, fna and faa files for each of the isolates will be present in their respective directories under consensus_and_fasta directory



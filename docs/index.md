This is out submission for the Wiki Page

Introduction :

Gene Prediction:

  

Identifying the biologically functional subsequences (genes) is crucial in understanding the genome of a species. Gene identification is a problem of self-evident importance and is far from being fully solved. The prediction of protein-coding genes, regulatory regions is termed as Gene Prediction or Gene Finding. It is usually an immediate step after sequencing and assembling a genome. Gene Prediction involved detection of Open Reading Frames, RNA genes and regulatory genes mainly centred on Protein-coding genes. Many bioinformatics tools are developed of reliable automated techniques for predicting genes, yet the accuracy remains unreliable. Our objectives are to verify available (best known) tools for gene prediction, test them on 50 bacterial isolates, compare the accuracy of tools and benchmark them accordingly.

  

Prokaryotic Genome:

  

Bacterial genomes show easily discernible, common architectural principles. They possess small genomes which are tightly packed with protein-coding genes when compared to eukaryotes. Usually the prokaryotic genome is composed of a single, double-stranded DNA molecules which is looped or coiled inside nucleoid. The prokaryotic genome usually is atleast a few million base pairs. The fact that prokaryotes have high gene diversity, is a result of intron absence. The overwhelming majority of bacterial and archaeal proteins are encoded in uninterrupted open reading frames (ORFs).

Few challenges involved in predicting the bacterial genomes:

![](https://lh5.googleusercontent.com/J2FX7HxFWsgCfeFQiXak71wibk--d-e9uZvY3CHr_J6X9SAdmaPF75FabTNkWgh9gCqzW4DrwhRHHZEYl0S36VGErKLM9tmZRiiPLJQo_Nn0xMwduye1o_3iAfxj6qgF3OHMQ-hb)

  

Even when these challenges are present, thankfully accuracy of prokaryotic gene prediction is approximated ~90%.

Tool Validation (Method used to decide final tools in the pipeline)

Initially, for prediction of coding regions in our genome, we chose four tools. In order to increase efficiency of prediction, we used a tool called ORFOrise to validate the performance of the tool against the reference FASTA and annotated GFF file (both obtained from NCBI) of our organism.

-   This tool validates the performance of CDS predictors
    
-   Uses 72 metrics, but there are 12 most important metrics (covered in the next slide)
    
-   Combination of different metrics can be used to evaluate the tool
    
-   Six model organisms with their annotations, 15 prediction tools(ab-initio and model-based)
    

Command:

python3 -m ORForise.Annotation_Compare -dna <reference fasta file> -ref <reference annotation file> -t <tool name> -tp <output file from the tool> -o <output file>

Results from the tool:

(Images to be inserted here)

Based on the results from ORFOrise , we chose to proceed with Prodigal, Glimmer3 and GenemarkS2 for the prediction of coding regions.

For the non-coding regions, we used Infernal to get the prediction.

Gene Prediction takes two major approaches to find genes:

1.  Ab-initio method
    
2.  Homology method
    

  

Methods

  

1.  Ab-initio based gene prediction
    

  

Ab-initio based prediction uses intrinsic features of the sequence to make predictions. The predictions rely on the GC content and signals within the given input query. The most common methods used for Ab-initio based gene prediction are: HMM based, neural networks based, markov-model based and so on. This method has a lower accuracy rate when compared to homology based prediction methods.

The tools that we explored for Ab-initio based methods are:

1.  GeneMarkS2
    

GeneMarkS2 is an improved version of GeneMarkS. It was formulated by Prof. Mark Borodovsky from Georgia Institute of Technology. This tool is used mainly for the prediction of prokaryotes (mainly Archaea and Bacteria). It works by using three periodic Markov chains by iterative self training. This improved version of the tools gives a reduced number of false positives, and dentifies several types of distinct sequence patterns.

Version - GeneMarkS2

Usage - perl gms2.pl --seq <input> --genome-type bacteria --output <output>.gff --format gff

![](https://lh5.googleusercontent.com/W8cqCDb4dBEcH3TCXteIHsi_FCy1Xer2Y-9kMElmct7eUMlLvqViMk5KzJOhgrmXswxhuZZIJMXE7E-EQcNVGQdl0dmuc-HXtH-C1iI8p2k9kfwJVHe4f8VurxA5Mu3g-RaWXwHO)

2.  Prodigal- PROkaryotic Dynamic programming Gene-finding ALgorithm
    

Prodigal constructs a training set for protein coding--GC frame plot based training, and then building log-likelihood coding statistics from training data. The tool works by sharpening coding scores and penalising all potential start candidates that lie downstream from a higher scoring start. Static length factor is added to the coding score while the factor is high in a genome with low GC content. This tool is fast, lightweight and ranks high for the number of perfect matches, and it can be used on finished and draft assemblies.

Version: Prodigal 2.6.3

Usage:

prodigal -a <output path to faa file> -d <output path to fna file> -i <input file path> -f gff -o <output file path>

  

![](https://lh5.googleusercontent.com/uoWvV3yKJWyP3W-gXaM9jQg4sKbVIsFt-i5p097KcFQPAqKdlPE_u53xpBwH7MnT8Ggc1NmDfMOLEv-4xENS6OWWbK8NXE-WJB-_LDk0mSkSEBL4b4I0jgwDIYn9FdEs_SaDFvlS)

3.  FragGeneScan- FragGeneScan, which combines sequencing error models and codon usages in a hidden Markov model to improve the prediction of protein-coding regions in short reads. The performance of FragGeneScan was comparable to Glimmer and MetaGene for complete genomes.
    

  

Usage :

./run_FragGeneScan.pl -genome=sequencefile.fa -out=output -complete=1 -train=complete

  
  

4.  Glimmer - Glimmer is a suite of programs for predicting prokaryotic genomes. Glimmer creates an Interpolated Markov model from a training set of known genes (with very long ORFs) and then using that model it attempts to identify all genes in a DNA sequence.Glimmer3 also uses a Dynamic Programming algorithm to choose the highest scoring set of ORFs and start sites
    

Version- Glimmer 3.0.2

Usage :

./res/g3-from-scratch.csh <path to input> out

![](https://lh6.googleusercontent.com/-9UeFoJKk1pACMn-op7aC091FqgoO4UxNuR1euNsrsjy6O2h-1iJMDLcEpCgepoKhAVLRcjIHWvfcLQw18LeJbKQ6tkRFkcNal05TZ-USduDLLGeOhynvL6oQj291SvU7JrrlAMc)

  

2. Homology Based Tools

Homology-based: these methods predict a gene using the alignment of a protein (or RNA sequence in the form of full-length mRNA, cDNA or EST) with the genome sequence that we want to annotate. The known sequence (also called evidence) guides the prediction.

1.  BLAST
    

Basic Local Alignment Search Tool finds regions of similarity between biological sequences

BLAST increases the speed of alignment by decreasing the search space or number of comparisons it makes. Specifically, instead of comparing every residue against each other, BLAST uses short "word" (w) segments to create alignment "seeds.

  

Version

Usage :

makeblastdb —in refseq —dbtype nucl —out database

blastn -query inputq_se -db database -out out.txt

3. Non-coding Prediction tools:

Noncoding RNAs (ncRNAs) play important roles in various cellular activities and diseases, they are functionally significant and abundant. ncRNAs are classified into different categories based on their functions and lengths including transfer RNA (tRNA), ribosomal RNA (rRNA), microRNA (miRNA), and long ncRNA (lncRNA) etc.

1.  Infernal
    

Infernal ("INFERence of RNA ALignment") is for searching DNA sequence databases for RNA structure and sequence similarities.It uses Covariance Models and probabilistic profiles of the sequence and the secondary structure of the RNA.It is more capable of identifying RNA homologs that conserve their secondary structure more than their primary sequence

Version: 1.1.4

Usage :

cmscan --rfam --noali --tblout infernal.tblout --fmt --clanin Rfam.clanin Rfam.cm infernal_input

  

![](https://lh6.googleusercontent.com/-l7HtjWsw3DtPjFGoYN1jEEZlJ1RM2--gNRC8kIepZAaEe51AuQdyB3ZXP8ScMsc8uweGOJsQ51BuGe2iXZZB23Mq2FNeVQ7XPbEa7l5OFSR98LQJCRDwYyl-f3MvfSz-nIK3XgH)

Since Infernal outperformed Aragorn in tRNA prediction, Infernal was chosen for the final pipeline.

![](https://lh6.googleusercontent.com/iA2YGowJcnaFZuXq4EuVn0dfoo0iWlJjPkqOSBjKtpoS9wf-MNXf19irJ7XE6SjpdGl_1uh-4VzZBPU6u57hLzt4mnJkzAzpBSbhvA0rTMxo9nUCsYoF8NsXllINthdno2SThj7K)

  
  
  

Prediction validation

1.  Abstract:
    

In order to evaluate the accuracy and sensitivity of 3 ab-initio tools, GffCompare is utilized to conducted prediction validation against reference genomes downloaded from NCBI.

By comparing the Gff files of gene prediction reuslts to GFF3 files of reference genomes, Gffcompare will report various statistics related to the accuracy and snesitivity. The computational process is shown as follow:

Sensitivity = TP / (TP+FN)

Accuracy = TP / (TP+FP)

* TP: True positive, FN: False negative, FP: False positive.

2.  Command:
    

gffcompare -r [qeury sequence.gff/gtf] [reference sequence.gff/gtf]

  

3.  Results:

Table 1 Gene validation output of Prodigal and GeneMarkS2 using GffCompare.
<img width="609" alt="image" src="https://github.gatech.edu/storage/user/56853/files/012bca24-458a-4498-ae7b-51f8569bff16">


  

4.  Notes:
    

The output of Glimmer3 can only be in the format of .predict or .fasta extracted from input. When file.gff can be obtained, we will conduct GffCompare to validate Glimmer3 results. Considering that Glimmer3 still has outstanding value in other evaluation, it will still be utilized in our final pipeline.

  

The final pipeline :

![](https://lh6.googleusercontent.com/R-h4Rkxt4LDaONLWJVODLl8k0YNHS7jFFfaFJxsXqCZc6IOA937jLDckPLA7GHVsTdAyG4iAU__nGVXsvOODjjYCMyjno42JT8BPBsXBQngBWZTf_bn9jygAgrDCRBNrN0_hgdFH)

  

Results and graphs

  
  
  

References:

1.  Lomsadze A, Gemayel K, Tang S, Borodovsky M. Modeling leaderless transcription and atypical genes results in more accurate gene prediction in prokaryotes.
    
2.  Maji, Srabanti, and Deepak Garg. "Progress in Gene Prediction: Principles and Challenges." (Strategy)
    
3.  Sommer MJ, Salzberg SL. Balrog: A universal protein model for prokaryotic gene prediction, PLoS Comput Biol. 2021 Feb)
    
4.  Arthur L. Delcher, Kirsten A. Bratke, Edwin C. Powers, Steven L. Salzberg, Identifying bacterial genes and endosymbiont DNA with Glimmer, Bioinformatics
    
5.  Silva, R., Padovani, K., Góes, F. et al. geneRFinder: gene finding in distinct metagenomic data complexities. BMC Bioinformatics 22, 87 (2021).
    
6.  Dimonaco NJ, Aubrey W, Kenobi K, Clare A, Creevey CJ. No one tool to rule them all: Prokaryotic gene prediction tool annotations are highly dependent on the organism of study. Bioinformatics. 2021 Dec 7;38(5):1198–207.
    
7.  Hyatt D, Chen GL, Locascio PF, Land ML, Larimer FW, Hauser LJ. Prodigal: prokaryotic gene recognition and translation initiation site identification. BMC Bioinformatics. 2010 Mar 8;11:119. doi: 10.1186/1471-2105-11-119.
    
8.  Rho M, Tang H, Ye Y. FragGeneScan: predicting genes in short and error-prone reads. Nucleic Acids Res. 2010 Nov;38(20):e191. doi: 10.1093/nar/gkq747.
    
9.  Trimble WL, Keegan KP, D'Souza M, Wilke A, Wilkening J, Gilbert J, Meyer F. Short-read reading-frame predictors are not created equal: sequence error causes loss of signal. BMC Bioinformatics. 2012 Jul 28;13:183.
    
10.  Laslett D, Canback B. ARAGORN, a program to detect tRNA genes and tmRNA genes in nucleotide sequences. Nucleic Acids Res. 2004 Jan 2;32(1):11-6. doi: 10.1093/nar/gkh152. PMID: 14704338; PMCID: PMC373265.
    
11.  Monica- Andreea Drăgan, Ismail Moghul, Anurag Priyam, Claudio Bustos, Yannick Wurm, GeneValidator: identify problems with protein-coding gene predictions, Bioinformatics, Volume 32, Issue 10, 15 May 2016, Pages 1559–1561, [](https://doi.org/10.1093/bioinformatics/btw015) 11. Rho M, Tang H, Ye Y. FragGeneScan: predicting genes in short and error-prone reads. Nucleic Acids Res. 2010 Nov;38(20):e191.
    
12.  Eric P. Nawrocki, Diana L. Kolbe, Sean R. Eddy, Infernal 1.0: inference of RNA alignments, Bioinformatics, Volume 25, Issue 10, 15 May 2009, Pages 1335–1337.
    
13.  Buchfink, B., Xie, C. & Huson, D. Fast and sensitive protein alignment using DIAMOND. Nat Methods 12, 59–60 (2015).
    
14.  Pertea G and Pertea M. GFF Utilities: GffRead and GffCompare [version 1; peer review: 3 approved]. F1000Research 2020, 9:304
    
15.  Burset M, Guigo R. Evaluation of gene structure prediction programs. genomics. 1996 Jun 15;34(3):353-67.

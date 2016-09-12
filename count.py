
# coding: utf-8

# In[ ]:

#useage python count.py > output.txt
import pysam
bamfile = pysam.Samfile("/path/to/bam/.bam", "rb") #change the path to bam file accordingly. Requires indexed bam file. If not, run samtools index .bam
for pileupcolumn in bamfile.pileup( 'chr8', 85814259, 85814260): # genomic location for the snp
    for pileupread in pileupcolumn.pileups:
        if pileupcolumn.pos == 85814259:
            base = pileupread.alignment.seq[pileupread.qpos]
            print base


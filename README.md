# Metagenomics
Gut Health
## contigs assembly
SOAPdenovo-63mer pregraph -s config.txt -K 39 -d 1 -R -oK.39 -p 40 1>pregraph.log1 2>pregraph.err1
SOAPdenovo-63mer contig -g K.39 -p 40 1>contig.log1 2>contig.err

SOAPdenovo-63mer map -p 20 -s scaffold.cfg -g K.39 1>map.lot1 2>map.err
SOAPdenovo-63mer scaff -p 20 -L 200 -g K.39 1> scaff.log 2>scaff.err

GapCloser -a $line.k.39.scafSeq -b scaffold.cfg -o gap_remove.scatigs
2bwt-builder scatigs

soap -a ${sample}.1.cl.fq -b ${sample}.2.cl.fq -D ${sample}.gap_remove.contigs.index -o blast -u ${sample}.unmap -m 200 -2 Single_output

## gene prediction
diamond blastp --query ../5_calculate_reads_counts/unigene.mix.liu.faa --db NR.gi/nr --outfmt 6 --threads 40 --out NR.blast --evalue 1e-5 --block-size 20.0
python fil_evalue.py NR.blast -o NR.blast.filter

## annotation
hmmscan contig.results > CAZyme.dbCAN

import urllib.request
import gzip
import shutil

#I don't know why this doesn't work. I ended up just downloading the file manually with an FileZilla FTP client and then unzipping it in windows!
urllib.request.urlretrieve("ftp://ftp.1000genomes.ebi.ac.uk//vol1/ftp/release/20130502/supporting/hd_genotype_chip/ALL.chip.omni_broad_sanger_combined.20140818.snps.genotypes.vcf.gz", 
                           'ALL.chip.omni_broad_sanger_combined.20140818.snps.genotypes.vcf.gz')

with gzip.open('ALL.chip.omni_broad_sanger_combined.20140818.snps.genotypes.vcf.gz', 'rb') as zipped_file:
     with open('file.txt', 'wb') as new_file:
        shutil.copyfileobj(zipped_file, new_file)

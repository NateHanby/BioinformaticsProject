import urllib.request

urllib.request.urlretrieve("ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20201028_3202_raw_GT_with_annot/20201028_CCDG_14151_B01_GRM_WGS_2020-08-05_chr12.recalibrated_variants.vcf.gz", 
                           'child_chr_12.gz')
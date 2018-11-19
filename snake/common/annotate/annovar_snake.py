## annovar functionally annotate genetic variants detected

# table_annovar.pl takes an input VCF file and generate a tab-delimited output file with many columns, 
# each representing one set of annotations.
# if the input is a VCF file, the program also generates a new output VCF file with the INFO field filled with annotation information.

if not 'ANNOVAROUT' in globals():
    ANNOVAROUT = OUTDIR + 'annovar/'

rule table_annovar:
    input:
        vcf = HAPLOTYPECALLEROUT + '{sample}.vcf',
    output:
        vcf = ANNOVAROUT+ '{sample}.hg19_multianno.vcf'
    params:
        lsfoutfile = ANNOVAROUT + '{sample}.anno.lsfout.log',
        lsferrfile = ANNOVAROUT + '{sample}.anno.lsferr.log',
        mem = config['tools']['annovar']['mem'],
        prefix = ANNOVAROUT + '{sample}',
        humandb = config['resources'][ORGANISM]['annovarhumandb'],
        params = config['tools']['annovar']['params'],
        protocol = config['tools']['annovar']['protocol'],
    threads:
        config['tools']['annovar']['threads']
    benchmark:
        ANNOVAROUT + '{sample}.anno.benchmark'
    log:
        ANNOVAROUT + '{sample}.anno.log'
    shell:
        ('{config[tools][annovar][call]} ' +
        '{input.vcf} ' +
        '{params.humandb} ' +
        '-out {params.prefix} ' +
        '{params.params} ' +
        '-protocol {params.protocol}') 


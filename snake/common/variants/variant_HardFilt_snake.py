# manipulate vcf files

# SelectVariants: 
# Select a subset of variants from a larger callset
# Category：Variant Manipulation Tools

# select snps && indels from one vcf
rule gatkSelectVariants:
    input:
        vcf = HAPLOTYPECALLEROUT + '{sample}.vcf',
        reference = config['resources'][ORGANISM]['reference'],
    output:
        snpsvcf = HAPLOTYPECALLEROUT + '{sample}_snps.vcf',
        indelsvcf = HAPLOTYPECALLEROUT + '{sample}_indels.vcf'
    params:
        lsfoutfile = HAPLOTYPECALLEROUT + '{sample}_snps_indels.vcf.lsfout.log',
        lsferrfile = HAPLOTYPECALLEROUT + '{sample}_snps_indels.vcf.lsferr.log',
        scratch = config['tools']['GATK']['SelectVariants']['scratch'],
        mem = config['tools']['GATK']['SelectVariants']['mem'],
        time = config['tools']['GATK']['SelectVariants']['time'],
        reference = config['resources'][ORGANISM]['reference'],
        params = config['tools']['GATK']['SelectVariants']['params'],
    threads:
        config['tools']['GATK']['SelectVariants']['threads']
    benchmark:
        HAPLOTYPECALLEROUT + '{sample}_snps_indels.vcf.benchmark'
    log:
        HAPLOTYPECALLEROUT + '{sample}_snps_indels.vcf.log'
    shell:
        ('{config[tools][GATK][call]} ' +
        '-T SelectVariants ' +
        '{params.params}' +
        '-R {input.reference} ' +
        '-selectType SNP ' +
        '--variant {input.vcf} ' +
        '-o {output.snpsvcf} ' +
        '&& ' + 
        '{config[tools][GATK][call]} ' +
        '-T SelectVariants ' +
        '{params.params}' +
        '-R {input.reference} ' +
        '-selectType INDEL ' +
        '--variant {input.vcf} ' +
        '-o {output.indelsvcf} ' )

# Apply the filter to the SNP call set
rule gatkVariantFiltrationForSNP:
    input:
        vcf = HAPLOTYPECALLEROUT + '{sample}_snps.vcf',
        reference = config['resources'][ORGANISM]['reference'],
    output:
        vcf = HAPLOTYPECALLEROUT + '{sample}_filtered_snps.vcf',
    params:
        lsfoutfile = HAPLOTYPECALLEROUT + '{sample}_filtered_snps.vcf.lsfout.log',
        lsferrfile = HAPLOTYPECALLEROUT + '{sample}_filtered_snps.vcf.lsferr.log',
        scratch = config['tools']['GATK']['VariantFiltration']['scratch'],
        mem = config['tools']['GATK']['VariantFiltration']['mem'],
        time = config['tools']['GATK']['VariantFiltration']['time'],
        reference = config['resources'][ORGANISM]['reference'],
        params = config['tools']['GATK']['VariantFiltration']['params'],
        filterexpression = config['tools']['GATK']['VariantFiltration']['snpfilterexpression']
    threads:
        config['tools']['GATK']['VariantFiltration']['threads']
    benchmark:
        HAPLOTYPECALLEROUT + '{sample}_filtered_snps.vcf.benchmark'
    log:
        HAPLOTYPECALLEROUT + '{sample}_filtered_snps.vcf.log'
    shell:
        ('{config[tools][GATK][call]} ' +
        '-T VariantFiltration ' +
        '{params.params}' +
        '--variant {input.vcf} ' +
        '-R {input.reference} ' +
        '--filterExpression "{params.filterexpression}" ' +
        '--filterName "BCH_snp_filter" ' +
        '-o {output.vcf}')

# Apply the filter to the Indel call set
rule gatkVariantFiltrationForIndel:
    input:
        vcf = HAPLOTYPECALLEROUT + '{sample}_indels.vcf',
        reference = config['resources'][ORGANISM]['reference'],
    output:
        vcf = HAPLOTYPECALLEROUT + '{sample}_filtered_indels.vcf',
    params:
        lsfoutfile = HAPLOTYPECALLEROUT + '{sample}_filtered_indels.vcf.lsfout.log',
        lsferrfile = HAPLOTYPECALLEROUT + '{sample}_filtered_indels.vcf.lsferr.log',
        scratch = config['tools']['GATK']['VariantFiltration']['scratch'],
        mem = config['tools']['GATK']['VariantFiltration']['mem'],
        time = config['tools']['GATK']['VariantFiltration']['time'],
        reference = config['resources'][ORGANISM]['reference'],
        params = config['tools']['GATK']['VariantFiltration']['params'],
	filterexpression = config['tools']['GATK']['VariantFiltration']['indelfilterexpression']
    threads:
        config['tools']['GATK']['VariantFiltration']['threads']
    benchmark:
        HAPLOTYPECALLEROUT + '{sample}_filtered_indels.vcf.benchmark'
    log:
        HAPLOTYPECALLEROUT + '{sample}_filtered_indels.vcf.log'
    shell:
        ('{config[tools][GATK][call]} ' +
        '-T VariantFiltration ' +
        '{params.params}' +
        '--variant {input.vcf} ' +
        '-R {input.reference} ' +
        '--filterExpression "{params.filterexpression}" ' +
        '--filterName "BCH_indel_filter" ' +
        '-o {output.vcf}')















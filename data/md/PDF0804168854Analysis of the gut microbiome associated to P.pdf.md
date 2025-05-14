# Analysis of the gut microbiome associated to PVC biodegradation in yellow mealworms

## Jianquan Xu \({ }^{a, *}\), Yongquan Dong \({ }^{b}\)

\({ }^{a}\) Jiangxi Modern Institute of Vocational Technology, Nan Chang 330095, China

\({ }^{b}\) College of Environmental and Chemical Engineering, Nanchang Hangkong University, Key Laboratory of Jiangxi Province for Persistent Pollutants, Nan Chang 330063, China

## Article Info

Edited by Dr G Liu

Keywords: Yellow mealworms PVC Biodegradation Gut microbiome Function Structure

## Abstract

The potential of invertebrates in the biodegradation of plastic polymers such as polyvinyl chloride (PVC) is receiving increasing attention. The present study is aimed to identify the gut microbiome involved in this degradation in yellow mealworms, i.e., the larvae of \(T\) enebrio molitor Linnaeus. The egested PVC polymer experienced a dramatic reduction in both number average molecular weight (Mn) and weight average molecular weight (Mw) of 99.3\% and 99.6\%, respectively, whereas FTIR analysis revealed chemical alterations. Mass spectrometry analysis identified two potential degradation products: phthalic acid, di(2-propylpentyl) ester and 2-Propenoic acid, tridecyl ester. Further, we used metagenomic sequencing to elucidate the response of the gut microbiome when transitioning from bran to PVC as a food source, identifying four microorganisms actively involved in PVC degradation. Additionally, metagenomic functional analysis of the gut microbiome identified 111 key gene modules that were significantly enriched. In summary, our findings suggest that yellow mealworms adapt to PVC degradation by modifying their gut microbiome both structurally and functionally.

## Introduction

For the last several decades, plastic waste has been a significant environmental concern (Gautam et al., 2007a). Global production of petroleum-based synthetic plastics reached 390.7 million tons in 2021 (Tmi Group, 2022). Resistance to biodegradation has been observed in six commonly used plastic polymers: polypropylene (PP), polyethylene (PE), polyurethane (PUR), polyvinyl chloride (PVC), polyethylene terephthalate (PET) and polystyrene (PS) (Wu et al., 2017). In Europe, the market share of PVC (10.3\%) is comparable to that of PP (19.8\%) and PE (29.4\%), based on polymer demand (Tmi Group, 2022). However, conventional disposal methods such as landfill and incineration cannot fundamentally resolve the pollution problem associated with plastic waste (Zhang et al., 2021), urging the development of more sustainable and eco-friendly treatment approaches (Shen et al., 2020).

Plastic degradation has intrigued scientists since the 1960s (Amass et al., 1998; Omari et al., 1974) and recently, focus has shifted towards the potential role of invertebrates. Indeed, superworms (Zophobas atratus) can breakdown and convert PS into minerals, and each superworm can consume about 0.58 mg styrofoam daily (Yang et al., 2020b). Also, Indian mealmoths (Plodia interpunctella) larvae can consume PE films (Yang et al., 2014). The greater wax moth \(G\) alleria mellonella consumed 92 mg of PE over a 12-hour period (Bombelli et al., 2017). One hundred lesser waxworms (Achroia grisella) degraded 43\% of high-density polyethylene (HDPE) over a span of twenty-eight days, with a survival rate of about 75\% (Kundungal et al., 2019). Finally, land snails (Achatina fulica) can ingest about 20 mg of polystyrene within a four-week period. These snails subsequently expelled microplastics in their fecal samples, resulting in a 30\% plastic mass loss (Song et al., 2020; Ballitoc and Sun, 2013).

Yellow mealworms are the larvae of Tenebrio molitor Linnaeus (hereafter referred to as \(T\). molitor), an insect species within the Tenebrionini tribe. These larvae have a high content of protein and fat (Allen et al., 2012). Accordingly, they are being commercialized as animal feed, and can potentially be used for human consumption (Ballitoc and Sun, 2013; Borremans et al., 2020). However, these larvae can also breakdown various plastics like PS (Yang et al., 2015a; Yang et al., 2015b; Yang et al., 2018a; Yang et al., 2018b; Jiang et al., 2021), PE (Brandon et al., 2018a; Bulak et al., 2021; Yang et al., 2021a), PVC (Peng et al., 2020), PUR (Orts et al., 2022; Liu et al., 2022) and PP (Yang et al., 2021b). This remarkable ability to degrade plastics has been attributed to their symbiotic intestinal microbes (Engel, 2013).

* Correspondence to: Jiangxi Modern Institute of Vocational Technology, Nan Chang, Jiangxi, 330095, China. E-mail address: newwebmen@163.com (J. Xu).

https://doi.org/10.1016/j.ecoenv.2024.116046

Received 27 September 2023; Received in revised form 18 January 2024; Accepted 27 January 2024

Available online 2 February 2024

0147-6513/© 2024 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

Styrofoam is degraded by microorganisms in the larval gut and transformed into carbon dioxide with a retention period of under 24 h (Yang et al., 2015a; Yang et al., 2015b). Furthermore, yellow mealworms possess an inherent capacity for breaking down LDPE, with shifts in intestinal flora toward communities associated with LDPE biodegradation (Yang et al., 2021a). The consumption of polyether-PU foams by T. molitor led to a 67% reduction in mass (Liu et al., 2022). Analysis of the gut microbiome in yellow mealworms by high-throughput sequencing revealed shifts in microbial communities (Yu et al., 2021).

However, despite the progress in biodegradation research for PE (Yang et al., 2014; Restrepo-Flórez et al., 2014; Sen and Raut, 2015; Montazer et al., 2020; Ru et al., 2020), PET (Tournier et al., 2020; YOSHIDA et al., 2016; YUAN et al., 2018) and PS (Peng et al., 2019b; Brandon et al., 2018a; Božek et al., 2017), less is known of PVC biodegradation. It is known that yellow mealworms can consume PVC plastic, and degradation was analyzed by NMR, gel permeation chromatography or FTIR (Wu et al., 2019; Peng et al., 2020). These studies also revealed shifts in the gut microbial communities responsible for PVC degradation and the intricate connections between microbial structure and function controlling PVC breakdown is still limited. All previous investigations into the plastic-degrading abilities of yellow mealworms were conducted under gregariously rearing conditions, neglecting the fact that these larvae would resort to cannibalism in the absence of regular food, potentially affecting their plastic consumption. Given that insect gut microbiomes are influenced by their diets (Huang et al., 2021; Yu et al., 2021) and plastic biodegradation by insect larvae has been linked to microbial populations (Pivato et al., 2022; Przemieniecki et al., 2020), the interpretation of previously reported shifts in gut microbial communities is challenging.

Hence, the present study has the following aims: (i) to explore the capability of yellow mealworms to survive on PVC when provided as their sole diet in isolated feeding conditions and (ii) elucidate the species of bacteria, their function and structure, associated with PVC degradation.

\section*{2. Materials and methods}

\subsection*{2.1 Mealworm survival, plastic consumption, and insect dissection}

Yellow mealworms at the developmental stage of 5-7 instars and approximately \(2 \mathrm{~cm}\) in length were procured from Nanchang Insect Breeding Plant (Jiangxi, China). On the basis of morphology and coloration, the species of larvae were identified as Tenebrio molitor Linnaeus (Robinson, 2005; Calmont and Soldati, 2008). These larvae were cultured indoors and were sustained by a diet of bran for five days in a controlled environment (humidity of \(60 \pm 5 \%\), temperature of \(25^{\circ} \mathrm{C}\) and darkness). Following this, the larvae were subjected to a 72-hour period of starvation to allow the egestion of prior feedstock frass, before initiating the experimental diet. The natural wheat bran used was sourced online from Pinshuo Trading (Huaian, Anhui).

To assess the viability of the larvae when consuming PVC, initial tests were conducted to evaluate survival rates and weight changes. One hundred larvae were divided into three groups: (i) the PVC group (fed with PVC film, \(n=60\) ), (ii) the bran group (fed with bran, \(n=30\) ) and (iii) the control group (starved, \(n=10\) ). Each larva was housed in a separate \(90 \mathrm{~mm}\) diameter Petri dish with the same controlled conditions described above (Fig. 1a) for eight days, when the body weights were recorded. On the eighth day, surviving larvae from the bran and PVC groups were chilled on ice to reduce their activity, treated with \(70 \%\) alcohol for 2 min, and followed by triple rinses with sterile water (Zhang et al., 2022). The intestines were gently extracted after clamping and

\section*{Fig. 1. Laboratory cultivation of T. molitor feeding on bran and PVC. (a) Tenebrio molitor L. fed with bran (1) and PVC (2) in Petri dishes; (b, c) cumulative survival (b) and weight loss (c) of larvae in PVC, bran and control starved groups.}

Commercial PVC film (0.1 mm thick) with plasticizer content of 28% was procured from the Packaging Factory (Lingyi, Shandong). The plastic film was cut into uneven squares of about 3 × 3 cm, exposed to an air stream to eliminate any residues (Brandon et al., 2018b) and placed in the container. The composition of the PVC film was quantitatively analyzed by PY-GCMS (Pyrolyzer: Frontier Lab EGA-PY-3030D; GC-MS: Shimadzu GCMS-QP2020NX), with the following detection parameters: cleavage temperature, 610 °C; cleavage time, 0.2 min; column Rtx-5 MS (30 m, 0.25 mm ID, 0.25 μm); inlet temperature, 300 °C; carrier gas = helium; flow rate = 1 mL/min; shunt ratio = 40:1. The heating up program was set as follows: initial temperature of 40 °C held (3 min), increase to 140 °C (10 °C/min), increase to 310 °C (20 °C/min), held for 8 min; ion source temperature: 230 °C, interface temperature: 310 °C, ionization mode: electron bombardment (70 eV), acquisition time: 28 min, scanning range: 29–600 m/z.

To assess the plastic depolymerization within the frass, we used gel permeation chromatography (GPC). The molecular weights (both number-averaged [Mn] and weight-averaged [Mw]) of the fragments were quantified using an Agilent 1260 Infinity II GPC/SEC system, following established protocols (Peng et al., 2020). Tetrahydrofuran (THF) (10 mL) was used to dissolve PVC (0.05 g) or frass specimens (0.05 g) by stirring for 2 h in a magnetic stirrer under gentle heating. The extract was filtered with a 0.22 μm PVDF sterile syringe filter, transferred to a clean 15-mL glass vial, and the THF was evaporated with nitrogen gas. The remaining polymer residue was weighed to determine the THF extractable fraction. The polymer residue was then resuspended in THF to 5 mg/mL. A sample of this solution (60 μL) was injected into the GPC analyzer at 0.80 mL/min and results were obtained in triplicate. To examine the chemical alterations at the surface of the residual PVC fragments we used FTIR spectroscopy (Thermo Scientific iN10 FTIR Spectrometer with OMNIC software, v9.12.928). Frass samples were freeze-dried for at least 36 h and ground with KBr to prepare a homogeneous KBr pellet (Peng et al., 2019a). Spectra (32 scans each) were collected in the range 4000–500 cm−1. For GC-MS analysis (Zhang et al., 2022), intestinal feces were subjected to ultrasonic processing with THF, followed by concentration to 0.5 mL and combination with 1 mL n-hexane. This solution underwent temperature-programmed injection (40 °C to 280 °C) into the GC-MS system. Detector conditions were maintained at 250 °C transfer-line-temperature, 280 °C ion-source-temperature, 70 eV ionization-mode-electron-impact and 0.3 s scan-time.

Genomic DNA was isolated from intestinal specimens using the MagPure-Soil-DNA-KF-Kit (Magen, Guangzhou, China). The yield and integrity of the DNA were examined using a NanoDrop2000 spectrophotometer (Thermo-Fisher-Scientific, USA) and 1% agarose-gel electrophoresis. The extracted DNA was divided into two aliquots and kept at −80 °C in preparation for subsequent metagenome and 16S rRNA sequencing.

DNA underwent fragmentation using S220 Focused-ultrasonicators (Covaris, USA) and subsequent purification was carried out employing Agencourt-AMPure-XP-beads (Beckman Coulter Co., USA). Following this, libraries were constructed using the TruSeq-Nano-DNA-LT-Sample-Preparation-Kit (Illumina, USA). The Metagenome sequencing and subsequent analyses were performed by OE Biotech company (Shanghai, China).

In total, a collection of 346 million paired-end reads was amassed, with each sample having an average of 115.38 million reads (s.e.) (Table S1). The raw metagenomic data for PVC were deposited in the NCBI SRA database, under the BioProject accession number PRJNA579552.

Initially, raw reads were subjected to quality enhancement and trimming using fastp (https://github.com/OpenGene/fastp). This involved the removal of adapter sequences from the 3' and 5' ends (Noguchi et al., 2006), as well as elimination of low-quality reads (e.g., reads with a quality threshold below 20 and reads <50 bp). As a result of this process, each sample produced an average of 114.22 ± 14.77 million clean reads, achieving coverage of 99.00 ± 0.06% (Table S1).

Subsequently, to address host contamination, the host genome was used as a reference for aligning the pair-end reads after filtering (Tenebrio molitor Tenebrio molitor_v3) available on the NCBI website using bowtie2 (v 2.2.9). The aligned reads were discarded, resulting in an average of 6.27 ± 1.19 million valid reads per sample (Table S2).

To establish the gene catalogue, valid sequences were assembled from each specimen into contigs (reads >500 bp) utilizing MEGAHIT (v1.1.2) (Dinghua et al., 2015). The prediction of open reading frames (ORFs) within contigs was accomplished using Prodigal (v2.6.3) (Hyatt et al., 2010). To acquire a non-redundant gene catalogue, pairwise comparison of ORFs was carried out using CD-HIT (v4.5.7).

The metagenomic datasets were subjected to distinct methodologies for species and functional classification. In the initial step, gene sequences were aligned to the NR database employing Bowtie2 (Version 2.2.9). This alignment to the NR database was executed in two stages: First, genes were aligned to the NR database using Bowtie2. Subsequently, the best match to a related phylogenetic group (with criteria of >95% identity and >90% query overlap) was employed to attribute each metagenomic species to a taxonomic category spanning from genus to class level. A stringent threshold of >90% of genes within a given species was required to establish this assignment. For visualizing the taxonomic composition and abundance profiles, the "vegan" package within the R programming environment was harnessed. In parallel, functional profiling was achieved through the utilization of DIAMOND (v0.9.7) to map genes against the KEGG database. This process allowed the creation of comprehensive functional profiles by matching genes to KEGG annotations, thereby providing insights into the potential biological pathways and functions encoded within the metagenomic data (Buchfink et al., 2015).

For bacterial sequencing, we aimed to analyze the 16S rRNA coding V3-V4 hypervariable regions utilizing the second aliquot of nonfragmented DNA. To achieve this, we employed primers 343F (5'-TACGGRAGGCAGG-3') and 798R (5'-AGGGTATCTAATCTCT-3'). For fungal analysis, the ITS1F (5'-ACTTGGTCAATTTAGGAAGTAA-3') and ITS2R (5'-BGCCTGGTTCTCTATCGATGC-3') primers were utilized to amplify the fungal ITS rRNA genes. DNA amplification was conducted using a thermocycler-PCR-system (GeneAmp 9700, USA), and the resulting PCR products underwent purification, mixing, and subsequent submission to OE Biotech Company for further processing and sequencing using an Illumina NovaSeq 6000 system (USA). The raw sequencing data were acquired in FASTQ format. To ensure data quality, the paired-end reads underwent initial processing using the Cutadapt software to identify and eliminate adapter sequences. After this initial step, the paired-end reads underwent further refinement including removal of low-quality sequences, denoising, merging of overlapping reads, and identification and removal of chimera reads. This entire

\section*{3. Results}

\subsection*{3.1. Tenebrio molitor can feed on PVC}

Upon completion of the 8-day observation period, the survival of the larvae in the control starved group was the lowest (50\%), followed by the PVC group (55\%) and the bran group (67\%) (Fig. 1b). The survival of the larvae in different group is consistent with the statistically significant alterations in body weight: starvation \((-7.5 \pm 3.1 \%)<\) PVC \((-4.7\) \(\pm 1.7 \%)<\) Bran \((25.3 \pm 12.6 \%)\) (Fig. 1c). The above results suggest that PVC film supplies energy to the larvae, extending larval survival.

\subsection*{3.2. Depolymerization and biodegradation of PVC}

At the end of the 8-day, PVC mass reduction and PVC mass reduction rate were \(1.0 \pm 0.8 \%\) and \(6.7 \pm 5.0 \mathrm{mg} / 100\) larvae-d (Fig. 2a). The THF extractable fraction of the frass was \(35.3 \pm 3.7 \%\), indirectly indicating that PVC is degraded in the mealworm gut (Fig. 2b).

GPC was used to assess the degree of PVC depolymerization. Both Mw and Mn in the PVC group were reduced (99.6\% and 99.3\%) compared to control PVC (Fig. 2c), which is consistent with previous studies (Peng et al., 2020).

Infrared spectra revealed chemical changes in the remaining polymers recovered from the frass. In the PVC group, new functional groups appeared such as \(-\mathrm{C}=\mathrm{O}(1900-1600 \mathrm{~cm}^{-1})\) and hydroxyl \((3500-3300 \mathrm{~cm}^{-1})\), indicating capacity to degrade PVC film through an oxidative process, consistent with previous studies (Gautam et al., 2007b; Peng et al., 2019b; Singh and Sharma, 2008) (Fig. 3). Additionally, the absorbance of the peak at \(613 \mathrm{~cm}^{-1}\) was reduced compared to control PVC implying a reduction in \(-\mathrm{C}-\mathrm{Cl}\) stretching. These spectra

\section*{Fig. 3. FTIR spectra of extracted polymer from the frass in the PVC group (orange) compared to control PVC (black).}

\section*{Fig. 2. Consumption and depolymerization of PVC by Tenebrio molitor L. (a) The PVC consumed by Tenebrio molitor L. (1) and the mass reduction (2). (b) The THFextractable fraction in the frass (c) Alterations in Mn and Mw between the remaining polymers from the frass versus the control PVC.}

3.3. Species profiling of the intestinal metagenomes of yellow mealworms feeding on PVC

Metagenomic clustering and 16S rRNA results showed obvious differences between the gut microbiota in PVC and bran groups (Fig. 4a-b). PCoA analysis (Fig. 4c-d) indicated segregation of microbial communities of the PVC and bran groups along the primary coordinate axis.

The top 50 most abundant genera are shown as a heatmap (Fig. 5a). For the PVC larvae there was an increase in abundance relative to bran of Escherichia-Shigella, Sphingomonas, Pelomonas, Parasutterella, Alloprevotella, Acidovorax, Methylobacterium-Methylorubrum, Methylobacillus, Prevotellaceae_UCG-001 and Parabacteroides. The most significant increase was observed in the Pelomonas genus (from 0.06% to 3.47%). Other increases are noted Acidovorax, Escherichia-Shigella, Sphingomonas and Parasutterella. In contrast, the abundance of other genera decreased, e.g., Bacillus, from 24% (bran) to 0.072% (PVC), followed by Pseudomonas and Enterobacter.

LEfSe analysis was further conducted to explore microbial components associated with PVC. This analysis revealed eleven biomarker species. Among these, Gammaproteobacteria, Proteobacteria, Enterobacteriales and Aquabacterium were enriched in the PVC group, whereas Pantoea, Erwiniaaceae, Thermoclostridium, Bacillus, Bacillaceae, Bacillales, and Firmicutes were enriched in the bran group (Fig. 5b).

3.4. Metagenomic function recognition of the gut microbiome

LEfSe was used to examine whether changes in the community structure had functional implications. In the bran and PVC groups, we identified 43 and 111 key gene modules, respectively, that exhibited significant enrichment (Table S3). Modules enriched in the bran group were associated with pathways such as purine metabolism, pentose phosphate pathway, carbon fixation in photosynthetic organisms, amino sugar and nucleotide sugar metabolism, glycolysis/glucogenesis and cysteine and methionine metabolism. Modules enriched in the PVC group were associated with the citrate cycle (TCA cycle), oxidative phosphorylation, pentose and glucuronate interconversions, valine,


\section*{Discussion}

With the growth of the plastics industry, the accumulation of waste petroleum-based plastics has led to environmental pollution. Conventional methods for treating plastic waste, involving physical and chemical processes, tend to be expensive and generate numerous byproducts that result in secondary pollution. A more promising avenue is biological degradation, which involves the use of microbes that breakdown complex plastic waste into simpler less toxic monomers (Sridharan et al., 2021). Insects are the largest group within the animal kingdom arthropod phylum, and are highly abundant, diverse and


![Figure 6](image6.png)
Fig. 6. LDA comparing key modules between bran and PVC groups. LDA scores ($\log_{10} \geq 2$) to identify key gene modules displaying significant differential abundances in bran and PVC groups. The significance of these differences between the two groups was evaluated through one-way ANOVA. **p < 0.05; ***p < 0.001.

The microbial communities residing in insect guts form intricate microecosystems comprising viruses, archaea, bacteria, fungi and protozoa. This composition is affected by diet and the external environment.

Some invertebrate species can feed on wood and other polymeric substances, and can even degrade plastic. These properties are attributed to the symbiotic microbes in their intestines (Engel and Moran, 2013; Yang et al., 2014).

The present study has revealed distinctive characteristics in the gut microbiome of yellow mealworms following PVC consumption. Through metagenomic analysis, we examined the impact of transitioning from a bran-based diet to PVC, identifying potential microorganisms capable of degrading PVC. These include Proteobacteria, Enterobacteriales, Aquabacterium, and Gammaproteobacteria. Proteobacteria can cause foodborne illnesses in humans and can degrade LDPE, linear alkylbenzene sulfonate, oil and other xenobiotic pollutants and natural polymers (Summera and Ramesh, 2016) (Oliveira et al., 2010); (Gao et al., 2019). Enterobacteriales are involved in pesticide degradation, lignocellulose breakdown and the metabolism of aromatic compounds and heavy metals (Parakhia et al., 2019); (Jiménez et al., 2015); (Devpura et al., 2017). The genus Aquabacterium degrades liquid and solid alkanes, as well as quinoline and indole, and it can dechlorinate trichloroethylene under anaerobic conditions (Masuda, 2009); (Shi et al., 2020; Liu, 2011). Gammaproteobacteria can degrade lignocellulose and petroleum hydrocarbons (Ferguson et al., 2017; Yu et al., 2018; Li et al., 2016).

The microorganisms engaged in PVC biodegradation in yellow mealworms are not exclusive to this insect species but are likely widespread in nature and may have evolved from microorganisms that naturally breakdown natural polymers like lignin.

In the PVC group, our metagenomic analysis unveiled a notable enrichment of oxidative phosphorylation-related gene modules. "Oxidative phosphorylation" is recognized for its capacity to regulate microbial acid production and coordinate the expression of "proton-pumping" genes as part of the dehydrogenation pathway (Krulwich et al., 2011). Both the Cytochrome bc1 complex (M00152) and the Cytochrome bc1 complex respiratory unit (M00151), constituents of the "oxidative phosphorylation" pathway, exhibited significant enrichment (Fig. 5). This suggests that the gut microbes in mealworms generate more energy to cope with carbon deficiency following PVC exposure. Fatty acid and lipopolysaccharide biosynthesis gene modules, closely related to energy metabolism, also showed significant enrichment. Intriguingly, an analysis of differentially expressed genes in the gut microflora of mice exposed to polystyrene microplastics (MPs) showed that most upregulated genes were linked to key metabolic pathways, especially fat and lipid metabolism after MPs exposure (Huang et al., 2023). This suggests that plastics have a common impact on the expression of crucial genes involved in fat and lipid metabolism, enhancing the ability to absorb nutrients by the gut in response to nutrient-deficient food.


5. Conclusion

In conclusion, yellow mealworms can sustain some growth through PVC consumption. PVC degradation was evident from the alterations in its chemical structure and in the reduced Mn and Mw, upon exit from the larvae intestinal tract. The PVC diet led to changes in the expression of intestinal flora and their functional genes. Thus the present study offers insights into how insects digest PVC plastics and introduces a novel perspective on environmentally friendly plastic disposal.

Credit author statement

This work was supported by Science and Technology Project Fund of Jiangxi Provincial Department of Education (grant no.: GJJ215003). Jianquan Xu designed the project and performed most of the experiments. Yongquan Dong provided the place for breeding larva and provided technical guidance.

Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Data availability

Data will be made available on request.

Appendix A. Supporting information

Supplementary data associated with this article can be found in the online version at doi:10.1016/j.ecoenv.2024.116046.

References

Przemieniecki, S.W., Kosewska, A., Ciesielski, S., Kosewska, O., 2020. Changes in the gut microbiome and enzymatic profile of Tenebrio molitor larvae biodegrading cellulose, polyethylene and polystyrene waste. Environ. Pollut. 256, 113265.

Restrepo-Flórez, J.-M., Bassi, A., Thompson, M.R., 2014. Microbial degradation and deterioration of polystyrene – a review. Int. Biodeterior. Biodegrad.

Robinson, W.H., 2005. Urban Insects and Arachnids: Plecoptera, Pscoptera.

Ru, J., Huo, Y., Yang, Y., 2020. Microbial degradation and valorization of plastic wastes. Front Microbiol 11, 442.

Sen, S.K., Raut, S., 2015. Microbial degradation of low density polyethylene (LDPE): a review. J. Environ. Chem. Eng. 3, 462–473.

Shen, M., Song, B., Zeng, G., Zhang, Y., Huang, W., Wen, X., Tang, W., 2020. Are biodegradable plastics a promising solution to solve the global plastic pollution? Environ. Pollut. 263, 114469.

Shi, J., Zheng, M., Zhang, Z., Han, H., Xu, C., 2020. Enhanced biodegradation of quinoline and indole with a novel symbiotic system of Polyurethane-chlorella bacteria. J. Water Process Eng. 37, 101525.

Singh, B., Sharma, N., 2008. Mechanistic implications of plastic degradation. Polym. Degrad. Stab. 93, 561–584.

Song, Y., Qiu, R., Hu, J., Li, X., He, D., 2020. Biodegradation and disintegration of expanded polystyrene by land snails Achatina fulica. Sci. Total Environ. 746, 141289.

Sridharan, R., Krishnaswamy, V.G., Kumar, P.S., 2021. Analysis and microbial degradation of low-density polyethylene (LDPE) in Winogradsky column. Environ. Res 201, 111646.

Summera, R. Ramesh, V. 2016. A discussion on low density polyethylene (LDPE) degradation by an alpha- proteobacteria-Nesiobacter exalbescence from saltpans of Chennai, Tamil Nadu using a detailed analysis of FTIR spectra. iMedPub.

Tmi Group, T.M.I. 2022. Plastics-the Facts 2022. TPE magazine international: thermoplastic elastomers.

Tournier, V., Topham, C.M., Gilles, A., David, B., Marty, A., 2020. An engineered PET depolymerase to break down and recycle plastic bottles. Nature 580, 216–219.

Wu, Q., Tao, H., Wong, M.H., 2019. Feeding and metabolism effects of three common microplastics on Tenebrio molitor L. Environ. Geochem. Health 41, 17–26.

Wu, W.M., Yang, J., Criddle, C.S., 2017. Microplastics pollution and reduction strategies. Front. Environ. Sci. Eng. 11, 6.

YANG, J., YANG, Y., WU, W.M., ZHAO, J., JIANG, L., 2014. Evidence of polystyrene biodegradation by bacterial strains from the guts of plastic-eating waxworms. Environ. Sci. Technol. 48, 13776–13784.

Yang, L., Gao, J., Liu, Y., Zhuang, G., Peng, X., Wu, W.M., Zhuang, X., 2021a. Biodegradation of expanded polystyrene and low-density polyethylene foams in larvae of Tenebrio molitor Linnaeus (Coleoptera: Tenebrionidae): Broad versus limited extent depolymerization and microbe-dependence versus independence. Chemosphere 262, 127818.

Yang, S.S., Ding, M.Q., He, L., Zhang, C.H., Li, Q.X., Xing, D.F., Cao, G.L., Zhao, L., Ding, J., Ren, N.Q., Wu, W.M., 2021b. Biodegradation of polypropylene by yellow mealworms (Tenebrio molitor) and superworms (Zophobas atratus) via gut-microbe-dependent depolymerization. Sci. Total Environ. 756, 144087.

Yang, S.S., Brandon, A.M., Flanagan, J.C.A., Yang, J., Ding, N., Cai, S.-Y., Fan, H.-Q., Wang, Z.-Y., Ren, J., Benbow, E., 2018a. Biodegradation of polystyrene wastes in yellow mealworms (larvae of Tenebrio molitor Linnaeus): Factors affecting biodegradation rates and the ability of polystyrene-fed larvae to complete their life cycle. Chemosphere 191, 979–989.

Yang, S.S., Wu, W.-M., Brandon, A.M., Fan, H.-Q., Receveur, J.P., Li, Y., Wang, Z.-Y., Fan, R., McClellan, R.L., Gao, S.-H., 2018b. Ubiquity of polystyrene digestion and biodegradation within yellow mealworms, larvae of Tenebrio molitor Linnaeus (Coleoptera: Tenebrionidae). Chemosphere 212, 262–271.

Yang, Y., Yang, J., Wu, W.M., Zhao, J., Song, Y., Gao, L., Yang, R., Jiang, L., 2015a. Biodegradation and mineralization of polystyrene by plastic-eating mealworms: part 1. chemical and physical characterization and isotopic tests. Environ. Sci. Technol. 49, 12080–12086.

Yang, Y., Yang, J., Wu, W.M., Zhao, J., Song, Y., Gao, L., Yang, R., Jiang, L., 2015b. Biodegradation and mineralization of polystyrene by plastic-eating mealworms: part 2. role of gut microorganisms. Environ. Sci. Technol. 49, 12087–12093.

Yang, Y., Wang, J., Xia, M., 2020a. Biodegradation and mineralization of polystyrene by plastic-eating superworms Zophobas atratus. Sci. Total Environ. 708, 135233.

Yang, Y., Wang, J., Xia, M., 2020b. Biodegradation and mineralization of polystyrene by plastic-eating superworms Zophobas atratus. Sci. Total Environ. 708, 135233.1–135233.7.

YOSHIDA, S., HIRAGA, K., TAKEHANA, T., TANIGUCHI, I., YAMAJI, H., MAEDA, Y., TOYOHARA, K., MIYAMOTO, K., KIMURA, Y., ODA, K., 2016. A bacterium that degrades and assimilates poly(ethylene terephthalate). Science 351, 1196–1199.

Yu, J., Chen, C., Liu, C., Yu, D., Chen, S., 2018. Insight into relationship between micro-consortia, nitrogen source and petroleum degradation at low temperature anaerobic condition. Cold Spring Harb. Lab.

Yu, L.A., Yla, B., Bl, A., Qiang, L.A., Ssy, A., Bl, A., NR, A., Ww, B., Dz, A., 2021. Response of the Yellow Mealworm (Tenebrio molitor) gut microbiome to diet shifts during polystyrene and polyethylene biodegradation. J. Hazard. Mater.

YUAN,
from __future__ import annotations
from typing import Any

GRAPH_FIELD_SEP = "<SEP>"

PROMPTS: dict[str, Any] = {}

PROMPTS["DEFAULT_LANGUAGE"] = "English"
PROMPTS["DEFAULT_TUPLE_DELIMITER"] = "<|>"
PROMPTS["DEFAULT_RECORD_DELIMITER"] = "##"
PROMPTS["DEFAULT_COMPLETION_DELIMITER"] = "<|COMPLETE|>"
PROMPTS["process_tickers"] = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
PROMPTS["DEFAULT_ENTITY_TYPES"] = [
  "enzyme",
  "organism",
  "fungus",
  "bacteria",
  "pathways",
  "metabolites",
  "experiment design",
  "nutrient",
  "pollutant",
  "research method",
  "diet",
  "environmental impact",
  "biodegradation process",
  "research institution",
  "publication",
  "analytical tools",
  "microbial genus",
  "experiment condition",
  "plastic type"
]


PROMPTS["entity_extraction"] = """-Goal-
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.
Use {language} as output language.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, use same language as input text. If English, capitalized the name.
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity as ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>)

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
- relationship_keywords: one or more high-level key words that summarize the overarching nature of the relationship, focusing on concepts or themes rather than specific details
Format each relationship as ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_keywords>{tuple_delimiter}<relationship_strength>)

3. Identify high-level key words that summarize the main concepts, themes, or topics of the entire text. These should capture the overarching ideas present in the document.
Format the content-level key words as ("content_keywords"{tuple_delimiter}<high_level_keywords>)

4. Return output in {language} as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

5. When finished, output {completion_delimiter}

######################
-Examples-
######################
{examples}

#############################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Output:
"""

PROMPTS["entity_extraction_examples"] = [
    """Example 1:
entity_types: ["enzyme","organism","fungus","bacteria","pathways","metabolites","experiment design","nutrient","pollutant","research method","diet","environmental impact","biodegradation process","research institution","publication","analytical tools","microbial genus","experiment condition","plastic type"]
text:
 Achroia grisella (Kundungal et al., 2019) and Spodoptera frugiperda (Zhang et al., 2022b).

Both T. molitor and T. obscurus larvae are not only two widely investigated plastic-degrading insect larvae (Wu and Cridde, 2021; Yang et al., 2023b), but also are commercially reared for animal feed and insect protein, typically being fed with wheat bran (WB) (Ding et al., 2023; Peng et al., 2019; Yang et al., 2021c). Our previous work has shown that both species can rapidly biodegrade LDPE, LLDPE and HDPE (Yang et al., 2021c, 2022). Studies of LDPE biodegradation by these two species have demonstrated that under nutrient-poor conditions, coordination of gut microbiome carbon and nitrogen metabolism is necessary for energy and nutrition acquisition during plastic degradation (Ding et al., 2023; Yang et al., 2023a). Although T. molitor and T. obscurus have distinct behaviours (Peng et al., 2019; Robinson, 2005), both species can adapt to LDPE diets by altering their gut microbiota or microbiome structure (Dai et al., 2022; Welti et al., 2020) to ensure their capacity to survive using PE as their sole source of both energy and carbon within a 3–5 week period (Lou et al., 2020, 2021; Przemieniecki et al., 2020; Woo et al., 2020; Yang et al., 2021a, 2021b, 2021c, 2022). Previous research on reported that a decrease in gut microbial community similarity occurs after larvae switch to a plastic-based diet, such as LDPE, PS, and etc. (Brandon et al., 2018; Peng et al., 2019, 2021; Przemieniecki et al., 2020; Ruiz Barrionuevo et al., 2022a, 2022b; Yang et al., 2022, Yang et al., 2023a). However, the majority of reports on microbiomes associated with PE degradation by insect larvae have focused on LDPE (Brandon et al., 2018; Peng et al., 2019; Yang et al., 2021c).

During plastics biodegradation, Tenebrio larvae are directly exposed to PE microplastics (MPs), through biofragmentation of ingested plastic foams or particles into fragments by chewing, grinding, and digestion in the gut. Studies on other macroinvertebrates have shown that long-term exposure to MPs can cause biological toxicity, causing mechanical damage and the onset of inflammatory responses in Corbicula fluminea, mice and zebrafish (Li et al., 2021).The gut is a vital line of defence against exogenous substances, as well as being an essential organ for immunity, digestion and absorption in insects. When the gut microbiota becomes imbalanced or are mechanically stimulated, various inflammatory and immune cells are activated, leading to intestinal inflammation (Baeckhed et al., 2005; Li et al., 2021; Suzuki et al., 2004). However, the extent to which gut health reflects the effects of PE-MPs with different PCPs on Tenebrio larvae during plastic degradation, has not been clearly elucidated. Our previous studies found that different metabolic intermediates were generated when T. molitor and T. obscurus larvae ingested and digested HDPE, LLDPE and LDPE. The degradation intermediates formed may also affect on T. obscurus and T. molitor larvae.

For more than a decade, PE has been the top plastic in the world, and it is a promising sustainable technology and green strategy to utilize the mealworms, which are macroinvertebrates with the ability to degrade plastics, in the biodegradation of PE. To the best of our knowledge, no studies have comprehensively addressed the comparison of the impacts of PE type (LDPE, LLDPE and HDPE) on larval physiology, gut microbiome and oxidative stress (at a physiological or biochemical level). In addition, in the long run, the larvae degrade microplastics and then excrete plastic into the ecosystem, and it is important to investigate whether their frass contain toxic substances that are harmful to aquatic and terrestrial organisms in

2. Materials and methods

2.1. Sources of Tenebrio larvae

T. molitor larvae were procured from the Dafa Birds and Flower Market in Harbin, China while T. obscurus larvae were procured from a Breeding Farm in Zaozhuang, Shandong, China. The dealers claimed that the larvae were fed a diet without antibiotics.

2.2. PE materials

The high-purity PE powders (size: <300 μm) of LDPE, HDPE, and LLDPE were purchased from Shanghai Plastics Trading Co., Ltd., Shanghai, China. The molecular weights are Mn 42.2, 93.2, and 59.5 kDa; Mw 110.5, 222.5, and 182 kDa; and size averaged molecular weight (Mz) 216.1, 456.5, and 408.8 kDa for LDPE, LLDPE, and HDPE, respectively (Table S1). No catalysts or additives were present according to manufacture (Table S2). Wheat bran (WB) was purchase from an agricultural market in Harbin, China. All analytical grade chemicals used for analyses were analytical degrade from Sin
------------------------
output:
("entity"{tuple_delimiter}ACHROIA GRISELLA{tuple_delimiter}SPECIES{tuple_delimiter}Achroia grisella is a species of moth investigated for its role in biodegradation of plastics)
{record_delimiter}
("entity"{tuple_delimiter}SPODOPTERA FRUGIPERDA{tuple_delimiter}SPECIES{tuple_delimiter}Spodoptera frugiperda is a species of moth studied for its ecological impact and potential in biodegradation)
{record_delimiter}
("entity"{tuple_delimiter}TENEBRIO MOLITOR{tuple_delimiter}SPECIES{tuple_delimiter}Tenebrio molitor is a plastic-degrading insect larva commonly known as the mealworm, reared for animal feed and capable of degrading various plastics)
{record_delimiter}
("entity"{tuple_delimiter}TENEBRIO OBSCURUS{tuple_delimiter}SPECIES{tuple_delimiter}Tenebrio obscurus is another species of plastic-degrading insect larva, similar to T. molitor in its capabilities and uses)
{record_delimiter}
("entity"{tuple_delimiter}PLASTIC DEGRADATION{tuple_delimiter}PROCESS{tuple_delimiter}Plastic degradation refers to the process through which organisms break down plastics, often involving the gut microbiome for energy and nutrition)
{record_delimiter}
("entity"{tuple_delimiter}LDPE{tuple_delimiter}MATERIAL{tuple_delimiter}Low-Density Polyethylene (LDPE) is a type of plastic that can be degraded by certain insect larvae)
{record_delimiter}
("entity"{tuple_delimiter}LLDPE{tuple_delimiter}MATERIAL{tuple_delimiter}Linear Low-Density Polyethylene (LLDPE) is a plastic type that is also subject to degradation by insect larvae)
{record_delimiter}
("entity"{tuple_delimiter}HDPE{tuple_delimiter}MATERIAL{tuple_delimiter}High-Density Polyethylene (HDPE) is another plastic that is degradable by certain insect larvae)
{record_delimiter}
("entity"{tuple_delimiter}GUT MICROBIOME{tuple_delimiter}BIOLOGICAL SYSTEM{tuple_delimiter}The gut microbiome is a community of microorganisms in the digestive system of insects that plays a critical role in digestion and degradation processes)
{record_delimiter}
("entity"{tuple_delimiter}MICROPLASTICS{tuple_delimiter}MATERIAL{tuple_delimiter}Microplastics are small plastic particles that can impact the health of organisms when ingested)
{record_delimiter}
("entity"{tuple_delimiter}FRASS{tuple_delimiter}MATERIAL{tuple_delimiter}Frass is the excrement of insects, which may contain remnants of degraded plastics and could impact the ecosystem)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO MOLITOR{tuple_delimiter}PLASTIC DEGRADATION{tuple_delimiter}Tenebrio molitor is involved in the plastic degradation process, utilizing its gut microbiome to break down plastics like LDPE, LLDPE, and HDPE{tuple_delimiter}8)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO OBSCURUS{tuple_delimiter}PLASTIC DEGRADATION{tuple_delimiter}Tenebrio obscurus participates in the plastic degradation process similar to T. molitor, aiding in breaking down various plastics{tuple_delimiter}8)
{record_delimiter}
("relationship"{tuple_delimiter}LDPE{tuple_delimiter}PLASTIC DEGRADATION{tuple_delimiter}LDPE is a type of plastic that can be degraded by insect larvae, contributing to the overall plastic degradation process{tuple_delimiter}6)
{record_delimiter}
("relationship"{tuple_delimiter}LLDPE{tuple_delimiter}PLASTIC DEGRADATION{tuple_delimiter}LLDPE is also a plastic type involved in the degradation process facilitated by insect larvae{tuple_delimiter}6)
{record_delimiter}
("relationship"{tuple_delimiter}HDPE{tuple_delimiter}PLASTIC DEGRADATION{tuple_delimiter}HDPE is another plastic that can be broken down by certain insect larvae during the degradation process{tuple_delimiter}6)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO MOLITOR{tuple_delimiter}GUT MICROBIOME{tuple_delimiter}The gut microbiome of Tenebrio molitor plays a crucial role in energy and nutrition acquisition during the degradation of plastics{tuple_delimiter}7)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO OBSCURUS{tuple_delimiter}GUT MICROBIOME{tuple_delimiter}The gut microbiome of Tenebrio obscurus is essential for its adaptation to plastic diets and degradation processes{tuple_delimiter}7)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO MOLITOR{tuple_delimiter}MICROPLASTICS{tuple_delimiter}Tenebrio molitor larvae are exposed to microplastics during the plastic degradation process, which may affect their health{tuple_delimiter}5)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO OBSCURUS{tuple_delimiter}MICROPLASTICS{tuple_delimiter}Tenebrio obscurus larvae are also exposed to microplastics, which can lead to potential health issues{tuple_delimiter}5)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO MOLITOR{tuple_delimiter}FRASS{tuple_delimiter}The frass produced by Tenebrio molitor may contain remnants of plastics and potentially harmful substances affecting the ecosystem{tuple_delimiter}4)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO OBSCURUS{tuple_delimiter}FRASS{tuple_delimiter}The frass of Tenebrio obscurus may also have similar ecological implications as that of T. molitor's frass{tuple_delimiter}4)
{completion_delimiter}
#############################""",
    """Example 2:
entity_types: ["enzyme","organism","fungus","bacteria","pathways","metabolites","experiment design","nutrient","pollutant","research method","diet","environmental impact","biodegradation process","research institution","publication","analytical tools","microbial genus","experiment condition","plastic type"]
text:
 \({ }^{\circledR}\) solution at pH 3.5 in a magnetic stirrer for 10-15 min. The polystyrene was then dried in absorbent paper and incubated overnight at \(59{ }^{\circ} \mathrm{C}\) to remove all remaining humidity and carefully observed under a stereomicroscope to confirm the absence of organic materials (e.g. exuviae). Undegraded substrate, ideally composed of not eaten PS debris and fecal pellets, was sieved to separate the two components. The resulting PS fraction was weighted and added to the above figure.

\subsection*{2.3. DNA extraction of gut microorganisms, markers amplification and sequencing}

At the end of the experiment, total DNA was extracted from A. diaperinus guts to characterize its microbial communities. Lesser mealworm larvae were collected and the whole intestines dissected under a Leica Wild M3C stereomicroscope using Petri dishes filled with sterilized paraffin as support. Total DNA was extracted using the QIAamp PowerFecal \({ }^{\circledR}\) DNA Kit according to the manufacturer's protocol. Extractions were made in triplicates from each group, i.e. three individual larvae were used to have triplicate observations from the PS group and three from the control group. DNA extractions were used for a metabarcoding analysis of the fungal and bacterial communities using the ITS1 and the 16S v3-v4 region as molecular marker, respectively (details in Protocol S1; Supplementary material).

\subsection*{2.4. Data analysis}

Raw sequences were demultiplexed based on their indices and primer sequences were removed. Quality trimming/filtering was performed in trimmomatic v.0.39 (Bolger et al., 2014) and then processed using the Quantitative Insights Into Microbial Ecology v.2 software (QIIME2 - v.2019.7) (Bolyen et al., 2019) as described in Protocol S2 (Supplementary material).

Diversity analyses were performed in QIIME2 and data for both markers were rarefied at the minimum sampling depth observed among samples prior to analyses. Good's coverage, Simpson and Shannon diversity indices ( \(\alpha\) diversity), were calculated for both markers, using the Kruskal-Wallis test to compare values across groups. Bray-Curtis Principal Coordinates Analysis (PCoA) was performed on both datasets. The phylogeny-based Unifrac distances (weighted and unweighted) PCoA were applied to the bacteria dataset only ( \(\beta\) diversity). QIME2 workflows are provided as Protocol S3 (bacteria) and Protocol S4 (fungi) (Supplementary material).

Differential abundance of OTUs was evaluated for both datasets (on the original non rarefied datasets) using the Phyloseq and DESeq2 packages in R v.3.6.1 (R Core Team 2018, http://www.R-project.org/) (Love et al., 2014; McMurdie and Holmes, 2013), and OTUs with an associated adjusted \(p\)-value (padj) \(<0.05\) were retained. The custom R script for this procedure is supplied as Protocol S5 of Supplementary material.

\section*{3. Results}

\subsection*{3.1. A. diaperinus survival rate and polystyrene weight loss}

Alphitobius diaperinus underwent a reduction of 77\% and 89\% of total weight in the CT and PS group, respectively. Reduction was more severe in the PS compared to the CT group (1.2×).

The weight of the polystyrene decreased during the experiment from 20 g (time zero) to 16 g (day 30) \((s=2.83)\). Henceforth, 4 g (20\%) of polystyrene was presumably degraded during 30 days of incubation.

\subsection*{3.2. Diversity of bacteria}



The taxa bar plot showed the presence of six predominant bacterial phyla, mostly with different relative frequencies: Proteobacteria (76% and 57% in PS and CT, respectively), Bacteroidetes (3% and 26%), Firmicutes (13% and 8%), Actinobacteria (4% and 8%), Fusobacteria (3% and \(<1 \%)\) and an unassigned phylum (<1% in both groups) (Fig. 1a).

Clustering at the level of classes identified eight predominant entities, often represented with different relative frequencies: Gammaproteobacteria (76% and 57%), Bacteroidia (3% and 25%), Bacilli (13% and 7%), Actinobacteria (4% and 8%), Fusobacteria (3% and 1%), Alphaproteobacteria (<1% and 1%), Erysipelotrichia (<1% both) and an unassigned class (<1% both) (Fig. 1b).

Shared OTUs count indicated that \(\sim 30 \%\) OTUs were shared among treatment and control groups, \(\sim 50 \%\) were observed in control only and \(\sim 20 \%\) in treatment only (Fig. 2).

The Good's coverage index, an estimate of the representativeness of the data, produced values higher than 0.99 for both PS and CT groups, thus indicating that the sequencing depth could be considered appropriate to provide an adequate estimation of the bacterial diversity in the samples. The Shannon and Simpson indices (Table 1) produced high values overall, with the only exception of one PS sample (library PS3). Based on the Simpson
------------------------
output:
("entity"{tuple_delimiter}ALPHITOBIUS DIAPERINUS{tuple_delimiter}ORGANISM{tuple_delimiter}Alphitobius diaperinus is a species of lesser mealworm whose gut microorganisms were studied for diversity and degradation of polystyrene)
{record_delimiter}
("entity"{tuple_delimiter}POLYSTYRENE{tuple_delimiter}COMPOUND{tuple_delimiter}Polystyrene is a plastic compound used in the experiment, which was degraded by Alphitobius diaperinus)
{record_delimiter}
("entity"{tuple_delimiter}DNA EXTRACTION{tuple_delimiter}PROCEDURE{tuple_delimiter}DNA extraction involves obtaining DNA from the gut microorganisms of Alphitobius diaperinus for microbial community analysis)
{record_delimiter}
("entity"{tuple_delimiter}METABARCODING ANALYSIS{tuple_delimiter}PROCEDURE{tuple_delimiter}Metabarcoding analysis is a method used to characterize microbial communities through sequencing specific DNA regions)
{record_delimiter}
("entity"{tuple_delimiter}QIIME2{tuple_delimiter}SOFTWARE{tuple_delimiter}QIIME2 is software used for analyzing and processing microbial ecology data)
{record_delimiter}
("entity"{tuple_delimiter}BRAY-CURTIS PCoA{tuple_delimiter}METHOD{tuple_delimiter}Bray-Curtis Principal Coordinates Analysis is a method for assessing the similarity of microbial communities based on abundance data)
{record_delimiter}
("entity"{tuple_delimiter}OTUs{tuple_delimiter}BIOLOGICAL ENTITY{tuple_delimiter}Operational Taxonomic Units (OTUs) are used to categorize microbial species based on DNA sequences in diversity analyses)
{record_delimiter}
("entity"{tuple_delimiter}SIMILARITY ANALYSIS{tuple_delimiter}PROCEDURE{tuple_delimiter}Similarity analysis involves comparing the diversity of microbial communities across different treatment and control groups)
{record_delimiter}
("relationship"{tuple_delimiter}ALPHITOBIUS DIAPERINUS{tuple_delimiter}POLYSTYRENE{tuple_delimiter}Alphitobius diaperinus is capable of degrading polystyrene during the experiment{tuple_delimiter}8)
{record_delimiter}
("relationship"{tuple_delimiter}ALPHITOBIUS DIAPERINUS{tuple_delimiter}DNA EXTRACTION{tuple_delimiter}DNA extraction was performed from the guts of Alphitobius diaperinus to study its microbial community{tuple_delimiter}9)
{record_delimiter}
("relationship"{tuple_delimiter}DNA EXTRACTION{tuple_delimiter}METABARCODING ANALYSIS{tuple_delimiter}DNA extraction is a precursor step to conducting metabarcoding analysis for microbial characterization{tuple_delimiter}8)
{record_delimiter}
("relationship"{tuple_delimiter}METABARCODING ANALYSIS{tuple_delimiter}QIIME2{tuple_delimiter}Metabarcoding analysis data was processed using QIIME2 software{tuple_delimiter}7)
{record_delimiter}
("relationship"{tuple_delimiter}QIIME2{tuple_delimiter}BRAY-CURTIS PCoA{tuple_delimiter}QIIME2 was used to perform Bray-Curtis Principal Coordinates Analysis on microbial community data{tuple_delimiter}7)
{record_delimiter}
("relationship"{tuple_delimiter}OTUs{tuple_delimiter}SIMILARITY ANALYSIS{tuple_delimiter}Similarity analysis evaluated the abundance and diversity of OTUs between treatment and control groups{tuple_delimiter}6)
{completion_delimiter}
#############################""",
    """Example 4:

entity_types: ["enzyme","organism","fungus","bacteria","pathways","metabolites","experiment design","nutrient","pollutant","research method","diet","environmental impact","biodegradation process","research institution","publication","analytical tools","microbial genus","experiment condition","plastic type"]
text:
# Biodegradation and Mineralization of Polystyrene by Plastic-Eating Mealworms: Part 2. Role of Gut Microorganisms

## Yu Yang,† Jun Yang,*,† Wei-Min Wu,‡ Jiao Zhao,§ Yiling Song,|| Longcheng Gao,† Ruifu Yang,§ and Lei Jiang*†

*Key Laboratory of Bio-Inspired Smart Interfacial Science and Technology of Ministry of Education, School of Chemistry and Environment, and ||School of Biological Science and Medical Engineering, Beihang University, Beijing 100191, People’s Republic of China

†Department of Civil and Environmental Engineering, William & Cloy Codiga Resource Recovery Research Center, Center for Sustainable Development & Global Competitiveness, Stanford University, Stanford, California 94305-4020, United States

§Shenzhen Key Laboratory of Bioenergy, BGI-Shenzhen, Shenzhen, Guangdong 518083, People’s Republic of China

## Supporting Information

### ABSTRACT:
The role of gut bacteria of mealworms (the larvae of Tenebrio molitor Linnaeus) in polystyrene (PS) degradation was investigated. Gentamicin was the most effective inhibitor of gut bacteria among six antibiotics tested. Gut bacterial activities were essentially suppressed by feeding gentamicin food (30 mg/g) for 10 days. Gentamicin-feeding mealworms lost the ability to depolymerize PS and mineralize PS into CO2, as determined by characterizing worm fecula and feeding with 13C-labeled PS. A PS-degrading bacterial strain was isolated from the guts of the mealworms, Exiguobacterium sp. strain YT2, which could form biofilm on PS film over a 28 day incubation period and made obvious pits and cavities (0.2-0.3 mm in width) on PS film surfaces associated with decreases in hydrophobicity and the formation of C-O polar groups. A suspension culture of strain YT2 (106 cells/mL) was able to degrade 7.4 ± 0.4% of the PS pieces (2500 mg/L) over a 60 day incubation period. The molecular weight of the residual PS pieces was lower, and the release of water-soluble daughter products was detected. The results indicated the essential role of gut bacteria in PS biodegradation and mineralization, confirmed the presence of PS-degrading gut bacteria, and demonstrated the biodegradation of PS by mealworms.

### INTRODUCTION
Global production of petroleum-based plastic has grown 200-fold from 1.5 million tons in 1950 to 299 million tons in 2013.1,2 Tremendous consumption of plastic has produced large amounts of plastic waste, which has aroused global environmental concern.3-7 Polystyrene (PS), which is a common petroleum-based plastic with Styrofoam (expanded PS foam) as a major product, showed an annual global production of approximately 21 million tons in 2013.1 Although styrene monomers8,9 and oligomers10 are susceptible to biodegradation, PS is generally considered non-biodegradable as a result of its high molecular weight and highly stable structure.11 Using a 14C-labeled PS tracer, previous investigations have shown that the rate of PS biodegradation in different microbial consortia, such as soil, sewage sludge, decaying garbage, or manure, ranged from 0.01 to less than 3% within 4 months.12-14 A few bacteria isolated from soil were found to be capable of colonizing PS film surfaces,15,16 and researchers have claimed success in the isolation of PS-degrading microorganisms, such as Rhodococcus ruber.15 However, no convincing evidence has been provided that these isolates were deposited in any culture collection center or changed the physical and chemical properties of PS.

Some mandibulate insects and stored-product insect pests are able to chew and eat plastic packages of grain.17-21 In our companion paper (10.1021/acs.est.5b02661), we reported that the larvae of Tenebrio molitor Linnaeus (Coleoptera: Tenebrionidae), which are commonly known as mealworms, are able to chew and eat Styrofoam. Analyses of fecula egested showed that the cleavage of long-chain PS molecules and the formation of low-molecular-weight metabolites occurred in the gut. On the basis of the carbon balance of the ingested Styrofoam and 13C-tracer tests, the ingested PS was mainly mineralized to CO2

(47.7%), with a small fraction incorporated into lipid biomass (10.1021/acs.est.5b02661).

The midgut lumen of the mealworm harbors a variety of microorganisms that play an important role in the digestion of refractory food.22. The number of cultivable microorganisms in the gut of each mealworm is approximately 5-6 × 10^5 colony-forming units (CFU). Gut microbial populations are influenced by food. Antibiotics, such as nystatin and ampicillin, can suppress gut microbiota.22. Thus, if gut microbiota are essential for PS biodegradation, the suppression of gut microbiota by antibiotics will negatively impact PS degradation. The isolation of PS-degrading bacteria from the gut of the mealworm is another approach to establish the essential role of microbiota in PS degradation. As described elsewhere, we recently isolated two polyethylene (PE)-degrading bacterial strains, Bacillus sp. YP1 and Enterobacter asburiae VT1, from the PE plastic-eating waxworm gut and identified the presence of PE-degrading microorganisms in this environment.
------------------------
output:
("entity"{tuple_delimiter}TENEBRIO MOLITOR{tuple_delimiter}ORGANISM{tuple_delimiter}Tenebrio molitor, commonly known as mealworms, are larvae that can chew and eat Styrofoam and play a role in polystyrene biodegradation)
{record_delimiter}
("entity"{tuple_delimiter}POLYSTYRENE{tuple_delimiter}CHEMICAL{tuple_delimiter}Polystyrene (PS) is a common petroleum-based plastic that is generally considered non-biodegradable due to its high molecular weight and stable structure)
{record_delimiter}
("entity"{tuple_delimiter}GENTAMICIN{tuple_delimiter}CHEMICAL{tuple_delimiter}Gentamicin is an antibiotic that was found to be the most effective inhibitor of gut bacteria in mealworms, affecting their ability to degrade polystyrene)
{record_delimiter}
("entity"{tuple_delimiter}EXIGUOBACTERIUM SP. YT2{tuple_delimiter}ORGANISM{tuple_delimiter}Exiguobacterium sp. strain YT2 is a PS-degrading bacterial strain isolated from the guts of mealworms, capable of forming biofilm on PS film and degrading it)
{record_delimiter}
("entity"{tuple_delimiter}BIODEGRADATION{tuple_delimiter}BIODEGRADATION{tuple_delimiter}Biodegradation is the process by which organic substances are broken down by living organisms, in this case, the degradation of polystyrene by mealworms and their gut bacteria)
{record_delimiter}
("entity"{tuple_delimiter}MINERALIZATION{tuple_delimiter}BIODEGRADATION{tuple_delimiter}Mineralization refers to the process of converting organic substances into inorganic substances, such as CO2, during the degradation of polystyrene by mealworms)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO MOLITOR{tuple_delimiter}POLYSTYRENE{tuple_delimiter}Mealworms (Tenebrio molitor) are capable of chewing and degrading polystyrene, contributing to its biodegradation{tuple_delimiter}8)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO MOLITOR{tuple_delimiter}GENTAMICIN{tuple_delimiter}Gentamicin suppresses the gut bacteria of mealworms, negatively impacting their ability to degrade polystyrene{tuple_delimiter}7)
{record_delimiter}
("relationship"{tuple_delimiter}EXIGUOBACTERIUM SP. YT2{tuple_delimiter}POLYSTYRENE{tuple_delimiter}Exiguobacterium sp. strain YT2 is a bacterial strain that can degrade polystyrene, indicating its role in the biodegradation process{tuple_delimiter}8)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO MOLITOR{tuple_delimiter}BIODEGRADATION{tuple_delimiter}The gut bacteria of mealworms play an essential role in the biodegradation of polystyrene{tuple_delimiter}9)
{record_delimiter}
("relationship"{tuple_delimiter}TENEBRIO MOLITOR{tuple_delimiter}MINERALIZATION{tuple_delimiter}Mealworms contribute to the mineralization of polystyrene into CO2 during the degradation process{tuple_delimiter}8)
{record_delimiter}
("relationship"{tuple_delimiter}EXIGUOBACTERIUM SP. YT2{tuple_delimiter}BIODEGRADATION{tuple_delimiter}Exiguobacterium sp. strain YT2 is involved in the biodegradation of polystyrene, demonstrating the role of gut bacteria in this process{tuple_delimiter}8)
{completion_delimiter}
#############################""",
]

PROMPTS[
    "summarize_entity_descriptions"
] = """You are a helpful assistant responsible for generating a comprehensive summary of the data provided below.
Given one or two entities, and a list of descriptions, all related to the same entity or group of entities.
Please concatenate all of these into a single, comprehensive description. Make sure to include information collected from all the descriptions.
If the provided descriptions are contradictory, please resolve the contradictions and provide a single, coherent summary.
Make sure it is written in third person, and include the entity names so we the have full context.
Use {language} as output language.

#######
-Data-
Entities: {entity_name}
Description List: {description_list}
#######
Output:
"""

PROMPTS[
    "entiti_continue_extraction"
] = """MANY entities were missed in the last extraction.  Add them below using the same format:
"""

PROMPTS[
    "entiti_if_loop_extraction"
] = """It appears some entities may have still been missed.  Answer YES | NO if there are still entities that need to be added.
"""

PROMPTS["fail_response"] = (
    "Sorry, I'm not able to provide an answer to that question.[no-context]"
)

PROMPTS["rag_response"] = """---Role---

You are a helpful assistant responding to user query about Knowledge Base provided below.


---Goal---

Generate a concise response based on Knowledge Base and follow Response Rules, considering both the conversation history and the current query. Summarize all information in the provided Knowledge Base, and incorporating general knowledge relevant to the Knowledge Base. Do not include information not provided by Knowledge Base.

When handling relationships with timestamps:
1. Each relationship has a "created_at" timestamp indicating when we acquired this knowledge
2. When encountering conflicting relationships, consider both the semantic content and the timestamp
3. Don't automatically prefer the most recently created relationships - use judgment based on the context
4. For time-specific queries, prioritize temporal information in the content before considering creation timestamps

---Conversation History---
{history}

---Knowledge Base---
{context_data}

---Response Rules---

- Target format and length: {response_type}
- Use markdown formatting with appropriate section headings
- Please respond in the same language as the user's question.
- Ensure the response maintains continuity with the conversation history.
- If you don't know the answer, just say so.
- Do not make anything up. Do not include information not provided by the Knowledge Base."""

PROMPTS["keywords_extraction"] = """---Role---

You are a helpful assistant tasked with identifying both high-level and low-level keywords in the user's query and conversation history.

---Goal---

Given the query and conversation history, list both high-level and low-level keywords. High-level keywords focus on overarching concepts or themes, while low-level keywords focus on specific entities, details, or concrete terms.

---Instructions---

- Consider both the current query and relevant conversation history when extracting keywords
- Output the keywords in JSON format
- The JSON should have two keys:
  - "high_level_keywords" for overarching concepts or themes
  - "low_level_keywords" for specific entities or details

######################
-Examples-
######################
{examples}

#############################
-Real Data-
######################
Conversation History:
{history}

Current Query: {query}
######################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["keywords_extraction_examples"] = [
    """Example 1:

Query: "How does international trade influence global economic stability?"
################
Output:
{
  "high_level_keywords": ["International trade", "Global economic stability", "Economic impact"],
  "low_level_keywords": ["Trade agreements", "Tariffs", "Currency exchange", "Imports", "Exports"]
}
#############################""",
    """Example 2:

Query: "What are the environmental consequences of deforestation on biodiversity?"
################
Output:
{
  "high_level_keywords": ["Environmental consequences", "Deforestation", "Biodiversity loss"],
  "low_level_keywords": ["Species extinction", "Habitat destruction", "Carbon emissions", "Rainforest", "Ecosystem"]
}
#############################""",
    """Example 3:

Query: "What is the role of education in reducing poverty?"
################
Output:
{
  "high_level_keywords": ["Education", "Poverty reduction", "Socioeconomic development"],
  "low_level_keywords": ["School access", "Literacy rates", "Job training", "Income inequality"]
}
#############################""",
]


PROMPTS["naive_rag_response"] = """---Role---

You are a helpful assistant responding to user query about Document Chunks provided below.

---Goal---

Generate a concise response based on Document Chunks and follow Response Rules, considering both the conversation history and the current query. Summarize all information in the provided Document Chunks, and incorporating general knowledge relevant to the Document Chunks. Do not include information not provided by Document Chunks.

When handling content with timestamps:
1. Each piece of content has a "created_at" timestamp indicating when we acquired this knowledge
2. When encountering conflicting information, consider both the content and the timestamp
3. Don't automatically prefer the most recent content - use judgment based on the context
4. For time-specific queries, prioritize temporal information in the content before considering creation timestamps

---Conversation History---
{history}

---Document Chunks---
{content_data}

---Response Rules---

- Target format and length: {response_type}
- Use markdown formatting with appropriate section headings
- Please respond in the same language as the user's question.
- Ensure the response maintains continuity with the conversation history.
- If you don't know the answer, just say so.
- Do not include information not provided by the Document Chunks."""


PROMPTS[
    "similarity_check"
] = """Please analyze the similarity between these two questions:

Question 1: {original_prompt}
Question 2: {cached_prompt}

Please evaluate whether these two questions are semantically similar, and whether the answer to Question 2 can be used to answer Question 1, provide a similarity score between 0 and 1 directly.

Similarity score criteria:
0: Completely unrelated or answer cannot be reused, including but not limited to:
   - The questions have different topics
   - The locations mentioned in the questions are different
   - The times mentioned in the questions are different
   - The specific individuals mentioned in the questions are different
   - The specific events mentioned in the questions are different
   - The background information in the questions is different
   - The key conditions in the questions are different
1: Identical and answer can be directly reused
0.5: Partially related and answer needs modification to be used
Return only a number between 0-1, without any additional content.
"""

PROMPTS["mix_rag_response"] = """---Role---

You are a helpful assistant responding to user query about Data Sources provided below.


---Goal---

Generate a concise response based on Data Sources and follow Response Rules, considering both the conversation history and the current query. Data sources contain two parts: Knowledge Graph(KG) and Document Chunks(DC). Summarize all information in the provided Data Sources, and incorporating general knowledge relevant to the Data Sources. Do not include information not provided by Data Sources.

When handling information with timestamps:
1. Each piece of information (both relationships and content) has a "created_at" timestamp indicating when we acquired this knowledge
2. When encountering conflicting information, consider both the content/relationship and the timestamp
3. Don't automatically prefer the most recent information - use judgment based on the context
4. For time-specific queries, prioritize temporal information in the content before considering creation timestamps

---Conversation History---
{history}

---Data Sources---

1. From Knowledge Graph(KG):
{kg_context}

2. From Document Chunks(DC):
{vector_context}

---Response Rules---

- Target format and length: {response_type}
- Use markdown formatting with appropriate section headings
- Please respond in the same language as the user's question.
- Ensure the response maintains continuity with the conversation history.
- Organize answer in sesctions focusing on one main point or aspect of the answer
- Use clear and descriptive section titles that reflect the content
- List up to 5 most important reference sources at the end under "References" sesction. Clearly indicating whether each source is from Knowledge Graph (KG) or Vector Data (DC), in the following format: [KG/DC] Source content
- If you don't know the answer, just say so. Do not make anything up.
- Do not include information not provided by the Data Sources."""

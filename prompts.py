LOCATED_IN = """
Given a text within triple backticks, your task is to identify the following semantic relations between specified biomedical entities:

- [bacteria|anatomical location] LOCATED IN [human|animal]: Represents knowledge about anatomical structures that are situated in or associated with a human or animal.
- [chemical|microbiome] LOCATED IN [human|animal|anatomical location]: Represents knowledge about the presence of chemicals, bacteria or microbiomes in a human, animal, or anatomical site.
- [bacteria] PART OF [microbiome]: Indicates that a bacterium is a component of a specified microbiome.

Extract specified relations if explicitly stated or strongly implied. Format the output using the following JSON structure:

{ "Relational triples":
    [
        "[subject] RELATION [object]",
        "[subject] RELATION [object]"
    ]
}

### Example:

Text:
```
Many tissue types, including <entity type=\"anatomical location\">brain</entity>, <entity type=\"anatomical location\">heart</entity>, <entity type=\"anatomical location\">arteries</entity>, <entity type=\"anatomical location\">ovaries</entity>, and others, contain <entity type=\"chemical\">melanin</entity>.
```
Output:
{ "Relational triples":
    [
        "[melanin] LOCATED IN [brain]",
        "[melanin] LOCATED IN [heart]",
        "[melanin] LOCATED IN [arteries]",
        "[melanin] LOCATED IN [ovaries]"
    ]
}

Text:
```
Additionally, studies using the postmortem brain samples have detected the widespread presence of <entity type=\"bacteria\">oral bacteria</entity> in the <entity type=\"anatomical location\">brains</entity> of <entity type=\"human\">patients</entity> with <entity type=\"disease or finding\">Alzheimer's disease</entity>.
```
Output:
{ "Relational triples":
    [
        "[oral bacteria] LOCATED IN [brains]",
        "[brains] LOCATED IN [patients]"
    ]
}

Text:
```
Both <entity type=\"bacteria\">live and inactivated L. plantarum CCFM8661</entity> raised the richness of <entity type=\"microbiome\">gut microbiota</entity>, reduced the ratio of Bacteroidetes to Firmicutes and decreased the relative abundance of <entity type=\"bacteria\">Staphylococcus</entity> in the feces of <entity type=\"animal\">acne mice</entity>.
```
Output:
{ "Relational triples":
    [
        "[live and inactivated L. plantarum CCFM8661] PART OF [gut microbiota]",
        "[live and inactivated L. plantarum CCFM8661] LOCATED IN [acne mice]"
    ]
} 
"""

INTERACT = """
Given a text within triple backticks, your task is to identify the following semantic relations between specified biomedical entities:

- [bacteria] INTERACT [bacteria|chemical|drug]: Captures interactions where bacteria engage with other bacteria, chemicals, or drugs.
- [chemical] INTERACT / PART OF [chemical]: Refers to chemical entities interacting with or being components of other chemicals.
- [drug] INTERACT [drug|chemical]: Describes interactions where drugs affect or are affected by other drugs or chemicals.
- [drug] CHANGE EFFECT [disease or finding]: Refers to a drug modifying the effect or outcome of a disease or clinical finding.
- [chemical|dietary supplement|drug|food|bacteria] INFLUENCE [disease or finding]: Denotes that a chemical, supplement, drug, food, or bacterium has an effect on the course, severity, or outcome of a disease or clinical finding.

Extract specified relations if explicitly stated or strongly implied. Format the output using the following JSON structure:

{ "Relational triples":
    [
        "[subject] RELATION [object]",
        "[subject] RELATION [object]"
    ]
}

### Example:

Text:
```
Results indicated that <entity type=\"bacteria\">live L. plantarum CCFM8661</entity> suppressed <entity type=\"disease or finding\">skin inflammation</entity> and <entity type=\"chemical\">serum hormone</entity> (<entity type=\"chemical\">insulin</entity> and <entity type=\"chemical\">testosterone</entity>) production in <entity type=\"animal\">acne mice</entity>.
```
Output:
{ "Relational triples":
    [
        "[live L. plantarum CCFM8661] INFLUENCE [skin inflammation]",
        "[live L. plantarum CCFM8661] INTERACT [serum hormone]",
        "[live L. plantarum CCFM8661] INTERACT [insulin]",
        "[live L. plantarum CCFM8661] INTERACT [testosterone]"
    ]
}

Text:
```
Both <entity type=\"bacteria\">live and inactivated L. plantarum CCFM8661</entity> raised the richness of <entity type=\"microbiome\">gut microbiota</entity>, reduced the ratio of Bacteroidetes to Firmicutes and decreased the relative abundance of <entity type=\"bacteria\">Staphylococcus</entity> in the feces of <entity type=\"animal\">acne mice</entity>.
```
Output:
{ "Relational triples":
    [
        "[live and inactivated L. plantarum CCFM8661] PART OF [gut microbiota]",
        "[live and inactivated L. plantarum CCFM8661] INTERACT [Staphylococcus]"
    ]
}

Text:
```
Additionally, multiple <entity type=\"disease or finding\">AI</entity>'s have increased levels of certain inflammatory markers such as <entity type=\"chemical\">TNF-a</entity>, <entity type=\"chemical\">IL-6</entity>, and <entity type=\"chemical\">IL-17</entity> that have been shown to contribute to <entity type=\"disease or finding\">arthropathy</entity> and are also linked to increased levels of <entity type=\"disease or finding\">gut dysbiosis</entity>.
```
Output:
{ "Relational triples":
    [
        "[TNF-a] INFLUENCE [arthropathy]",
        "[IL-6] INFLUENCE [arthropathy]",
        "[IL-17] INFLUENCE [arthropathy]",
        "[TNF-a] INFLUENCE [gut dysbiosis]",
        "[IL-6] INFLUENCE [gut dysbiosis]",
        "[IL-17] INFLUENCE [gut dysbiosis]"
    ]
} 
"""

IMPACT = """
Given a text within triple backticks, your task is to identify the following semantic relations between specified biomedical entities:

- [chemical|dietary supplement|food] IMPACT [bacteria|microbiome]: Describes how chemicals, supplements, or foods influence bacterial populations or microbiome composition.
- [chemical|drug] IMPACT / PRODUCED BY [microbiome]: Indicates that a chemical or drug affects a microbiome or is a product of microbial metabolic activity.
- [chemical|dietary supplement|drug|food] ADMINISTERED [human|animal]: Indicates that a substance (e.g., chemical, supplement, drug, or food) is given to or consumed by a human or animal subject as part of a treatment, intervention, or experimental design.

Extract specified relations if explicitly stated or strongly implied. Format the output using the following JSON structure:

{ "Relational triples":
    [
        "[subject] RELATION [object]",
        "[subject] RELATION [object]"
    ]
}

### Example:

Text:
```
Previous studies investigating the effects of <entity type=\"drug\">Antibiotic growth promotants</entity> (<entity type=\"drug\">AGPs</entity>) on the <entity type=\"microbiome\">poultry gut microbiome</entity> have largely focused on <entity type=\"biomedical technique\">16S rDNA surveys</entity> based on a single <entity type=\"anatomical location\">gastrointestinal (GI) site</entity>, diet, and/or timepoint, resulting in an inconsistent view of their impact on community composition.
```
Output:
{ "Relational triples":
    [
        "[Antibiotic growth promotants] IMPACT [poultry gut microbiome]",
        "[AGPs] IMPACT [poultry gut microbiome]"
    ]
}

Text:
```
<entity type=\"drug\">AGPs</entity> are thought to operate through modulating the <entity type=\"microbiome\">gut microbiome</entity> to limit opportunities for colonization by pathogens, increase nutrient utilization, and reduce <entity type=\"disease or finding\">inflammation</entity>.
```
Output:
{ "Relational triples":
    [
        "[AGPs] IMPACT [gut microbiome]"
    ]
}

Text:
```
There is limited evidence from clinical studies of the positive effects of <entity type=\"dietary supplement\">probiotics</entity> in <entity type=\"human\">patients</entity> with <entity type=\"disease or finding\">migraine headache</entity>.
```
Output:
{ "Relational triples":
    [
        "[probiotics] ADMINISTERED [patients]"
    ]
} 
"""

LINKED_TO = """
Given a text within triple backticks, your task is to identify the following semantic relations between specified biomedical entities:

- [microbiome|bacteria|chemical|dietary supplement|drug|food] CHANGE EXPRESSION [Gene]: Captures the effect of microbiome, bacteria, chemicals, dietary supplements, drugs or food on gene expression.
- [microbiome] IS LINKED TO [disease or finding]: Represents an expressed association between a specific microbiome and a disease or clinical condition.
- [microbiome] COMPARED TO [microbiome]: Indicates that two microbiomes are being contrasted or analyzed relative to one another.

Extract specified relations if explicitly stated or strongly implied. Format the output using the following JSON structure:

{ "Relational triples":
    [
        "[subject] RELATION [object]",
        "[subject] RELATION [object]"
    ]
}

### Example:

Text:
```
Modification of the <entity type=\"microbiome\">gut microbiota</entity> has been reported to reduce the incidence of <entity type=\"disease or finding\">type 1 diabetes mellitus</entity> (<entity type=\"disease or finding\">T1D</entity>).
```
Output:
{ "Relational triples":
    [
        "[gut microbiome] IS LINKED TO [type 1 diabetes mellitus]",
        "[gut microbiome] IS LINKED TO [T1D]"
    ]
}

Text:
```
While <entity type=\"disease or finding\">chronic inflammation</entity> has been shown to affect many physiologic systems, this review explores the connection between <entity type=\"microbiome\">gut microbiota</entity>, bone metabolism, and the skeletal and joint destruction associated with various <entity type=\"disease or finding\">AI</entity>, including <entity type=\"disease or finding\">psoriatic arthritis</entity>, <entity type=\"disease or finding\">systemic lupus erythematosus</entity>, <entity type=\"disease or finding\">irritable bowel disease</entity>, and <entity type=\"disease or finding\">rheumatoid arthritis</entity>.
```
Output:
{ "Relational triples":
    [
        "[gut microbiota] IS LINKED TO [AI]",
        "[gut microbiota] IS LINKED TO [psoriatic arthritis]",
        "[gut microbiota] IS LINKED TO [systemic lupus erythematosus]",
        "[gut microbiota] IS LINKED TO [irritable bowel disease]",
        "[gut microbiota] IS LINKED TO [rheumatoid arthritis]"
    ]
}

Text:
```
There are several <entity type=\"dietary supplement\">phytochemicals</entity> (e.g., <entity type=\"dietary supplement\">curcumin</entity>, and <entity type=\"dietary supplement\">betulinic acid</entity>) that modulate the dysfunction of one or several key genes (e.g., <entity type=\"gene\">TREM2</entity>, <entity type=\"gene\">C3aR1</entity>) affected in the <entity type=\"anatomical location\">aged brain</entity>.
```
Output:
{ "Relational triples":
    [
        "[phytochemicals] CHANGE EXPRESSION [TREM2]",
        "[phytochemicals] CHANGE EXPRESSION [C3aR1]",
        "[curcumin] CHANGE EXPRESSION [TREM2]",
        "[curcumin] CHANGE EXPRESSION [C3aR1]",
        "[betulinic acid] CHANGE EXPRESSION [TREM2]",
        "[betulinic acid] CHANGE EXPRESSION [C3aR1]"
    ]
} 
"""

AFFECT = """
Given a text within triple backticks, your task is to identify the following semantic relations between specified biomedical entities:

- [disease or finding] INTERACT [chemical]: Captures stated interactions between a disease or finding and a chemical entity.
- [disease or finding] ASSOCIATED WITH / IS A [disease or finding]: Expresses a causal, compositional, or hierarchical relationship between diseases or clinical findings—either as one affecting another or being a subtype.
- [disease or finding] TARGET [human|animal]: Denotes that a disease affects or manifests in a specific human or animal population, either implicitly or explicitly described as a host or patient.
- [disease or finding] STRIKE [anatomical location]: Indicates that a disease or pathological condition impacts or manifests in a specific anatomical region.
- [disease or finding] CHANGE ABUNDANCE [bacteria|microbiome]: Reflects that the presence, levels, or diversity of bacterial species or microbiomes are altered due to a disease or clinical condition.

Extract specified relations if explicitly stated or strongly implied. Format the output using the following JSON structure:

{ "Relational triples":
    [
        "[subject] RELATION [object]",
        "[subject] RELATION [object]"
    ]
}

### Example:

Text:
```
<entity type=\"disease or finding\">Helicobacter pylori infection</entity> consists a high global burden affecting more than 50% of the <entity type=\"human\">world's population</entity>. It is implicated, beyond <entity type=\"disease or finding\">substantiated local gastric pathologies</entity>, i.e., <entity type=\"disease or finding\">peptic ulcers</entity> and <entity type=\"disease or finding\">gastric cancer</entity>, in the pathophysiology of several <entity type=\"disease or finding\">neurodegenerative disorders</entity>, mainly by inducing <entity type=\"disease or finding\">hyperhomocysteinemia-related brain cortical thinning</entity> (<entity type=\"disease or finding\">BCT</entity>). 
```
Output:
{ "Relational triples":
    [
        "[Helicobacter pylori infection] TARGET [world's population]",
        "[Helicobacter pylori infection] ASSOCIATED WITH [local gastric pathologies]",
        "[Helicobacter pylori infection] ASSOCIATED WITH [peptic ulcers]",
        "[Helicobacter pylori infection] ASSOCIATED WITH [gastric cancer]",
        "[Helicobacter pylori infection] ASSOCIATED WITH [neurodegenerative disorders]",
        "[Helicobacter pylori infection] ASSOCIATED WITH [hyperhomocysteinemia-related brain cortical thinning]",
        "[Helicobacter pylori infection] ASSOCIATED WITH [BCT]"
    ]
}

Text:
```
Further to this, the observed downregulation of these <entity type=\"chemical\">NAPEs</entity> is in line with the results in plasma of a mouse model of <entity type=\"disease or finding\">Parkinson's</entity>.
```
Output:
{ "Relational triples":
    [
        "[Parkinson's] INTERACT [NAPEs]"
    ]
}

Text:
```
The <entity type=\"animal\">FD mice</entity> also exhibited <entity type=\"disease or finding\">gut microbiota dysbiosis</entity> (decreased <entity type=\"bacteria\">Bacteroidetes</entity> and increased <entity type=\"bacteria\">Proteobacteria</entity>), which was significantly associated with the <entity type=\"disease or finding\">cognitive deficits</entity>.
```
Output:
{ "Relational triples":
    [
        "[gut microbiota dysbiosis] CHANGE ABUNDANCE [Bacteroidetes]",
        "[gut microbiota dysbiosis] CHANGE ABUNDANCE [Proteobacteria]";
        "[gut microbiota dysbiosis] TARGET [FD mice]",
        "[gut microbiota dysbiosis] ASSOCIATED WITH [cognitive deficits]"
    ]
} 
"""

USED_BY = """
Given a text within triple backticks, your task is to identify the following semantic relations between specified biomedical entities:

- [human|animal|microbiome] USED BY [biomedical technique]: Represents cases where a human, animal, or microbiome is analyzed, measured, or sampled through a biomedical method or technological assay.

Extract specified relations if explicitly stated or strongly implied. Format the output using the following JSON structure:

{ "Relational triples":
    [
        "[subject] RELATION [object]",
        "[subject] RELATION [object]"
    ]
}

### Example:

Text:
```
Here we describe a protocol to characterize the structural and functional phenotype of the <entity type=\"anatomical location\">rodent gut</entity> and to examine the <entity type=\"microbiome\">gut microbiota</entity> composition through <entity type=\"biomedical technique\">V4 16S rRNA gene sequencing</entity> and <entity type=\"biomedical technique\">microbiome profiling</entity>.
```
Output:
{ "Relational triples":
    [
        "[gut microbiota] USED BY [V4 16S rRNA gene sequencing]",
        "[gut microbiota] USED BY [microbiome profiling]"
    ]
} 
"""
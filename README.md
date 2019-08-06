#### Summary
We are sequencing West Nile virus from California, with an emphasis on San Diego, Kern, and Sacramento/Yolo counties, to understand how 1) the virus spreads between regions, 2) is maintained locally between seasons, and 3) the factors that promote local outbreaks. Our goal is to generate thousands of new West Nile virus genomes from infected birds and mosquitoes. This research is part of the [WestNile 4K Project](https://westnile4k.org/).

#### Data
Below is a table showing the count of sequenced  genomes by county.

| County          |   Sequence Count |
| :-------------- | :--------------- |
| sandiego      | 206 |
| kern          | 204 |
| sacramento    | 153 |
| yolo          |  42 |
| losangeles    |  28 |
| fresno        |  17 |
| stanislaus    |  13 |
| butte         |  10 |
| kings         |   9 |
| tulare        |   8 |
| sanbernardino |   6 |
| riverside     |   6 |
| contracosta   |   5 |
| yuba          |   4 |
| sutter        |   4 |
| merced        |   4 |
| shasta        |   3 |
| placer        |   3 |
| lake          |   3 |
| ventura       |   2 |
| solano        |   2 |
| madera        |   2 |
| alameda       |   2 |
| sanjoaquin    |   1 |
| lassen        |   1 |
| glenn         |   1 |
| calaveras     |   1 |
| Total         | 740 |

#### Alignment

Alignment were performed using Mafft. The PHI test was used to test for recombination and RDP4 was used to narrow down sequences with potential contamination. These sequences are in consensus_sequences/contaminated\_sequences.

| Name | MAXCHI | CHIMAERA | SISCAN |
|:-- |:-- |:-- |:--|
| W162 | +      | -        | +      |
| W301 | +      | +        | +      |

The following sequences with <50% coverage of the coding region weren't included in the alignment.

| Name                                           | Length |
|:-- | :-- |
| Consensus_W052_L1_L2_L3_threshold_0_quality_20 |   4244 |
| Consensus_W118_L1_threshold_0_quality_20       |      0 |
| Consensus_W170_L1_threshold_0_quality_20       |   3526 |
| Consensus_W251_L1_threshold_0_quality_20       |   1862 |
| Consensus_W327_L1_threshold_0_quality_20       |   5042 |
| Consensus_W329_L1_threshold_0_quality_20       |   4088 |
| Consensus_W330_L1_threshold_0_quality_20       |   3255 |
| Consensus_W336_L1_threshold_0_quality_20       |   1832 |
| Consensus_W338_L1_threshold_0_quality_20       |   2305 |
| Consensus_W341_L1_threshold_0_quality_20       |    482 |
| Consensus_W501_L1_L2_threshold_0_quality_20    |   4421 |
| Consensus_W662_L1_L2_L3_threshold_0_quality_20 |   4665 |
| Consensus_W804_L1_L2_threshold_0_quality_20    |   2260 |
| Consensus_W805_L1_L2_threshold_0_quality_20    |   2937 |

The samples from San Diego county were provided by Nikos Garfield and Saran Grewal from the [San Diego County Vector Control Program](http://www.sandiegocounty.gov/deh/pests/vector_disease.html). 
The samples from all the other counties in California were provided by Chris Barker, Sarah Wheeler and Ying Fang (University of California, Davis).

The samples from WA were provided by Krisztian Magori from the Eastern Washington University, Amy Salamone, Wayne Clifford and David Kangiser from the Washongton State Department of Health.

The sequencing is being performed using an amplicon-based sequencing scheme using [Primal](http://primal.zibraproject.org/). Our full protocol is available online [here](https://docs.google.com/document/d/1PilT4w5jHO-ROsE8TL5WBGa0wSCdTHAsNl1LIOYiTgk/edit?usp=sharing). Briefly, after preparing cDNA from WNV samples, we generate 38 amplicons, ~400 bp in length, with ~100 bp overlap between amplicons in two PCR reactions. The two amplicon pools are subsequently combined and subjected to standard Illumina library preparation. Sequencing data is processed using the iVar pipeline which we will be released soon.

Stay tuned for new data uploads and preliminary analysis. 

Please note, that the draft_consensus_sequences folder contains genomes that we are still processing to exlucde potential contamination.

**Disclaimer**. Please note that this data is still based on work in progress and should be considered preliminary. If you intend to include any of these data in publications, please let us know – otherwise please feel free to download and use without restrictions. We have shared this data with the hope that people will download and use it, as well as scrutinize it so we can improve our methods and analyses. Please contact us if you have any questions or comments – we’ll buy beers for #ResearchParasites that spot flaws and faults in the data and come up with improvements!

---
**Andersen Lab**  
The Scripps Research Institute  
La Jolla, CA, USA  
[data@andersen-lab.com](mailto:data@andersen-lab.com)

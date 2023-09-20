# Predicting Fruit Fly Longevity from Genome Sequences

This repository contains code and data for a bioinformatics research project to predict longevity phenotypes in the model organism Drosophila melanogaster from genome-wide SNP genotype data.

## Abstract 

This project develops and evaluates a neural network approach for modeling the genotype-phenotype map between genetic variation and lifespan in fruit flies. Genome sequences and matched longevity measurements from 182 Drosophila lines were used to train a simple linear model to predict fly longevity scores from 17,165 SNP genotypes. Model training employed techniques like high dropout rates to mitigate overfitting on the small sample sizes. The results suggest an additive architecture underlies natural variation in fly longevity, without evidence for statistical epistasis. This work provides a demonstration of applying neural network methods to high-dimensional genomic data for complex trait prediction.

## Data

The input SNP data and longevity phenotypes are stored in `phenopred.data.csv` ([Mackay et al. 2012](https://doi.org/10.1038/nature10811)). This file contains:

- `SID`: Unique identifier for each Drosophila line 
- `SNP0` - `SNP17164`: Binary genotype values (0 or 1) for 17,165 SNPs
- `LS`: The quantitative longevity phenotype for each line

## Methods

The Jupyter notebook `phenopred.ipynb` provides code to reproduce the analysis:

- Loading and preprocessing SNP genotypes and phenotypes
- Splitting data into training and validation subsets
- Fitting a linear neural network model with a Dense output layer 
- Training using the Adam optimizer and mean absolute error loss 
- Evaluating model overfitting through dropout, loss trends, and visualization
- Interpreting the additive genetic architecture predicted by the linear model

## Conclusions

The neural network modeling results suggest an additive genetic basis underlies naturally occurring variation in Drosophila longevity, without statistical epistasis effects. The live demonstration highlights challenges in genomics-based prediction including small sample sizes and high dimensionality. This work provides a foundation for future studies of complex trait mapping in model organisms.

## References

Mackay, T.F.C. et al. (2012) The Drosophila melanogaster Genetic Reference Panel. Nature. https://doi.org/10.1038/nature10811

## Contact

Please direct any questions about this research to Dr. [YOUR NAME] at [UNIVERSITY/INSTITUTE EMAIL].

# Patient Journey Analysis with Neo4j Graph Data Science

## Overview
This repository contains three Jupyter Notebooks to demonstrate a Patient Journey analysis using [Synthea Synthetic Patient Data](https://synthea.mitre.org/). These notebooks uses generated Synthea data for approximately 5,000 patients. A smaller Synthea data set is published to the [Github repo](https://www.packtpub.com/product/graph-data-processing-with-cypher/9781804611074) associated with the book [Graph Data Processing with Cypher](https://www.packtpub.com/product/graph-data-processing-with-cypher/9781804611074).

## Notebooks

1. **patientJourney_tabularEDA.ipynb**: This notebook explores and analyzes the Synthea Patient Journey dataset using tabular EDA techniques. It provides insights into the structure, distribution, and relationships within the data that are useful for creating the graph data model.

2. **patientJourney_dataLoad.ipynb**: This notebook demonstrates the process of loading Synthea Patient, Encounter, Procedure, and Drug data into a Neo4j AuraDS instance. 

3. **patientJourney_nodeSimilarity.ipynb**: This notebook performs patient journey analysis on the Synthea dataset using the GDS Node Similarity algorithm, along with embeddings and k-nearest neighbors (KNN). It explores the relationships among patients, encounters, procedures, and drugs, but does not leverage temporal relationships. Creating these is an advanced data modeling topic and the objective of this notebook is to demonstrate the insights available without such a refactoring. 

## Utility Files

- **neoUtils.py**: This utility file contains a function to connect to the Neo4j instance, enabling secure access to the database without exposing login credentials in the Jupyter Notebooks.

## Future Plans
- **KNN-Focused Notebook**: The Node Similarity algorithm is computationally expensive and does not scale well to large data sets. A KNN-focused patient journey notebook is in development and will be posted to this repo once it is available. The Neo4j GDS implementation of KNN scales much better to large data sets, though may not provide the same insights as Node Similarity. 

- **Temporal relationships:** As noted above, the current data loading and analysis notebooks do not use temporal relationships because they are an advanced topic and the initial objective was to demonstrate the insights that could be produced without them. However, a near-term goal is to publish both data loading and analysis notebooks that demonstrate how to use these types of relationships for patient journey analysis. 

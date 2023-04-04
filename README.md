# Synthea Patient Journey Analysis with Neo4j Graph Data Science

## Overview
This repository contains three Jupyter Notebooks to demonstrate a Patient Journey analysis using [Synthea Synthetic Patient Data](https://synthea.mitre.org/). These notebooks uses generated Synthea data for approximately 5,000 patients. A smaller Synthea data set is published to the [Github repo](https://www.packtpub.com/product/graph-data-processing-with-cypher/9781804611074) associated with the book [Graph Data Processing with Cypher](https://www.packtpub.com/product/graph-data-processing-with-cypher/9781804611074).

## Notebooks

1. **patientJourney_tabularEDA.ipynb**: This notebook explores and analyzes the Synthea Patient Journey dataset using tabular EDA techniques. It provides insights into the structure, distribution, and relationships within the data that are useful for creating the graph data model.

2. **patientJourney_dataLoad.ipynb**: This notebook demonstrates the process of loading Synthea Patient, Encounter, Procedure, and Drug data into a Neo4j AuraDS instance. 

3. **patientJourney_nodeSimilarity.ipynb**: This notebook performs patient journey analysis on the Synthea dataset using the GDS Node Similarity algorithm, along with embeddings and k-nearest neighbors (KNN). It explores the relationships among patients, encounters, procedures, and drugs, but does not leverage temporal relationships. Creating these is an advanced data modeling topic and the objective of this notebook is to demonstrate the insights available without such a refactoring. Future notebooks that create and leverage temporal relationships are planned.

## Utility Files

- **neoUtils.py**: This utility file contains a function to connect to the Neo4j instance, enabling secure access to the database without exposing login credentials in the Jupyter Notebooks.

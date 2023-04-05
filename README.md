# Patient Journey Analysis with Neo4j Graph Data Science

## Overview
This repository contains three Jupyter Notebooks to demonstrate a Patient Journey analysis using [Synthea Synthetic Patient Data](https://synthea.mitre.org/). 

## Notebooks

1. **patientJourney_tabularEDA.ipynb**: This notebook explores and analyzes the Synthea Patient Journey dataset using tabular EDA techniques. It provides insights into the structure, distribution, and relationships within the data that are useful for creating the graph data model.

2. **patientJourney_dataLoad.ipynb**: This notebook demonstrates the process of loading Synthea Patient, Encounter, Procedure, and Drug data into a Neo4j AuraDS instance. 

3. **[patientJourney_nodeSimilarity.ipynb](https://github.com/danb-neo4j/patient_journey/blob/main/patientJourney_nodeSimilarity.ipynb)**: This notebook performs patient journey analysis on the Synthea dataset using the GDS Node Similarity algorithm, along with embeddings and k-nearest neighbors (KNN). It explores the relationships among patients, encounters, procedures, and drugs, but does not leverage temporal relationships. Creating these is an advanced data modeling topic and the objective of this notebook is to demonstrate the insights available without such a refactoring. 

## Utility Files

- **neoUtils.py**: This utility file contains a function to connect to the Neo4j instance, enabling secure access to the database without exposing login credentials in the Jupyter Notebooks.

## Synthea Data

- This demo uses generated Synthea data for approximately 5,000 patients. The full data set is [available here](https://drive.google.com/drive/folders/1OqoYdHdW5e0eeeS6Idj3BTtLeDjEgIOz?usp=sharing) and includes a Neo4j Dump file that can be directly loaded into a Neo4j instance.
- A smaller Synthea data set is published to the [Github repo](https://github.com/PacktPublishing/Cypher-Querying) associated with the book [Graph Data Processing with Cypher](https://www.packtpub.com/product/graph-data-processing-with-cypher/9781804611074). 
- This demo uses Patient, Encounter, Procedure, and Drug and leverages the data model demonstrated in book Graph Data Processing with Cypher.

## Future Plans
- **KNN-Focused Notebook**: The Node Similarity algorithm is computationally expensive and does not scale well to large data sets. A KNN-focused patient journey notebook is in development and will be posted to this repo once it is available. The Neo4j GDS implementation of KNN scales much better to large data sets, though may not provide the same insights as Node Similarity. 

- **Temporal Relationships**: As noted above, the current data loading and analysis notebooks do not use temporal relationships because they are an advanced topic and the initial objective was to demonstrate the insights that could be produced without them. However, a near-term goal is to publish both data loading and analysis notebooks that demonstrate how to use these types of relationships for patient journey analysis, emphasizing the GDS Pathfinding algorithms among others. 

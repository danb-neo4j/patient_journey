# collection of functions for Neo4j
import os 
import configparser

# function adapted from Neo4j GDS Fraud Demo Notebook (h/t Zach B.)
def read_neo4j_properties(NEO4J_PROPERTIES_FILE: str=None) -> str:
    '''Parses Neo4j database or Aura connection details from provided .ini filepath.
        Requirements:
        configparser

        Args:
        NEO4J_PROPERTIES_FILE: path to a .ini file

        Returns:
        HOST: link to Neo4j or Aura host 
        USERNAME: login username
        PASSWORD: login password 

        Note: The .ini file should use the following syntax
        [NEO4J]
        PASSWORD=<password>
        USERNAME=<database name>
        HOST=<host uri>

        If no path is passed, the function will return the defaults:
        HOST = 'neo4j://localhost'
        USERNAME = 'neo4j'
        PASSWORD = 'password'
    '''
    if NEO4J_PROPERTIES_FILE is not None and os.path.exists(NEO4J_PROPERTIES_FILE):
        config = configparser.RawConfigParser()
        config.read(NEO4J_PROPERTIES_FILE)
        HOST = config['NEO4J']['HOST']
        USERNAME = config['NEO4J']['USERNAME']
        PASSWORD = config['NEO4J']['PASSWORD']
        print('Using HOST, USERNAME, PASSWORD from .ini file')
        return HOST, USERNAME, PASSWORD
    else:
        print('Could not find database properties file, using defaults:')
        HOST = 'neo4j://localhost'
        USERNAME = 'neo4j'
        PASSWORD = 'password'
        print(f'HOST: {HOST} \nUSERHAME: {USERNAME} \nPASSWORD: {PASSWORD}')
        return HOST, USERNAME, PASSWORD 





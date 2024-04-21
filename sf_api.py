import pandas as pd
from simple_salesforce import Salesforce
from dotenv import load_dotenv

class SfCon():
    def __init__(sefl):
        import os
        sf_client_key = os.getenv("sf_client_key")
        sf_client_secret = os.getenv("sf_client_secret")
        sf_acccess_token = os.getenv("sf_access_token")
        sf_con = Salesforce(
            consumer_key=sf_client_key,
            consumer_secret=sf_client_secret,
            security_token=sf_acccess_token
        )            

if __name__ == '__main__':
    _ = load_dotenv()
    sf_con = SfCon()
    sf_con.

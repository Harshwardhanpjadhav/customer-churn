from src.churn.logger import logging
from src.churn.exception import CustomException
import os
import sys
from src.churn.constants.database import DATABASE_NAME, COLLECTION_NAME
from src.churn.configuration.mongodb_connection.mongodb_conn import MongoDBConnection
import pandas as pd
import numpy as np
from typing import Optional


class GetChurnData:
    def __init__(self):
        try:
            #MongoDBConnection object
            self.mongodb_client = MongoDBConnection(
                database_name=DATABASE_NAME)
        except Exception as e:
            raise CustomException(e, sys)

    def export_collection_as_dataframe(self, collection_name: Optional[str] = None, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            logging.info("Started Converting data to dataframe >>>")

            if database_name is None:
                collection = self.mongodb_client.db[COLLECTION_NAME]
            else:
                collection = self.mongodb_client[database_name][COLLECTION_NAME]
                
                
            # Fetching data from mongo db and stroring in as df
            df = pd.DataFrame(list(collection.find()))

            # Dropping _id column
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)


            # Replacing nan with np.nan
            df.replace({"na": np.nan}, inplace=True)

            # Dropping Unwanted columns
            

            logging.info("Converting data to dataframe Successfull >>>")
            logging.info(df.shape)
            return df

        except Exception as e:
            raise CustomException(e, sys)

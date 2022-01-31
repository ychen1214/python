# code to pip install bs4 package
import sys
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp/pypkg", "bs4"])
sys.path.append("/tmp/pypkg")

from pyspark.sql import DataFrame, SparkSession
from typing import List
import pyspark.sql.types as T
import pyspark.sql.functions as F
import glog
from datetime import date
from google.oauth2 import service_account
from google.cloud import storage
import json
from bs4 import BeautifulSoup

def infer_schema(spark: SparkSession, inputs: List[DataFrame], credentials: str):
    '''Need to define this function to skip schema inference'''
    # TODO: edit this schema with the schema you want you data to output in
    return T.StructType([
        T.StructField("product_title", T.StringType(), True),
    ])

def parse_html(html: str):
    '''
    TODO: modify parse function
    This function will take a single html string and output a tuple with the extracted data. 
    The order of elements in the tuple should match the order of the fields in the schema. 
    '''
    sp = BeautifulSoup(html, 'html.parser')
    # extract product page
    product_title = None
    for span in sp.find_all("span",id="productTitle"):
        product_title = span.get_text()[1:]
    return (product_title, )


def get_blob_data(blob_path, json_key, bucket_name):
    '''
    For blob at blob_path, download and parse the html in the file
    '''
    credentials = service_account.Credentials.from_service_account_info(json_key)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_path)
    html = blob.download_as_bytes()
    record = parse_html(html)
    return record


def transform(spark_session: SparkSession, inputs: List[DataFrame], credentials=None) -> DataFrame:
    """Transforms input DataFrame(s) and returns a single DataFrame as a result

    # Arguments
    spark_session -- Entrypoint into PySpark's Dataset and DataFrame API
    inputs        -- A nonempty List of the input components for this Transform. The index of each
                     input in the list is determined by how the Transform is configured.
    credentials   -- If set (in Advanced Settings), this variable takes upon the string value of the
                     content of the 'Credentials Secret' field.

    # Returns
    Any object of type DataFrame
    """
    # TODO: Create credentials in the Advanced setting. These creds will be brought in through the credentials
    # parameter and will be used to create a GCS client

    # TODO: modify the schema
    schema = T.StructType([
        T.StructField("product_title", T.StringType(), True),
    ])
    
    # Get the current date from upstream
    df0 = inputs[0]
    fetch_date = df0.select("*").collect()[0]["date"]
    
    # creating the gcs client
    json_account_info = json.loads(credentials)  # convert JSON to dictionary
    credentials = service_account.Credentials.from_service_account_info(json_account_info)
    storage_client = storage.Client(credentials=credentials)
    
    # list out all blobs in bucket and filter out blobs with current date
    bucket_name = "data_hoc" #TODO: add bucket name
    prefix = "html/"
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix, delimiter="")
    blob_paths = [b.name for b in blobs]
    glog.info(f"blob_paths: {blob_paths}")
    todays_blobs = [] 
    for bp in blob_paths:
        if len(bp.split('_')) == 3 and bp.split('_')[1] == fetch_date.strftime('%Y%m%d'):
            todays_blobs.append(bp)

    # Create spark RDD with list of blobs from today - this will allow spark to 
    # parse files in parallel. 
    rdd = spark_session.sparkContext.parallelize(todays_blobs)
    records = rdd.flatMap(lambda blob_path: [get_blob_data(blob_path, json_account_info, bucket_name)])
    df = spark_session.createDataFrame(records, schema=schema)
    return df
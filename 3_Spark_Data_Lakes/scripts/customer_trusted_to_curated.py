import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node customer-trusted
customertrusted_node1678144382886 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://dan-gals-bucket/Customers/trusted/"],
        "recurse": True,
    },
    transformation_ctx="customertrusted_node1678144382886",
)

# Script generated for node Accelerometer-landing
Accelerometerlanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://dan-gals-bucket/accelerometer/"],
        "recurse": True,
    },
    transformation_ctx="Accelerometerlanding_node1",
)

# Script generated for node Security Filter
SecurityFilter_node2 = Join.apply(
    frame1=Accelerometerlanding_node1,
    frame2=customertrusted_node1678144382886,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="SecurityFilter_node2",
)

# Script generated for node Drop Fields
DropFields_node1678144544802 = DropFields.apply(
    frame=SecurityFilter_node2,
    paths=["user", "timeStamp", "x", "y", "z"],
    transformation_ctx="DropFields_node1678144544802",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1678144544802,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://dan-gals-bucket/Customers/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()

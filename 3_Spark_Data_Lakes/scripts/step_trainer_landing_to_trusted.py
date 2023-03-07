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

# Script generated for node customer_curated
customer_curated_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://dan-gals-bucket/Customers/curated/"],
        "recurse": True,
    },
    transformation_ctx="customer_curated_node1",
)

# Script generated for node step_trainer_landing
step_trainer_landing_node1678155506606 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://dan-gals-bucket/step-trainer/"],
        "recurse": True,
    },
    transformation_ctx="step_trainer_landing_node1678155506606",
)

# Script generated for node Filter Step Trainer
FilterStepTrainer_node2 = Join.apply(
    frame1=customer_curated_node1,
    frame2=step_trainer_landing_node1678155506606,
    keys1=["serialNumber"],
    keys2=["serialNumber"],
    transformation_ctx="FilterStepTrainer_node2",
)

# Script generated for node Drop Fields
DropFields_node1678155765451 = DropFields.apply(
    frame=FilterStepTrainer_node2,
    paths=[
        "shareWithPublicAsOfDate",
        "birthDay",
        "registrationDate",
        "shareWithResearchAsOfDate",
        "customerName",
        "email",
        "lastUpdateDate",
        "phone",
        "shareWithFriendsAsOfDate",
    ],
    transformation_ctx="DropFields_node1678155765451",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1678155765451,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://dan-gals-bucket/step-trainer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()

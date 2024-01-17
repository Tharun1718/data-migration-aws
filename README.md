# Data Migration and Transformation Tool for amazon rds datawarehouses

## Overview

Data is fetched from an external url and stored in s3 bucket. Then the data is loaded into amazon rds warehouse.

1.**`download.py`**: data extracted from the zip file using this function.

2.**`s3_operations.py`**: data is stored as documents in amazon s3 bucket.

3.**`rds_operations.py`**: documents in the bucket is loaded into the amazon rds warehouse.

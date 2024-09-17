# Data Engineer Take-home Assignment

## Requirements
- Python 3.7+
- Pandas
- Requests
- Pytest (for running tests)

## Setup

1. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Place the provided `Country-Code.xlsx` file** in the project directory.

3. **Run the main script:**
    ```bash
    python src/main.py
    ```

## Explanation

The project is organized into three main steps:

1. **Fetch restaurant details** from the provided URL and save them to `restaurant_details.csv`.
2. **Extract event data** for April 2019 and save it to `restaurant_events.csv`.
3. **Analyze the user ratings** and save the updated data to `restaurant_details_with_ratings.csv`.
#find the answers to the questions listed in the docs in the "output" directory

## Running the Tests

The project includes unit tests to verify that the data extraction, analysis, and utility functions work as expected. The tests are located in the `tests/` directory.

1. **Run the tests** using `pytest`:

    ```bash
    pytest
    ```

2. **Run a specific test file**:

    If you'd like to run tests for a specific file, you can specify the test file:

    ```bash
    pytest tests/test_extract_data.py
    ```

3. **View detailed output**:

    To get detailed output from the tests, use the `-v` flag:

    ```bash
    pytest -v
    ```

## Directory Structure

project_root/
│
├── src/                             # Your source code
│   ├── extract_data.py              # Contains extraction functions
│   ├── main.py                      # Main entry point for the program
│   ├── utils.py                     # Utility functions (e.g., saving/loading)
│   ├── analyze_ratings.py           # Rating analysis logic
│
├── tests/                           # Directory for all test files
│   ├── __init__.py                  # Makes it a package (can be empty)
│   ├── test_extract_data.py         # Unit tests for extract_data.py
│   ├── test_utils.py                # Unit tests for utils.py
│   ├── test_analyze_ratings.py      # Unit tests for analyze_ratings.py
│
├── Country-Code.xlsx                # Excel file for country codes
├── requirements.txt                 # Dependencies (like pytest, pandas, requests)
└── README.md                        # Project documentation


## Notes
- Ensure that you have the `Country-Code.xlsx` file in place before running the main script.
- Make sure your environment meets the requirements listed in `requirements.txt`.


## Cloud-Based Design & Deployment Solution

### Cloud Architecture Design Considerations

In a cloud environment, the goal is to make the system scalable, cost-efficient, and reliable while ensuring security and ease of maintenance. Below is a high-level design for deploying the restaurant data analysis system on cloud services.

#### Components Overview:
1. **Data Ingestion**:
   - **Amazon S3**: The `Country-Code.xlsx` file, along with the restaurant data (JSON), will be stored in an S3 bucket. This makes the data highly accessible and secure with versioning and lifecycle management.
   - **API Gateway + Lambda**: The restaurant data from the provided URL can be ingested using an API Gateway to securely manage HTTP requests. This could trigger a Lambda function that fetches the JSON data and stores it in S3 for further processing.
   
2. **Data Processing**:
   - **AWS Lambda**: This serverless compute service can be used to extract, process, and transform the data from the JSON and Excel files. Lambda is cost-effective and scales automatically, ideal for event-driven processing.
   - **AWS Glue**: A managed ETL (Extract, Transform, Load) service can be used to handle larger or more complex data transformations. Glue could also help manage dependencies between jobs (e.g., fetching data, cleaning it, and analyzing ratings).
   
3. **Data Storage**:
   - **Amazon S3**: The processed data (like CSV files) can be stored back into S3, making it easy to access for downstream services like reporting or dashboards.
   - **Amazon RDS (Relational Database Service)**: Optionally, if frequent querying or relational data storage is needed, the processed restaurant data can be loaded into a MySQL or PostgreSQL RDS instance for structured storage and querying.
   
4. **Analysis & Reporting**:
   - **Amazon Athena**: Athena allows you to query data stored in S3 using SQL. This would be perfect for querying the processed restaurant data, generating reports, and analyzing user ratings. It’s serverless, cost-effective, and scales automatically based on usage.
   - **Amazon QuickSight**: For visualization and reporting, AWS QuickSight can be used to create dashboards from the data in S3 or RDS. QuickSight is highly integrated with AWS services and provides a scalable business intelligence solution.

5. **Security & Access Control**:
   - **IAM Roles**: Fine-grained Identity and Access Management (IAM) roles should be set up to ensure that each service (S3, Lambda, RDS, etc.) only has the necessary permissions.
   - **VPC**: If the system stores sensitive information, it can be deployed inside a Virtual Private Cloud (VPC) for enhanced security, ensuring only authorized access.

6. **Deployment & Monitoring**:
   - **AWS CloudFormation**: Use CloudFormation templates to deploy the infrastructure as code, ensuring repeatability and version control of the infrastructure setup.
   - **AWS CloudWatch**: CloudWatch can be used to monitor the health and performance of Lambda functions, API Gateway, and other AWS services, providing logs and setting up alerts based on resource usage.

#### Decision Considerations:
- **Scalability**: Using services like Lambda and Athena ensures the system can scale based on the load, and there is no need for manual intervention to handle increasing volumes of data.
- **Cost**: The use of serverless services (Lambda, Athena) minimizes costs as you only pay for what you use. Storage in S3 is also cheap and durable.
- **Flexibility**: By using S3 for raw and processed data storage, the architecture is flexible enough to handle different kinds of analytics and data pipelines.
- **Security**: With IAM roles and VPC, the system can be made secure to protect sensitive data.

---

## Architecture Diagram

### Architecture Diagram Description

Below is a textual description of the architecture diagram.

1. **Amazon S3 (Data Storage)**: 
   - Store `Country-Code.xlsx` and the restaurant data (JSON) files.
   - Store the output CSV files (processed restaurant data, analyzed ratings, events data).

2. **API Gateway**:
   - Trigger HTTP requests to ingest restaurant data.
   - Connects to AWS Lambda for the ingestion process.

3. **AWS Lambda (Data Processing)**:
   - Fetch data from the provided URL.
   - Extract, transform, and load the restaurant data and Excel file.
   - Store processed results back into S3.

4. **Amazon Glue (Optional ETL)**:
   - Perform complex ETL operations if necessary, managing dependencies between different stages of data processing.

5. **Amazon RDS (Optional Relational Database)**:
   - Store processed restaurant data in a structured relational database for advanced querying and analysis.

6. **Amazon Athena (Data Analysis)**:
   - Query processed data stored in S3 using SQL.
   - Used for generating reports and insights on the processed restaurant data.

7. **Amazon QuickSight (Reporting)**:
   - Create visualizations and dashboards from the data in S3 or RDS.
   - Used for business intelligence reporting.

8. **Monitoring and Security**:
   - **AWS CloudWatch**: Monitor the performance of Lambda, API Gateway, and other AWS services.
   - **IAM Roles**: Secure access to resources.
   - **VPC (Virtual Private Cloud)**: Optional, to ensure private networking and additional security for sensitive data.


+------------------------------------------------------+
|                   Amazon S3 (Data Storage)           |
|  - Country-Code.xlsx                                  |
|  - Restaurant Data (JSON)                             |
|  - Processed CSV files                                |
+------------------------------------------------------+
                           ^
                           |
                           |
                    +-------------------+
                    |    AWS Lambda     |
                    |  - Fetch data     |
                    |  - Process data   |
                    |  - Store results  |
                    +-------------------+
                           ^
                           |
                           |
                    +--------------------+
                    |    API Gateway     |
                    |  - Ingest data     |
                    +--------------------+
                           |
                           v
                    +-------------------+
                    |   Optional ETL    |
                    | +---------------+ |
                    | |  AWS Glue      | |
                    | | - ETL tasks    | |
                    +-------------------+
                           |
                           v
              +-------------------------------+
              |         Optional Storage       |
              | +---------------------------+  |
              | |       Amazon RDS          |  |
              | | - Store structured data   |  |
              +-------------------------------+
                           |
                           v
              +-------------------------------+
              |       Amazon Athena           |
              | - Query processed data (SQL)  |
              +-------------------------------+
                           |
                           v
              +-------------------------------+
              |     Amazon QuickSight          |
              |  - Reports and Dashboards      |
              +-------------------------------+

        +-------------------------------------------------+
        |        Monitoring and Security                  |
        |  +-------------------------------------------+  |
        |  | AWS CloudWatch: Monitor performance       |  |
        |  | IAM Roles: Secure access control          |  |
        |  | VPC (Optional): Private networking        |  |
        +-------------------------------------------------+

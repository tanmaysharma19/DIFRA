# Data Insights and Financial Reporting Automation (DIFRA)

**Project Description:**

DIFRA (Data Insights and Financial Reporting Automation) is a data-driven solution designed to automate the process of collecting, aggregating, and reporting financial spending data from various vendor sources. This project aims to eliminate manual work, reduce errors, and provide valuable financial insights to streamline financial reporting processes.

**Project Components:**

DIFRA is composed of multiple components, each with its specific responsibility:

1. **Data Lake (Storage):**
   - Responsible for storing raw spending data in a structured manner.
   - Simulated as a local storage solution for the Proof of Concept (POC) phase.
   - Can be extended to cloud-based storage in Phase 2.

2. **Data Ingestion Scheduler:**
   - Manages the scheduling and orchestration of data ingestion processes.
   - Easily extensible to cloud-based scheduling solutions in Phase 2.

3. **Data Ingestion Component:**
   - Responsible for collecting and ingesting data from various sources.
   - Performs data preprocessing and initial processing tasks.
   - Facilitates data cleaning and preparation for aggregation.
     
4. **Data Aggregator:**
   - Aggregates spending data, grouping expenditures by vendor.
   - Utilizes fuzzy string matching to normalize vendor names.
   - Designed for local execution in the POC phase and can transition to cloud-based solutions in Phase 2.

5. **Data Repository:**
   - Stores aggregated spending data for analysis and ML based modeling.
   - Can be implemented as a relational database or cloud-based data warehouse in Phase 2.

6. **Reporting and Visualization:**
   - Generates visual reports and insights from aggregated data.
   - Utilizes Python libraries or third-party BI tools for data visualization.

7. **Notification Service:**
   - Sends automated notifications upon successful data processing or errors.
   - Supports email or cloud-based notification services.

**Getting Started:**

To run individual components of the project, navigate to the respective component folder and execute the `main.py` script. Make sure to configure settings in `config.py` as needed.

**Dependencies:**

- Python 3.x
- Required Python libraries (specified in individual component READMEs)
- External dependencies (e.g., Apache Airflow, cloud storage services) as needed in Phase 2.

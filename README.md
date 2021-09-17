![This is Image](https://www.kindpng.com/picc/m/432-4328812_youtube-analytics-you-tube-logo-hd-png-download.png)
# Youtube_Data_Analysis
Project to analyse the youtube's video data by fetching data through the youtube's **APIs**,
then storing it into **SQLite** database and performing data analysis using queries and other techniques.
### Step 01 : Requirements
* **Create Virtual Environment**

``` virtualenv envs ```

* **Activate Virtual environment**

``` source envs/bin/activate ```

* **Pip the requirements.txt **

 ```pip install -r requirements.txt```

* python == 3.8
* antiorm==1.2.1
* certifi==2021.5.30
* charset-normalizer==2.0.5
* connection==2021.7.20
* db==0.1.1
* db-sqlite3==0.0.1
* idna==3.2
* numpy==1.21.2
* pandas==1.3.3
* python-dateutil==2.8.2
* pytz==2021.1
* requests==2.26.0
* six==1.16.0
* urllib3==1.26.6

### Step 02 : Implementation
- **Create Database connection** 👍

``` connection.py ```

- **Create Tables**
  - Videos
  - Tags
  - Videos_vs_Tags

```create_tables.py```

- **Fetch Data**
  - Use API
  - Keyword (python)
- **Clean up Data**
- **Store data in DB**

``` fetch_data.py ```

### Step 03 : Queries for Analysis Data
* Tag Vs number videos
* Tag with most videos, least videos etc
* Tag vs Avg duration of videos
* Tag with most video time, least video time etc
* Tag Classification
* Classify tags as Tutorials, demos, live coding etc
* And calculate above data for each category

``` analyzer.py ```

* **Output:**
  * As Excel file sheets
  
  ``` Excel_files/ ```
  
* **Some more Queries**
  * tags vs no.of comments
  * tags vs no.of view count
  * tags vs no.of likes count 



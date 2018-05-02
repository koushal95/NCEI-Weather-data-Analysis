from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
import pyspark.sql.functions as sqlf

# Create a Spark Context
sc = SparkContext()

# Create a sql context
sqlc = SQLContext(sc)

# Analysis on the latest 18 years
years = range(2000, 2019)

# Yearly stats
for year in years:
    # get data as raw text
    txtfile = sc.textFile('../data/%s.csv' % year)
    # split attribute values using commas
    data = txtfile.map(lambda x: x.split(','))
    # create table
    table = data.map(lambda r: Row(station=r[0], date=r[1], ele=r[2], val=int(r[3]), m_flag=r[4], q_flag=r[5], s_flag=r[6], obs_time=r[7]))
    # create dataframe
    df = sqlc.createDataFrame(table)

    # Handle abnomalities and missing data
    clean_df = df.filter(df['q_flag'] == '')
import streamlit
import snowflake.connector
import pandas

snow_conn = snowflake.connector.connect(**streamlit.secrets['snowflake'])
snow_cur = snow_conn.cursor()

streamlit.title("Zena\'s Amazing Athleisure Catalog")
snow_cur.execute("SELECT COLOR_OR_STYLE FROM CATALOG_FOR_WEBSITE")
catalog_options = snow_cur.fetchall()
catalog_options = pandas.DataFrame(catalog_options)
streamlit.write(catalog_options)

streamlit.text(catalog_options.iloc[:,0].values.tolist())
# streamlit.text(catalog_options)




snow_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

results = snow_cur.fetchall()

streamlit.text("Calling snowflake now:")
streamlit.text(results)
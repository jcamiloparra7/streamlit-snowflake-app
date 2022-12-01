import streamlit
import snowflake.connector

snow_conn = snowflake.connector.connect(**streamlit.secrets['snowflake'])

streamlit.title("Hello, im a streamlit app")

snow_cur = snow_conn.cursor()

snow_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

results = snow_cur.fetchall()

streamlit.text("Calling snowflake now:")
streamlit.text(results)
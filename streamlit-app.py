import streamlit
import snowflake.connector
import pandas

snow_conn = snowflake.connector.connect(**streamlit.secrets['snowflake'])
snow_cur = snow_conn.cursor()

streamlit.title("Zena\'s Amazing Athleisure Catalog")
snow_cur.execute("SELECT COLOR_OR_STYLE FROM CATALOG_FOR_WEBSITE")
catalog_options = snow_cur.fetchall()
catalog_options = pandas.DataFrame(catalog_options)
# streamlit.write(catalog_options)
catalog_option_list = catalog_options.iloc[:, 0].values.tolist()
chosen_option = streamlit.selectbox('Pick a sweatsuit color or style:', catalog_option_list)
# streamlit.text(catalog_options)
snow_cur.execute(f"SELECT DIRECT_URL, PRICE, SIZE_LIST, UPSELL_PRODUCT_DESC FROM CATALOG_FOR_WEBSITE WHERE COLOR_OR_STYLE = '{chosen_option}'")
option_attr = snow_cur.fetchone()
image_caption = f'Our warm, comfortable, {chosen_option} sweatsuit!'
streamlit.image(option_attr[0], width=400, caption=image_caption)
streamlit.text(f'Price: {option_attr[1]}')
streamlit.text(f'Sizes Available: {option_attr[2]}')
streamlit.text(option_attr[3])

snow_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

results = snow_cur.fetchall()

# streamlit.text("Calling snowflake now:")
# streamlit.text(results)

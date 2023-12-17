import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

st.title("Streamlit - Supabase connector demo")
project_url: str = os.getenv("PROJECT_URL")
api_key: str = os.getenv("API_KEY")

conn=st.connection(name='supabase',project_url=project_url,api_key=api_key)

df=conn.query(table_name="covid_cases",colume_list="*")

print(df.size)
print(df.head())
result = df.groupby('Date')[['Confirmed', 'Deaths','Recovered']].sum().reset_index()
print(result)
st.header('Line chart of Confirmed covid cases vs Date', divider='rainbow')
st.line_chart(result, x="Date", y="Confirmed")
st.header('Line chart of Death covid cases vs Date', divider='rainbow')
st.line_chart(result, x="Date", y="Deaths")
st.header('Line chart of Recovered covid cases vs Date', divider='rainbow')
st.line_chart(result, x="Date", y="Recovered")


result_1 =df.groupby('Country/Region')[['Confirmed', 'Deaths','Recovered']].sum().reset_index()
result_1 = result_1.sort_values(by='Deaths', ascending=False).head(15)
print(result_1)
st.header('Bar chart of Covid Death cases vs Country', divider='rainbow')
st.bar_chart(result_1, x="Country/Region", y="Deaths")
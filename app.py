import streamlit as st
import pandas as pd
import altair as alt



# load dataset
dataf = pd.read_csv("salary Pay by Years.csv")
# set titel to the webapp page
st.title('Job average pay visualisation')
 
# show the dataset and plot it (if checkbox)
def show_data(da_ta, Show = "Show Dataset"):
    if st.checkbox(Show):
        st.write("### Enter the number of rows to view")
        rows = st.number_input("", min_value=0,value=5)
        if rows > 0:
                rows = st.dataframe(da_ta.head(rows))
        st.write(
        alt.Chart(da_ta).mark_point().encode(
            x='Years of Experience',
            y='Average Pay',
            color='Job Title'
        ).configure_axis(
            grid=False
        ) )      
        return show_data
show_data(dataf)


# split the dataset by job titel
def sub_data(data_s):
    data_sub = dataf[dataf["Job Title"]== data_s]
    if data_s == "Data Analyst":
        return data_sub
    elif data_s ==  "Data Scientist":
        return data_sub
    elif data_s ==  "Data Engineer":
            return data_sub


### pie chart
def pie_chart(data_p):
    st.write("average pay",(
    alt.Chart(data_p).mark_arc().encode(
        theta=alt.Theta(field="Average Pay", type="quantitative"),
        color=alt.Color(field="Years of Experience", type="nominal"),
    ) ))
    return (pie_chart )


# bar chart
def bar_chart(data_ub):
    
    st.write(
    alt.Chart(data_ub).mark_bar().encode(
        x='Years of Experience',
        y="Average Pay"
).properties(height=700))
    return bar_chart


# create a function to not repeat some code over and over again

def show_df(df):
    
    if st.button("click here to show data"):
       st.write(df)
    else:
        st.write("-----> the data will be shown here.")
    return show_df


def call_function(dat):
    show_df(dat)
    pie_chart(dat)
    bar_chart(dat)
    return call_function


# dataset subesets
data_analyst = sub_data("Data Analyst")
data_scientist = sub_data("Data Scientist")
data_engineer = sub_data("Data Engineer")
header = "Average pay VS Years of Experience."

with st.sidebar:
 genre = st.radio( "Choose a job titel",
                ("Option:","Data Scientist", "Data Engineer", "Data Analyst"))

if genre == "Option:":
    st.subheader("Choose a job titel on the sidebar")


elif genre == "Data Scientist":
    st.header(header)
    st.subheader("Data Science:")
    call_function(data_scientist)

elif  genre == "Data Engineer":
    st.header(header)
    st.subheader("Data Engineer:")  
    call_function(data_engineer)
   

elif genre == "Data Analyst":
    st.header(header)
    st.subheader("Data Analyst:")
    call_function(data_analyst)
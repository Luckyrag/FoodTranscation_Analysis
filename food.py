# importing all the project necessary libaray
import numpy as np
import pandas as pd
import streamlit as st
import glob                  # working on pattern matching.
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the Home Page (Local-Host)

# Create three columns
col1, col2, col3 = st.columns(3)

# Place the image in the center column
with col2:
    st.image("Logo_main.png",use_container_width=True,width=800)

# Center the title using HTML
st.markdown(
    """
    <h1 style="text-align: center;">Food Distibution Analysis</h1>
    """,
    unsafe_allow_html=True
)
st.sidebar.title("Naigation")
page = st.sidebar.radio("Go to ",["Introduction","Analysis"])

# Mapping the data set using glob module 

# specify the path to xlsx
july_path = "july" 
# load all files in single folder
july_Data = glob.glob(july_path + '/*.xlsx')

july_list=[]
for file in july_Data:
    july_list.append(pd.read_excel(file))


# specify the path to xlsx
aug_path="Aug/"
# load all the files of aug folder with the help of glob libary using glob function
aug_Data= glob.glob(aug_path + '/*.xlsx')

#using read_excel read all data od aug file
aug_list=[]
for a in aug_Data:
    aug_list.append(pd.read_excel(a))
    
# create a new dataframe to store the merged excel files
july_merged = pd.DataFrame()
for jm in july_list:
    july_merged=pd.concat([july_merged,jm],ignore_index=True)
    
# create a new dataframe to store the merged excel life of aug_folder
aug_merged = pd.DataFrame()
for ag in aug_list:
    aug_merged=pd.concat([aug_merged,ag],ignore_index=True)

# changing the formate of date and day for same processing of Data.
july_merged['Date']=july_merged['Date'].dt.strftime('%d-%m-%y')
july_merged['Day']=july_merged['Date'].str[:2]

aug_merged['Date']=aug_merged['Date'].dt.strftime('%d-%m-%y')
aug_merged['Day']=aug_merged['Date'].str[0:2]

# Arranging the columns
july_merged=july_merged[['Sno', 'Date', 'District','Day', 'Total_Cards ', 'Trans', 'AvailedCards_OTP',
       'AvailedCards_Portability', 'AvailedCards_Poffline',
       'Total_AvailedCards', 'Monthly_Trans', 'Monthly_AvailedCards_OTP',
       'Mothly_AvailedCards_portability', 'Mothly_AvailedCards_Poffline',
       'Monthly_Total_AvailedCards', 'Total_Availed %',
       'Poffline%(Against_AvailedCards)']]

aug_merged=aug_merged[['Sno', 'Date', 'District','Day', 'Total_Cards ', 'Trans', 'AvailedCards_OTP',
       'AvailedCards_Portability', 'AvailedCards_Poffline',
       'Total_AvailedCards', 'Monthly_Trans', 'Monthly_AvailedCards_OTP',
       'Mothly_AvailedCards_portability', 'Mothly_AvailedCards_Poffline',
       'Monthly_Total_AvailedCards', 'Total_Availed %',
       'Poffline%(Against_AvailedCards)']]

# merging both the dataframe with 'inner' merged 
Final =pd.merge(july_merged,aug_merged,on=['District','Day'],how='inner') # after mergeing it have various columns so select only usefull from it.
final1=Final[['Sno_x', 'District', 'Day', 'Total_Cards _x', 'Trans_x','Total_AvailedCards_x','Total_Cards _y', 'Trans_y','Total_AvailedCards_y']]


# change the name of columns 
final1.columns=['Sno','District', 'Day','Total_Cards _july', 'Trans_july','Total_AvailedCards_july','Total_Cards _aug', 'Trans_aug','Total_AvailedCards_aug']
final1.set_index('Sno',inplace=True)

# using Group by for the overview
final2=final1.groupby(['Day'])[['Total_Cards _july','Total_AvailedCards_july','Total_Cards _aug','Total_AvailedCards_aug']].sum()
final3=final1.groupby(['Day'])[['Total_AvailedCards_july','Total_AvailedCards_aug']].sum() # for visualization



# Create Functionality of each page
if page == "Introduction":
    # Sub-page navigation for Introduction
    sub_page = st.selectbox("Choose Introduction Sub-Page", ["Overview", "Details"])

    if sub_page == "Overview":
        st.title("Overview")
        st.dataframe(final2, width=700, height=200)
        st.caption(final2.sum())
        # Add a second navigation (radio buttons) for selecting months
        sub_page2 = st.radio("Select Month", ["July", "August"])
        st.subheader("District Wise Allowance")
        if sub_page2 == "July":
           st.write("July_Transcation")
           st.write(july_merged)

        if sub_page2 == "August":
            st.write("August_Transcation")
            st.write(aug_merged)
        

    elif sub_page == "Details":
        st.balloons()
        st.title("Details")
        st.write("#### Dataset statistics")
        st.caption("July_Info")
        st.write(july_merged.describe())
        st.caption("August_Info")
        st.write(aug_merged.describe())


if page == "Analysis":
    st.subheader("Data Visualization")

    # Create the plot
    fig, ax = plt.subplots(figsize=(14, 7))
    final3.plot(kind='bar', ax=ax)
    ax.set_title("July and August Day Wise Transaction", fontdict={'fontsize': 16})
    ax.set_xlabel("Day of month", fontdict={'fontsize': 16})
    ax.set_ylabel("Number of Cards Availed Ration", fontdict={'fontsize': 16})

    # Display the plot in Streamlit
    st.pyplot(fig)

    if st.button("show Line Chart"):
        st.subheader("Line plot")
        fig,ax=plt.subplots(figsize=(14,7))
        ax=final3.plot(kind='line',ax=ax)
        ax.set_title("july and August Day Wise Transcation",fontdict={'fontsize':16})
        ax.set_xlabel("Day of month ",fontdict={'fontsize':16})
        ax.set_ylabel("Number of Cards Availed Ration ",fontdict={'fontsize':16})
        st.pyplot(fig)

    if st.button("Show Shorted Transcation"):
        st.subheader("Day wise Shorted chart")
        fig,ax=(plt.subplots(figsize=(14,7)))
        ax=final2.sort_values('Total_AvailedCards_july')['Total_AvailedCards_july'].plot(kind='bar')
        ax.set_title("Increasing-Day wise Transcestion",fontdict={'fontsize':16})
        ax.set_xlabel("Day of month ",fontdict={'fontsize':16})
        ax.set_ylabel("Number of Cards Availed Ration ",fontdict={'fontsize':16})
        st.pyplot(fig)


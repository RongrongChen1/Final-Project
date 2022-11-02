import streamlit as st
import pandas as pd
import json
# --------------------------------
st.title('Different World Informations')
df_uv = pd.read_csv('USvideos.csv')
df_uv['new_views'] = df_uv[df_uv['views']>1000000].views/1000000
df_uv['thumb_rate'] = df_uv['likes']/df_uv['views']
uv_list = []
i = 0
f = open('US_category_id.json','r')
a = json.load(f)
uv_id = df_uv['category_id'].value_counts().index
for id in uv_id:
    i = 0
    while i<= 31: 
        if int(a['items'][i]['id']) == id:
            uv_list.append(a['items'][i]['snippet']['title'])
        else: 
            pass
        i += 1  
id = {
    'id': uv_id,
    'Corresponding':uv_list,
}
dv_uv = pd.DataFrame(id)
st.write(dv_uv)
st.write('-'*20)
#----------------------------------
# note that you have to use 0.0 and 40.0 given that the data type of population is float
Views_filter = st.slider('Which was affected by views:', 0.0, 225.3, 5.4)  # min, max, default

# create a multi select
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df_uv.category_id.unique(),  # options
     df_uv.category_id.unique())  # defaults

# create a input form
form = st.sidebar.form("Category_id")
category_id_filter = form.text_input('Category_id (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

# # filter by population
df_uv = df_uv[df_uv.new_views >= Views_filter]

# filter by capital
df_uv = df_uv[df_uv.category_id.isin(capital_filter)]

if category_id_filter == 'ALL':
    df_uv = df_uv
else:
    df_uv = df_uv[df_uv.category_id == category_id_filter]
df_uv.loc[:,['views','likes','dislikes','comment_count','thumb_rate']]
# # show dataframe
# st.subheader('City Details:')
# st.write(df[['city', 'country', 'population']])

# # show the plot
# st.subheader('Total Population By Country')
# fig, ax = plt.subplots(figsize=(20, 5))
# pop_sum = df.groupby('country')['population'].sum()
# pop_sum.plot.bar(ax=ax)
# st.pyplot(fig)

# s = pd.Series(df_uv.category_id.isin(capital_filter),index=df_uv.category_id.isin(capital_filter))
# s

# s_sort = s.sort_values(ascending=False)
# fig, ax1 = plt.subplots(figsize = (15, 15))
# color = 'tab:red'
# ax1.set_xlabel('Series')
# ax1.set_ylabel('Weighted proportion', color=color)
# ax1.plot(s_sort.index, s[s_sort.index], color=color)
# ax1.tick_params(axis='y', labelcolor=color)
# plt.xticks(rotation = 60);
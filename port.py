import streamlit as st
import plotly.express as px

df = px.data.iris()

# 在侧边栏创建筛选器
selected_species = st.multiselect("选择品种哈哈哈哈：", df['species'].unique(), default=df['species'].unique())

# 根据筛选器过滤数据
filtered_df = df[df['species'].isin(selected_species)]

# 绘图
fig = px.scatter(filtered_df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)
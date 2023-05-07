import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlitの練習')
# やりたいこと
# 利用者が自分のデータをアップロードし、加工、可視化する。
# データのアップロード部分
# 加工部分
# 可視化部分
# intaractive性

#　まずは基本から
# csvファイルをアップロードしグラフ化するだけのプログラム
st.write('まずはすでにアップロードしておいたCSVファイルをTableとして表示する。'
df = pd.read_csv('newly_confirmed_cases_daily.csv')
st.dataframe(df)
         
chart_data = df[]
st.line_chart(chart_data)
         
        

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

st.header("st.write")

st.write("hellw, *World!* :sunglasses:")

st.write(123)

df = pd.DataFrame({
    "a": [1, 3, 3, 4],
    "b": ["a", "b", "c", "d"]
})
st.write(df)

st.write("以下是一个数据框", df, "以上是一个数据框")

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=["a", "b", "c"]
)
c = alt.Chart(df2).mark_circle().encode(
    x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"]
)
st.write(c)
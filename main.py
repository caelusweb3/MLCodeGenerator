import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import uuid
import os
from PIL import Image
import sidebar

image = Image.open('images/code.png')

st.image(image,
         width=80)
st.title("Machine Learning Code Generator")

"""

[![Star](https://img.shields.io/github/stars/ulgacemre/MLCodeGenerator?style=social)](https://github.com/ulgacemre/MLCodeGenerator)
&nbsp[![Follow](https://img.shields.io/twitter/follow/EmreUlgac?label=Follow&style=social)](https://twitter.com/EmreUlgac)
&nbsp[![Buy me a book](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/ulgacemre)
"""


st.markdown("<br>", unsafe_allow_html=True)
"""Generate your machine learning code:

1. Specify parameters from sidebar
2. Training code will be generated below
3. Download code or run on colab
---
"""
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# Display sidebar and get user inputs.
inputs = sidebar.show()
inputs
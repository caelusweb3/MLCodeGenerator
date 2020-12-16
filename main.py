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
import utils

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


# Display sidebar and get user inputs.
inputs = sidebar.show()
inputs

if inputs["task"] == "Classification":

    # Generate code and notebook based on jinja template.
    env = Environment(
        loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True,
    )
    template = env.get_template(f"classifier.py.jinja")
    code = template.render(header=utils.code_header, notebook=False, **inputs)
    notebook_code = template.render(
        header=utils.notebook_header, notebook=True, **inputs
    )
    notebook = utils.to_notebook(notebook_code)

    # Display donwload/open buttons.
    st.write("")  # add vertical space
    col1, col2, col3 = st.beta_columns(3)
    open_colab = col1.button("🚀 Open in Colab")  # logic handled further down
    with col2:
        utils.download_button(code, "generated-code.py", "🐍 Download (.py)")
    with col3:
        utils.download_button(
            notebook, "generated-notebook.ipynb", "📓 Download (.ipynb)"
        )
    colab_error = st.empty()

    # Display code.
    # TODO: Think about writing Installs on extra line here.
    st.code(code)

    # Handle "Open Colab" button. Down here because to open the new web page, it
    # needs to create a temporary element, which we don't want to show above.
    if open_colab:
        if colab_enabled:
            colab_link = add_to_colab(notebook)
            utils.open_link(colab_link)
        else:
            colab_error.error(
                """
                **Colab support is disabled.** (If you are hosting this: Create a Github 
                repo to store notebooks and register it via a .env file)
                """
            )

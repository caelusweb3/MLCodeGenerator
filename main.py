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
from github import Github
from dotenv import load_dotenv

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

# Set up github access for "Open in Colab" button.
load_dotenv()  # load environment variables from .env file
if os.getenv("GITHUB_TOKEN") and os.getenv("REPO_NAME"):
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(os.getenv("REPO_NAME"))
    colab_enabled = True

    def add_to_colab(notebook):
        """Adds notebook to Colab by pushing it to Github repo and returning Colab link."""
        notebook_id = str(uuid.uuid4())
        repo.create_file(
            f"notebooks/{notebook_id}/generated-notebook.ipynb",
            f"Added notebook {notebook_id}",
            notebook,
        )
        colab_link = f"http://colab.research.google.com/github/{os.getenv('REPO_NAME')}/blob/main/notebooks/{notebook_id}/generated-notebook.ipynb"
        return colab_link


else:
    colab_enabled = False

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
        utils.download_button(code, "code.py", "🐍 Download (.py)")
    with col3:
        utils.download_button(
            notebook, "notebook.ipynb", "📓 Download (.ipynb)"
        )
    colab_error = st.empty()

    # Display code.
    # TODO: Think about writing Installs on extra line here.
    st.code(code)

    # Handle "Open Colab" button. Down here because to open the new web page, it
    # needs to create a temporary element, which we don't want to show above.
    if open_colab:
        if colab_enabled:
            """
            Colab feature coming soon :)
            """
            #colab_link = add_to_colab(notebook)
            #utils.open_link(colab_link)
        else:
            colab_error.error(
                """
                Colab feature coming soon :)
                """
            )

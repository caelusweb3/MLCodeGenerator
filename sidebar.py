
"""
Shows the sidebar for the streamlit app and manages all user inputs.
"""

import streamlit as st

# Define possible models in a dict.
# Format of the dict:
# option 1: framework -> model -> code
# option 2 – if model has multiple variants: framework -> model -> model variant -> code
MODELS = {
    "scikit-learn": {
        "Support vectors": "sklearn.svm.SVC",
        "Random forest": "sklearn.ensemble.RandomForestClassifier",
        "K-nearest neighbors": "sklearn.neighbors.KNeighborsClassifier",
        "Decision tree": "sklearn.tree.DecisionTreeClassifier",
    },
}

classifier_list = ["Random forest","Support vectors","XGBclassifier","Decision tree","Logistic Regression"]




def show():
    """Shows the side bar and returns user inputs as dict."""

    inputs = {}

    with st.sidebar:
        st.write("## Task")
        inputs["task"] = st.selectbox(
            "Which problem do you want to solve?",
            ("Classification", "Regression"),
        )
        if inputs["task"] == "Regression":
            st.write(
                "Coming soon! [Mail me](mailto:johannes.rieke@gmail.com) what you need."
            )
        else:


            st.write("## Model")
            framework = st.multiselect('Choose Classfier',classifier_list)
            inputs["classifier"] = framework

            st.write("## Input Type")
            input_type = st.selectbox('Choose Input Type',['csv','pickle'])
            inputs["input_type"] = input_type

            st.write("## Scaler ")
            scaler_type = st.selectbox('Choose Scaler',['Standard Scaler','Min Max Scaler'])
            inputs["scaler_type"] = scaler_type

            st.write("## Evaluation")
            evaluations = st.multiselect('Choose Evaluations',["Confusion Matrix","Classification Report","Metrics"])
            st.checkbox('YellowBrick Visualization')
            inputs["evaluations"] = evaluations
            

    return inputs
import streamlit as st
import joblib
import numpy as np

cols = ['REGION_No Region', 'REGULARITY', 'TOP_PACK', 'REGION_DAKAR', 'REGION_THIES', 'REGION_SAINT-LOUIS']

reg = st.number_input("Enter Regularity", min_value = 0.0 )

regions = ['No Region', 'DAKAR', 'LOUGA', 'TAMBACOUNDA', 'KAOLACK',
       'THIES', 'SAINT-LOUIS', 'KOLDA', 'KAFFRINE', 'DIOURBEL',
       'ZIGUINCHOR', 'MATAM', 'SEDHIOU', 'KEDOUGOU']

selected_region = st.selectbox("Enter Region", options=regions, index=0)
top_pack = st.number_input("Enter Top Pack",  min_value = 0.0 )

with open("my_log_model.pkl", "rb") as file:
    my_model = joblib.load(file)

if selected_region  == "No Region":
    prediction = my_model.predict(np.array([1, reg, top_pack, 0, 0, 0]).reshape(1,-1))
elif selected_region == "DAKAR":
    prediction = my_model.predict(np.array([0, reg, top_pack, 1, 0, 0]).reshape(1,-1))
elif selected_region == "THIES":
    prediction = my_model.predict(np.array([0, reg, top_pack, 0, 1, 0]).reshape(1,-1))
elif selected_region == "SAINT-LOUIS":
    prediction = my_model.predict(np.array([0, reg, top_pack, 0, 0, 1]).reshape(1,-1))
else:
    prediction = my_model.predict(np.array([0, reg, top_pack, 0, 0, 0]).reshape(1,-1))


if reg and selected_region and top_pack:
    if prediction[0] == 0:
        st.success("The user will not leave ", icon= "✅")
    else:
        st.error("The user will leave!!!")
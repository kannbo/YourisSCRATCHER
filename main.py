import os

a=True

import streamlit as st,uuid,scratchattach as scratch3,os
from multiapp import MultiApp
if len(st.session_state)==0:
    st.session_state["account"]={}
  st.title("あなたはスクラッチャー？")

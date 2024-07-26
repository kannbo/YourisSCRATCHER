import os

a=True

import streamlit as st,uuid,scratchattach as scratch3,os,requests as r
if len(st.session_state)==0:
  st.session_state["test"]="jagajaga"
  st.session_state["ingk"]=0
st.title("あなたはスクラッチャー？")
st.write("あなたは手順に沿って行動してください")
st.write(["あなたの名前を入力",
          "表示されたURLにクラウドを入力",
          "ボタンを押して証明する"])
if st.session_state["ingk"]==0:
  st.session_state["name"]=st.text_input("名前")
  if st.button("送信"):
    st.session_state["ingk"]=1
elif st.session_state["ingk"]==1:
  st.write("https://scratch.mit.edu/projects/1049954829/")
  if st.button("確認"):
    i=""
    aaaa=[i["user"] for i in r.get("https://clouddata.scratch.mit.edu/logs?projectid=1049954829&limit=800&offset=0").json()]
    if st.session_state["name"] in aaaa:
      st.success("あなたはスクラッチャーです!")
    else:
      st.warning("スクラッチャーではない,または数字以外を入力しました。")

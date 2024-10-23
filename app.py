import streamlit as st
import pickle
import numpy as np
import pandas as pd
pipe1=pickle.load(open('./1st_pipe.pkl','rb'))
pipe2=pickle.load(open('./2nd_pipe.pkl','rb'))
st.title("IPL Win Predictor")
cities=['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur','Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban','Centurion', 'East London', 'Johannesburg', 'Kimberley','Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala','Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi','Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai','Lucknow', 'Guwahati', 'Mohali']
teams=['Mumbai Indians','Kolkata Knight Riders','Rajasthan Royals','Chennai Super Kings','Sunrisers Hyderabad','Delhi Capitals','Punjab Kings','Lucknow Super Giants','Gujarat Titans','Royal Challengers Bengaluru']
col1,col2=st.columns(2)
if 'key' not in st.session_state:
    st.session_state['key'] = 0
with col1:
  b1=st.button("1st Innings")
  if b1:
      st.session_state['key'] =1
      st.rerun()
with col2:
  b2=st.button("2nd Innings")
  if b2:
      st.session_state['key'] =2
      st.rerun()
if st.session_state['key'] ==0:
    st.header("Choose the Innings")
if st.session_state['key'] ==1:
    col1,col2=st.columns(2)
    with col1:
        batting_team=st.selectbox('Select the batting team',sorted(teams),key=1)
    with col2:
        bowling_team=st.selectbox('Select the bowling team',sorted(teams),key=2)
    city=st.selectbox('Select the match venue',sorted(cities),key=3)
    col3,col4,col5=st.columns(3)
    with col3:
        score=st.number_input('Current Score',key=4)
    with col4:
        overs=st.number_input('Overs passed',key=5)
    with col5:
        wickets=st.number_input('wickets down',key=6)
    if st.button('Predict Probability'):
        balls_left=120-overs*6
        wickets_left=10-wickets
        crr=score/overs
        input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],'total_runs_scored':[score],'balls_left':[balls_left],'wickets_left':[wickets_left],'CRR':[crr]})
        result=pipe1.predict_proba(input_df)
        loss=result[0][0]
        win=result[0][1]
        st.header(batting_team + " - "+ str(round(win*100))+"%")
        st.header(bowling_team + " - "+ str(round(loss*100))+"%")
if st.session_state['key'] ==2:
    col1,col2=st.columns(2)
    with col1:
        batting_team=st.selectbox('Select the batting team',sorted(teams),key=1)
    with col2:
        bowling_team=st.selectbox('Select the bowling team',sorted(teams),key=2)
    city=st.selectbox('Select the match venue',sorted(cities),key=3)
    target=st.number_input('Target',key=7)
    col3,col4,col5=st.columns(3)
    with col3:
        score=st.number_input('Current Score',key=4)
    with col4:
        overs=st.number_input('Overs passed',key=5)
    with col5:
        wickets=st.number_input('wickets down',key=6)
    if st.button('Predict Probability'):
        runs_left=target-score
        balls_left=120-overs*6
        wickets_left=10-wickets
        crr=score/overs
        rrr=(runs_left*6)/balls_left
        input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'target_runs':[target],'CRR':[crr],'RRR':[rrr]})
        result=pipe2.predict_proba(input_df)
        loss=result[0][0]
        win=result[0][1]
        st.header(batting_team + " - "+ str(round(win*100))+"%")
        st.header(bowling_team + " - "+ str(round(loss*100))+"%")

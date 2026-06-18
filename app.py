from proposal_generator import agent
import streamlit as st

st.set_page_config("Sales Proposal Agent")

st.title("Client Requirement Proposal Generator Agent")

client_mail=st.text_area("Enter the Client Mail : ",height=500)

if st.button("Submit"):

    final_state=agent.invoke({'client_email':client_mail})

    st.write("Proposed Solution : ")
    st.markdown(final_state['final_proposal'])
    st.download_button("Download Proposal",final_state['final_proposal'],'proposal.txt')
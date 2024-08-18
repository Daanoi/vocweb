import streamlit as st


st.set_page_config(page_title="DSAT Vocab", page_icon=":nerd_face:", layout="wide")

#HEADER
with st.container():
    st.subheader("Welcome :wave:")
    st.title("DSAT Vocab Game")
    st.write("Links:")
    st.write("  [DSAT Vocab Game 2024 >](http://localhost:8000)")
    st.write("  [DSAT Vocab Game 2024 Word List >](https://docs.google.com/document/d/1IOYDR5jCS1qen4OxwLI4_s-urNRJS3diMBx7qHMSRRM/edit)")



#CONTACT

with st.container():
    st.write("----")
    st.subheader("Send any vocabs you wish to be added!")
    st.subheader("ex) 'Dan' (vocab) = 'genius' (synonym)")
    st.write('##')

    contact_form = """
    <form action="https://formsubmit.co/dan.kim.daniel.06@gmail.com" method="POST">
        <input tupe="hidden" name=_captcha" value="False">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Enter vocab with its synonym here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

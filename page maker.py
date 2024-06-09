import streamlit as st

def page1():
    st.write("# This is Page 1")
    st.experimental_set_page("Page 2")

def page2():
    st.write("# This is Page 2")

page_names_to_funcs = {
    "Page 1": page1,
    "Page 2": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()




#add more spicy 

import streamlit as st
import streamlit.components.v1 as components

def switch_page(page_name: str):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")
    
    page_name = standardize_name(page_name)

    pages = get_pages("multipage_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")

st.write("# This is the main page")

if st.button("Click me"):
    switch_page("next_page")
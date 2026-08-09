import streamlit as st
from database import create_table, get_articles


st.set_page_config(
    page_title="Security News Dashboard",
    page_icon="🛡️",
    layout="wide"
)

create_table()

st.title("🛡️ Security News Dashboard")
st.caption("Cybersecurity news monitoring dashboard")


# Sidebar
st.sidebar.header("Filters")

articles = get_articles(500)

if not articles:
    st.warning("No news available. Run `python main.py` first.")
    st.stop()


sources = sorted(set(article[2] for article in articles))

selected_source = st.sidebar.selectbox(
    "Source",
    ["All"] + sources
)

search = st.sidebar.text_input(
    "Search",
    placeholder="Search news..."
)


# Filtering
filtered_articles = articles

if selected_source != "All":
    filtered_articles = [
        article
        for article in filtered_articles
        if article[2] == selected_source
    ]

if search:
    search_lower = search.lower()

    filtered_articles = [
        article
        for article in filtered_articles
        if search_lower in article[1].lower()
    ]


# Statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total News", len(articles))

with col2:
    st.metric("Displayed", len(filtered_articles))

with col3:
    st.metric("Sources", len(sources))


st.divider()

# News
for article in filtered_articles:
    article_id, title, source, url, published, summary = article

    st.subheader(title)

    st.write(
        f"**Source:** {source}  \n"
        f"**Published:** {published}"
    )

    if summary:
        st.write(summary)

    st.link_button("Read article", url)

    st.divider()

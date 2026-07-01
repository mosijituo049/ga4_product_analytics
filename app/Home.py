import streamlit as st
import plotly.express as px

from utils import load_css
from src.services import (
    load_dataset_overview,
    load_funnel,
    load_device_distribution,
    load_country_distribution,
    load_source_distribution
)

load_css()

overview = load_dataset_overview()
funnel = load_funnel()
device = load_device_distribution()
country = load_country_distribution()
source = load_source_distribution()

purchase = funnel.loc[
    funnel["stage"] == "Purchase",
    "sessions"
].iloc[0]

conversion = funnel.loc[
    funnel["stage"] == "Purchase",
    "overall_conversion_rate"
].iloc[0]

st.set_page_config(
    page_title="GA4 Product Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 GA4 Product Analytics Platform")

st.caption(
    """
    Monitor user behaviour, identify conversion bottlenecks,
    and predict purchase intent.
    """
)

st.divider()

#Executive Summary
with st.container():
    st.subheader("Executive Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Users",
            f"{overview.iloc[0]['total_users']:,}"
        )

    with col2:

        st.metric(
            "Sessions",
            f"{overview.iloc[0]['total_sessions']:,}"
        )

    with col3:
        st.metric(
            "Purchases",
            f"{purchase:,}"
        )

    with col4:

        st.metric(
            "Conversion",
            f"{conversion:.2f}%"
        )

st.divider()

#Overview
with st.container():
    st.subheader("Overview")

    col5,col6 = st.columns(2)

    with col5:
        fig_funnel = px.funnel(
            funnel,
            y="stage",
            x="sessions"
        )

        st.plotly_chart(
            fig_funnel,
            use_container_width=True
        )

    with col6:
        fig_device = px.pie(
            device,
            names="device_category",
            values="events",
            hole=0.5
        )

        st.plotly_chart(
            fig_device,
            use_container_width=True
        )

    col7,col8 = st.columns(2)

    with col7:
        fig_traffic = px.bar(
            source,
            x="sessions",
            y="session_source",
            orientation="h"
        )

        st.plotly_chart(
            fig_traffic,
            use_container_width=True
        )

    with col8:
        fig_country = px.bar(
            country,
            x="sessions",
            y="country",
            orientation="h"
        )

        st.plotly_chart(fig_country, use_container_width=True)

st.divider()

#Quick Insights
with st.container():
    st.subheader("💡 Quick Insights")
    st.info(
    """
    • Largest drop-off occurs between View Item and Add to Cart.

    • Mobile generates the majority of traffic.

    • Purchase conversion remains below 5%.

    • Funnel optimization should focus on Product Detail Pages.
    """
    )

if __name__ == "__main__":
    print("Home Page")
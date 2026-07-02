import joblib
import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

from utils import load_css
from src.services import (
    load_purchase_prediction
)

prediction_df = load_purchase_prediction()

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "tuned_rf_model.pkl"

model = joblib.load(MODEL_PATH)

OUTPUT_DIR = BASE_DIR / "outputs"

comparison_df = pd.read_csv(
    OUTPUT_DIR / "model_comparison.csv"
)
comparison_df = comparison_df.round(3)

feature_df = pd.read_csv(
    OUTPUT_DIR / "feature_importance.csv"
)

load_css()

st.title("🤖 Purchase Intent Prediction")
st.markdown(
    """
Predict the probability that a user will complete a purchase based on
their session behaviour.
"""
)

st.divider()

best_model = comparison_df.loc[
    comparison_df["ROC-AUC"].idxmax()
]

with st.container():
    st.subheader("📊 Model Performance")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Accuracy",
        f"{best_model['Accuracy']:.3f}"
    )

    col2.metric(
        "Precision",
        f"{best_model['Precision']:.3f}"
    )

    col3.metric(
        "Recall",
        f"{best_model['Recall']:.3f}"
    )

    col4.metric(
        "ROC-AUC",
        f"{best_model['ROC-AUC']:.3f}"
    )

    st.success(
        f"🏆 Best Model: {best_model['Model']}"
    )

st.divider()

with st.container():
    st.subheader("📋 Model Comparison")

    st.dataframe(
        comparison_df,
        use_container_width=True,
        hide_index=True
    )

st.divider()

top_features = (
    feature_df
    .sort_values("Importance", ascending=False)
    .head(15)
)

with st.container():

    st.subheader("📈 Feature Importance")

    fig = px.bar(

        top_features.sort_values("Importance"),

        x="Importance",

        y="Feature",

        orientation="h",

        color="Importance",

        color_continuous_scale="Blues",

        text="Importance"
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )

    fig.update_layout(

        xaxis_title="Importance Score",

        yaxis_title="",

        height=600,

        showlegend=False,

        margin=dict(
            l=10,
            r=10,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info(
        """
    Feature importance indicates how much each feature contributes
    to the Random Forest prediction.

    Higher importance means the feature has greater influence on
    purchase intent.
    """
    )

st.divider()

with st.container():
    st.subheader("📈 High Intent Distribution")

    st.markdown("""
    Predicted purchase intent across all sessions in the dataset.
    """)

    probability = model.predict_proba(prediction_df)[:, 1]
    prediction_df["purchase_probability"] = probability
    prediction_df["intent"] = pd.cut(
        prediction_df["purchase_probability"],
        bins=[0, 0.5, 0.8, 1],
        labels=[
            "Low",
            "Medium",
            "High"
        ]
    )

    intent_summary = (
        prediction_df["intent"]
        .value_counts()
        .rename_axis("Intent")
        .reset_index(name="Sessions")
    )

    intent_summary["Percentage"] = (
        intent_summary["Sessions"]
        / intent_summary["Sessions"].sum()
    )

    fig = px.bar(
        intent_summary,
        x="Intent",
        y="Percentage",
        color="Intent",
        text=intent_summary["Percentage"].map("{:.1%}".format)
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

with st.container():
    st.subheader("🎯 Predict Purchase Intent")

    st.markdown(
        "Enter session information to estimate the probability of purchase."
    )

    left_col, right_col = st.columns(2)

    with left_col:

        session_duration = st.number_input(
            "Session Duration (sec)",
            min_value=0.0,
            value=300.0
        )

        total_events = st.number_input(
            "Total Events",
            min_value=0,
            value=15
        )

        total_engagement_time = st.number_input(
            "Total Engagement Time",
            min_value=0.0,
            value=250.0
        )

        pageviews = st.number_input(
            "Page Views",
            min_value=0,
            value=6
        )

        unique_pages = st.number_input(
            "Unique Pages",
            min_value=0,
            value=4
        )

        item_views = st.number_input(
            "Item Views",
            min_value=0,
            value=3
        )

        searches = st.number_input(
            "Searches",
            min_value=0,
            value=1
        )

        add_to_cart = st.number_input(
            "Add to Cart",
            min_value=0,
            value=1
        )

        begin_checkout = st.selectbox(
            "Checkout Started",
            [0, 1]
        )
    
    with right_col:

        device = st.selectbox(
            "Device",
            [
                "desktop",
                "mobile",
                "tablet"
            ]
        )

        operating_system = st.selectbox(
            "Operating System",
            [
                "Windows",
                "Macintosh",
                "Android",
                "iOS"
            ]
        )

        country = st.text_input(
            "Country",
            value="United States"
        )

        acquisition_channel = st.selectbox(
            "Acquisition Channel",
            [
                "Google",
                "Direct",
                "Other",
                "Unknown"
            ]
        )
    
st.divider()


if st.button(
    "🚀 Predict Purchase Intent",
    use_container_width=True
):
    engagement_per_event = (
        total_engagement_time / total_events
        if total_events > 0 else 0
    )

    item_view_rate = (
        item_views / pageviews
        if pageviews > 0 else 0
    )

    checkout_ratio = (
        begin_checkout / add_to_cart
        if add_to_cart > 0 else 0
    )

    input_df = pd.DataFrame({

        "session_duration_sec":[session_duration],

        "total_events":[total_events],

        "total_engagement_time":[total_engagement_time],

        "pageviews":[pageviews],

        "unique_pages":[unique_pages],

        "item_views":[item_views],

        "searches":[searches],

        "add_to_cart":[add_to_cart],

        "begin_checkout":[begin_checkout],

        "device_category":[device],

        "operating_system":[operating_system],

        "country":[country],

        "acquisition_channel":[acquisition_channel],

        "engagement_per_event":[engagement_per_event],

        "item_view_rate":[item_view_rate],

        "checkout_ratio":[checkout_ratio]

    })

    with st.expander("View Model Input"):
        st.dataframe(input_df)

    probability = model.predict_proba(input_df)[0, 1]

    prediction = model.predict(input_df)[0]

    with st.container(border=True):
        st.subheader("📊 Prediction Result")

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric(
                "Purchase Probability",
                f"{probability:.1%}"
            )

        with result_col2:
            st.metric(
                "Predicted Class",
                "Purchase" if prediction == 1 else "No Purchase"
            )

        
        st.caption("Purchase Probability")

        st.progress(probability)

        if probability >= 0.8:

            st.success("🟢 High Purchase Intent")
            level = "high"

        elif probability >= 0.5:

            st.info("🟡 Medium Purchase Intent")
            level = "medium"

        else:

            st.warning("🔴 Low Purchase Intent")
            level = "low"

    st.divider()

    st.subheader("💡 Recommended Action")

    if level == "high":

        st.success("""
        ### Recommended Action

        - Send personalised promotion
        - Push reminder notification
        - Recommend similar products
        - Prioritise remarketing audience
        """)
    elif level == "medium":

        st.info("""
        ### Recommended Action

        - Continue nurturing
        - Show personalised homepage
        - Recommend trending products
        """)
    
    else:

        st.warning("""
        ### Recommended Action

        - Increase engagement
        - Optimise landing page
        - Improve onboarding experience
        """)
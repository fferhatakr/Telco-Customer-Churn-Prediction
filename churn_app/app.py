import streamlit as st
import pickle
import pandas as pd


with open("xgb_churn_model.pkl", "rb") as f:
    model = pickle.load(f)


KOLONLAR = [
    'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',
    'Partner_1', 'Dependents_1', 'PhoneService_1', 'MultipleLines_1',
    'MultipleLines_No phone service', 'InternetService_DSL',
    'InternetService_Fiber optic', 'OnlineSecurity_1',
    'OnlineSecurity_No internet service', 'OnlineBackup_1',
    'OnlineBackup_No internet service', 'DeviceProtection_1',
    'DeviceProtection_No internet service', 'TechSupport_1',
    'TechSupport_No internet service', 'StreamingTV_1',
    'StreamingTV_No internet service', 'StreamingMovies_1',
    'StreamingMovies_No internet service', 'Contract_One year',
    'Contract_Two year', 'PaperlessBilling_1',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check',
    'Yasli_Kidem_Etkisi', 'Partner_Film'
]

st.title("📉 Müşteri Terk Tahmini")


tenure = st.number_input("Müşteri kaç aydır bizim şirketi tercih ediyor?", 0, 100, 12)
monthly = st.number_input("Aylık Fatura Ücreti Ne Kadar?", 0.0, 500.0, 70.0)
total = st.number_input("Toplam Ödenen Tutar Ne Kadar?", 0.0, 50000.0, 1000.0)
senior = st.selectbox("Müşteri 65 yaş üstü mü?", ["Hayır", "Evet"])


if st.button("Tahmin Et"):

    veri = pd.DataFrame([[0]*len(KOLONLAR)], columns=KOLONLAR)

    veri["tenure"] = tenure
    veri["MonthlyCharges"] = monthly
    veri["TotalCharges"] = total
    veri["SeniorCitizen"] = 1 if senior == "Evet" else 0

    tahmin = model.predict(veri)[0]

    if tahmin == 1:
        st.error("❌ Müşteri yüksek ihtimalle şirketimizi terk edecek")
    else:
        st.success("✅ Müşteri şu anda memnun ve bizi tercih etmeye devam edicek.")
        
    oran = model.predict_proba(veri)[0][1]
    st.write(f"Terk Etme Olasılığı: %{oran*100:.2f}")


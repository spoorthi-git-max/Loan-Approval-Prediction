
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from pandas.api.types import is_numeric_dtype

st.set_page_config(page_title="Loan Approval Prediction", page_icon="💰", layout="wide")
st.title("🏦 Loan Approval Prediction System")

df = pd.read_csv("loan_data_set.csv")

st.header("Dataset Overview")
c1,c2,c3=st.columns(3)
c1.metric("Rows",df.shape[0]); c2.metric("Columns",df.shape[1]); c3.metric("Data Points",df.size)

with st.expander("Preview"):
    st.dataframe(df)

with st.expander("Summary"):
    st.write(df.describe(include="all"))

with st.expander("Missing Values"):
    st.write(df.isnull().sum())

if "Loan_Status" in df.columns:
    fig,ax=plt.subplots()
    vc=df["Loan_Status"].value_counts()
    ax.bar(vc.index.astype(str),vc.values)
    ax.set_xlabel("Loan Status")
    ax.set_ylabel("Count")
    st.pyplot(fig)

df_model=df.copy()
if "Loan_ID" in df_model.columns:
    df_model=df_model.drop(columns=["Loan_ID"])

for col in df_model.columns:
    if is_numeric_dtype(df_model[col]):
        df_model[col]=df_model[col].fillna(df_model[col].mean())
    else:
        df_model[col]=df_model[col].fillna(df_model[col].mode()[0])

encoders={}
for col in df_model.columns:
    if not is_numeric_dtype(df_model[col]):
        le=LabelEncoder()
        df_model[col]=le.fit_transform(df_model[col].astype(str))
        encoders[col]=le

X=df_model.drop(columns=["Loan_Status"])
y=df_model["Loan_Status"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

st.success(f"Model Accuracy: {model.score(X_test,y_test):.2%}")

st.header("Applicant Details")
left,right=st.columns(2)
user_input={}
for i,col in enumerate(X.columns):
    box=left if i%2==0 else right
    with box:
        if col in encoders:
            opts=list(encoders[col].classes_)
            sel=st.selectbox(col.replace("_"," "),opts)
            user_input[col]=encoders[col].transform([sel])[0]
        else:
            if col=="Loan_Amount_Term":
                val=st.selectbox("Loan Amount Term",[12,36,60,120,180,240,300,360])
            elif col=="Credit_History":
                val=st.selectbox("Credit History",[1,0],format_func=lambda x:"Good" if x==1 else "Poor")
            else:
                val=st.number_input(col.replace("_"," "),value=float(X[col].mean()))
            user_input[col]=val

if st.button("Predict Loan Status",use_container_width=True):
    pred=model.predict(pd.DataFrame([user_input]))
    prob=model.predict_proba(pd.DataFrame([user_input]))
    if pred[0]==1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
    conf=float(max(prob[0]))
    st.progress(conf)
    st.write(f"Confidence: {conf*100:.2f}%")

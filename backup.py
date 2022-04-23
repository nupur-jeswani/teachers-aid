import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import io

# setting title of our dashboard
st.set_page_config(
    page_title="Teacher's Aid",
    page_icon=":mortar_board:",
    layout="wide"
)

# importing the dataset and caching it to enhance the performance of our web app


@st.cache
def getData():
    df = pd.read_excel(
        io="datasets//FIRST YEAR//SEM1_SEM2.xlsx",
        engine="openpyxl",
        sheet_name="SEM 1"
    )

    return df


st.header("Teacher's Aid")

st.markdown("---")

st.markdown("<b>Select department and semester to start analyzing - </b>", True)

# filtering options
left, right = st.columns(2)

df = getData()

with left:
    deptSelection = st.selectbox(
        label="Select Department - ",
        options=df["DEPARTMENT"].unique(),
    )

with right:
    semSelection = st.selectbox(
        label="Select Semester - ",
        options=["Semester 1", "Semester 2", "Semester 3", "Semester 4"]
    )


# getting data
@st.cache
def filterData(deptSelection, semSelection, divSelection):
    if semSelection == "Semester 1":
        df1 = pd.read_excel(
            io="datasets//FIRST YEAR//SEM1_SEM2.xlsx",
            engine="openpyxl",
            sheet_name="SEM 1"
        )
    elif semSelection == "Semester 2":
        df1 = pd.read_excel(
            io="datasets//FIRST YEAR//SEM1_SEM2.xlsx",
            engine="openpyxl",
            sheet_name="SEM 2"
        )
    elif semSelection == "Semester 3" and deptSelection == "CMPN":
        df1 = pd.read_excel(
            io="datasets//SECOND YEAR//CMPN//SECOND_YEAR_CMPN.xlsx",
            engine="openpyxl",
            sheet_name="SEM3"
        )
    elif semSelection == "Semester 3" and deptSelection == "ETRX":
        df1 = pd.read_excel(
            io="datasets//SECOND YEAR//ETRX//SECOND_YEAR_ETRX.xlsx",
            engine="openpyxl",
            sheet_name="ETRX_SEM3"
        )
    elif semSelection == "Semester 4" and deptSelection == "ETRX":
        df1 = pd.read_excel(
            io="datasets//SECOND YEAR//ETRX//SECOND_YEAR_ETRX.xlsx",
            engine="openpyxl",
            sheet_name="ETRX_SEM4"
        )
    elif semSelection == "Semester 3" and deptSelection == "EXTC":
        df1 = pd.read_excel(
            io="datasets//SECOND YEAR//EXTC//SECOND_YEAR_EXTC.xlsx",
            engine="openpyxl",
            sheet_name="EXTC_SEM3"
        )
    elif semSelection == "Semester 4" and deptSelection == "EXTC":
        df1 = pd.read_excel(
            io="datasets//SECOND YEAR//EXTC//SECOND_YEAR_EXTC.xlsx",
            engine="openpyxl",
            sheet_name="EXTC_SEM4"
        )
    elif semSelection == "Semester 3" and deptSelection == "INFT":
        df1 = pd.read_excel(
            io="datasets//SECOND YEAR//INFT//SECOND_YEAR_INFT.xlsx",
            engine="openpyxl",
            sheet_name="INFT_SEM3"
        )
    elif semSelection == "Semester 4" and deptSelection == "INFT":
        df1 = pd.read_excel(
            io="datasets//SECOND YEAR//INFT//SECOND_YEAR_INFT.xlsx",
            engine="openpyxl",
            sheet_name="INFT_SEM4"
        )
    elif semSelection == "Semester 3" and deptSelection == "INSTRU":
        df1 = pd.read_excel(
            io="datasets//SECOND YEAR//INSTRU//SECOND_YEAR_INSTRU.xlsx",
            engine="openpyxl",
            sheet_name="INSTRU_SEM3"
        )
    elif semSelection == "Semester 4" and deptSelection == "INSTRU":
        df1 = pd.read_excel(
            io="datasets//SECOND YEAR//INSTRU//SECOND_YEAR_INSTRU.xlsx",
            engine="openpyxl",
            sheet_name="INSTRU_SEM4"
        )
    elif semSelection == "Semester 5" and deptSelection == "CMPN":
        df1 = pd.read_excel(
            io="datasets//THIRD YEAR//CMPN//THIRD_YEAR_CMPN.xlsx",
            engine="openpyxl",
            sheet_name="CMPN_SEM5"
        )
    elif semSelection == "Semester 5" and deptSelection == "ETRX":
        df1 = pd.read_excel(
            io="datasets//THIRD YEAR//ETRX//THIRD_YEAR_ETRX.xlsx",
            engine="openpyxl",
            sheet_name="ETRX_SEM5"
        )
    elif semSelection == "Semester 5" and deptSelection == "EXTC":
        df1 = pd.read_excel(
            io="datasets//THIRD YEAR//EXTC//THIRD_YEAR_EXTC.xlsx",
            engine="openpyxl",
            sheet_name="EXTC_SEM5"
        )
    elif semSelection == "Semester 5" and deptSelection == "INFT":
        df1 = pd.read_excel(
            io="datasets//THIRD YEAR//INFT//THIRD_YEAR_INFT.xlsx",
            engine="openpyxl",
            sheet_name="INFT_SEM5"
        )
    elif semSelection == "Semester 6" and deptSelection == "INFT":
        df1 = pd.read_excel(
            io="datasets//THIRD YEAR//INFT//THIRD_YEAR_INFT.xlsx",
            engine="openpyxl",
            sheet_name="INFT_SEM6"
        )
    elif semSelection == "Semester 5" and deptSelection == "INSTRU":
        df1 = pd.read_excel(
            io="datasets//THIRD YEAR//INSTRU//THIRD_YEAR_INSTRU.xlsx",
            engine="openpyxl",
            sheet_name="INSTRU_SEM5"
        )

    if deptSelection == "INFT":
        df1 = df1[df1["DEPARTMENT"] == "INFT"]

        if divSelection == "All Sections":
            return df1
        if divSelection == "A":
            df1 = df1[df1["CLASS AND SECTION"] == "A"]
        if divSelection == "B":
            df1 = df1[df1["CLASS AND SECTION"] == "B"]
        return df1

    elif deptSelection == "EXTC":
        df1 = df1[df1["DEPARTMENT"] == "EXTC"]

        if divSelection == "All Sections":
            return df1
        if divSelection == "A":
            df1 = df1[df1["CLASS AND SECTION"] == "A"]
        if divSelection == "B":
            df1 = df1[df1["CLASS AND SECTION"] == "B"]
        return df1

    elif deptSelection == "ETRX":
        df1 = df1[df1["DEPARTMENT"] == "ETRX"]

        if divSelection == "D1":
            df1 = df1[df1["CLASS AND SECTION"] == "D1"]
        return df1

    elif deptSelection == "CMPN":
        df1 = df1[df1["DEPARTMENT"] == "CMPN"]

        if divSelection == "All Sections":
            return df1
        if divSelection == "A":
            df1 = df1[df1["CLASS AND SECTION"] == "A"]
        if divSelection == "B":
            df1 = df1[df1["CLASS AND SECTION"] == "B"]
        if divSelection == "C":
            df1 = df1[df1["CLASS AND SECTION"] == "C"]
        return df1

    elif deptSelection == "INSTRU":
        df1 = df1[df1["DEPARTMENT"] == "INSTRU"]

        if divSelection == "D3":
            return df1

    else:
        return st.markdown("<b>The data doesn't exist.</b>")


# based division
if deptSelection == "INFT":
    divSelection = st.selectbox(
        label="Select Section",
        options=["All Sections", "A", "B"]
    )

elif deptSelection == "CMPN":
    divSelection = st.selectbox(
        label="Select Section",
        options=["All Sections", "A", "B", "C"]
    )
elif deptSelection == "EXTC":
    divSelection = st.selectbox(
        label="Select Section",
        options=["All Sections", "A", "B"]
    )
elif deptSelection == "INSTRU":
    divSelection = st.selectbox(
        label="Section - ",
        options=["D3"]
    )
elif deptSelection == "ETRX":
    divSelection = st.selectbox(
        label="Section - ",
        options=["D1"]
    )

# storing data
dataSelection = filterData(deptSelection, semSelection, divSelection)

# displaying information for level 1 filtering

l, r = st.columns(2)

with l:
    st.markdown("<br>", True)
    st.markdown(
        f"<h6>Total Number of students present in {deptSelection, divSelection} - </h6> {dataSelection.shape[0]}", True)

with r:
    st.markdown("<br>", True)
    x = dataSelection["Overall CGPA"].mean()
    st.markdown(
        f"<h6>Average CGPA of {deptSelection, divSelection} - </h6> {round(x)}", True)

st.markdown("<br>", True)
st.dataframe(dataSelection)
st.markdown("---")

# cgpa analysis
st.markdown("<h5>CGPA Analysis</h5>", True)

cgpa = st.slider(
    'Select CGPA value to see the list of students who scored above that value - ', 0, 10, 6)

data3 = dataSelection[dataSelection["Overall CGPA"] >= cgpa]

st.dataframe(data3[["DEPARTMENT", "CLASS AND SECTION",
             "ROLL NO.", "NAME", "Overall CGPA"]], 1300, 400)

st.markdown("---")


if semSelection == "Semester 1":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Physics (Unit Tests)", "Chemistry (Unit Tests)", "Maths (Unit Tests)", "Basic Electrical Engineering (Unit Tests)",
                 "Mechanics (Unit Tests)"]
    )

if semSelection == "Semester 2":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Physics (Unit Tests)", "Chemistry (Unit Tests)", "Maths (Unit Tests)",
                 "C Programming (Unit Tests)", "Engineering Drawing (Unit Tests)"]
    )

if deptSelection == "INFT" and semSelection == "Semester 3":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Engineering Mathematics III (Unit Tests)", "Data Structure and Analysis (Unit Tests)", "Database Management System ( Unit Tests)",
                 "Principle Of Communication ( Unit Tests)", "Paradigms and Computer programming Fundamentals (Unit Tests)", ]
    )

if deptSelection == "INFT" and semSelection == "Semester 4":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Engineering Mathematics-IV (Unit Tests)", "Computer Network and Network Design (Unit Tests)",
                 "Operating System (Unit Tests)", "Automata Theory (Unit Tests)", "Computer Organization and Architecture (Unit Tests)"]
    )

if deptSelection == "CMPN" and semSelection == "Semester 3":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Discrete structure & graph theory (Unit Tests)", "Digital logic & computer architecture (Unit Tests)",
                 "Computer graphics (Unit Tests)", "Data structure (Unit Tests)", "Engineering mathematics (Unit Tests)"]
    )

if deptSelection == "CMPN" and semSelection == "Semester 4":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Engineering mathematics (Unit Tests)", "Database management system (Unit Tests)",
                 "Operating system (Unit Tests)", "Microprocessor (Unit Tests)", "Analysis of algorithm (Unit Tests)"]
    )

if deptSelection == "EXTC" and semSelection == "Semester 3":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Applied mathematics-III (Unit Tests)", "Digital Logic Design (Unit Tests)", "Electronic Devices and Circuits (Unit Tests)",
                 "Electrical Networks (Unit Tests)", "Electronic Instrumentation (Unit Tests)"]
    )

if deptSelection == "EXTC" and semSelection == "Semester 4":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Applied Mathematics-IV (Unit Tests)", "Analog Electronics (Unit Tests)", "Wave Theory and Propagation (Unit Tests)",
                 "Microprocessor and Peripherals (Unit Tests)", "Signal And Systems (Unit Tests)", "Control Systems (Unit Tests)"]
    )

if deptSelection == "ETRX" and semSelection == "Semester 3":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Applied Mathematics-III (Unit Tests)", "Electronic Devices and Circuits I (Unit Tests)", "Digital Circuit Design (Unit Tests)",
                 "Electrical Network Analysis and Synthesis (Unit Tests)", "Electronic Instruments And Measurements (Unit Tests)"]
    )

if deptSelection == "ETRX" and semSelection == "Semester 4":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Applied Mathematics IV (Unit Tests)", "Electronic Devices and Circuits (Unit Tests)", "Microprocessors And Applications (Unit Tests)",
                 "Digital System Design (Unit Tests)", "Principle Of Communication Engineering (Unit Tests)", "Linear Control Systems (Unit Tests)"]
    )

if deptSelection == "INSTRU" and semSelection == "Semester 3":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Engineering Mathematics- III (Unit Tests)", "Transducers- I (Unit Tests)", "Analog Electronics (Unit Tests)",
                 "Digital Electronics (Unit Tests)", "Electrical Networks and Measurements (Unit Tests)", "Object Oriented Programing (Unit Tests)"]
    )

if deptSelection == "INSTRU" and semSelection == "Semester 4":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Engineering Mathematics- IV (Unit Tests)", "Transducers- II (Unit Tests)", "Signal Conditioning & Circuit Design (Unit Tests)",
                 "Feedback Control Systems (Unit Tests)", "Control System Components (Unit Tests)"]
    )


# add average marks of all students in each subject for each exam
# displaying data and charts

def plot1(examSelection):
    data = dataSelection

    if semSelection == "Semester 1":
        if examSelection == "Physics (Unit Tests)":
            fig1 = px.histogram(data, x="PHY UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="PHY UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="PHY AVG", data=data, palette="BuGn_r")

            ut1Avg = data["PHY UT1"].mean()
            ut2Avg = data["PHY UT2"].mean()
            utAvg = data["PHY AVG"].mean()

            belowPassing = data[data["PHY AVG"] < 7]
            belowPassing = belowPassing[[
                "DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME", "PHY UT1", "PHY UT2", "PHY AVG"]]

            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Chemistry (Unit Tests)":
            fig1 = px.histogram(data, x="CHEM UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="CHEM UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="CHEM AVG", data=data, palette="BuGn_r")

            ut1Avg = data["CHEM UT1"].mean()
            ut2Avg = data["CHEM UT2"].mean()
            utAvg = data["CHEM AVG"].mean()

            belowPassing = data[data["CHEM AVG"] < 7]
            belowPassing = belowPassing[[
                "DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME", "CHEM UT1", "CHEM UT2", "CHEM AVG"]]

            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Maths (Unit Tests)":
            fig1 = px.histogram(data, x="MATHS UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="MATHS UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="PHY AVG", data=data, palette="BuGn_r")

            ut1Avg = data["MATHS UT1"].mean()
            ut2Avg = data["MATHS UT2"].mean()
            utAvg = data["MATHS AVG"].mean()

            belowPassing = data[data["MATHS AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION",
                                         "ROLL NO.", "NAME", "MATHS UT1", "MATHS UT2", "MATHS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Basic Electrical Engineering (Unit Tests)":
            fig1 = px.histogram(data, x="BEE UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="BEE UT2 ", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="BEE AVG", data=data, palette="BuGn_r")

            ut1Avg = data["BEE UT1"].mean()
            ut2Avg = data["BEE UT2 "].mean()
            utAvg = data["BEE AVG"].mean()

            belowPassing = data[data["BEE AVG"] < 7]
            belowPassing = belowPassing[[
                "DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME", "BEE UT1", "BEE UT2 ", "BEE AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Mechanics (Unit Tests)":
            fig1 = px.histogram(data, x="MECH UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="MECH UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="MECH AVG", data=data, palette="BuGn_r")

            ut1Avg = data["MECH UT1"].mean()
            ut2Avg = data["MECH UT2"].mean()
            utAvg = data["MECH AVG"].mean()

            belowPassing = data[data["MECH AVG"] < 7]
            belowPassing = belowPassing[[
                "DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME", "MECH UT1", "MECH UT2", "MECH AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

    if semSelection == "Semester 2":
        if examSelection == "Physics (Unit Tests)":
            fig1 = px.histogram(data, x="PHY UT1",
                                marginal="box", hover_data=data.columns)
            fig2 = px.histogram(data, x="PHY UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="PHY AVG", data=data, palette="BuGn_r")

            ut1Avg = data["PHY UT1"].mean()
            ut2Avg = data["PHY UT2"].mean()
            utAvg = data["PHY AVG"].mean()

            belowPassing = data[data["PHY AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME", "PHY UT1",
                                        "PHY UT2", "PHY AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Chemistry (Unit Tests)":
            fig1 = px.histogram(data, x="CHEM UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="CHEM UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(
                x="CHEM AVG", data=data, palette="BuGn_r")

            ut1Avg = data["CHEM UT1"].mean()
            ut2Avg = data["CHEM UT2"].mean()
            utAvg = data["CHEM AVG"].mean()

            belowPassing = data[data["CHEM AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME", "CHEM UT1",
                                        "CHEM UT2", "CHEM AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Maths (Unit Tests)":
            fig1 = px.histogram(data, x="MATHS UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="MATHS UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(
                x="MATHS AVG", data=data, palette="BuGn_r")

            ut1Avg = data["MATHS UT1"].mean()
            ut2Avg = data["MATHS UT2"].mean()
            utAvg = data["MATHS AVG"].mean()

            belowPassing = data[data["MATHS AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION",
                                        "ROLL NO.", "NAME", "MATHS UT1", "MATHS UT2", "MATHS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "C Programming (Unit Tests)":
            fig1 = px.histogram(data, x="C PROG UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="C PROG UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(
                x="C PROG AVG", data=data, palette="BuGn_r")

            ut1Avg = data["C PROG UT1"].mean()
            ut2Avg = data["C PROG UT2"].mean()
            utAvg = data["C PROG AVG"].mean()

            belowPassing = data[data["C PROG AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION",
                                        "ROLL NO.", "NAME", "C PROG UT1", "C PROG UT2", "C PROG AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Engineering Drawing (Unit Tests)":
            fig1 = px.histogram(data, x="ED UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="ED UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(
                x="ED AVG", data=data, palette="BuGn_r")

            ut1Avg = data["ED UT1"].mean()
            ut2Avg = data["ED UT2"].mean()
            utAvg = data["ED AVG"].mean()

            belowPassing = data[data["ED AVG"] < 7]
            belowPassing = belowPassing[[
                "DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME", "ED UT1", "ED UT2", "ED AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

    if semSelection == "Semester 3" and deptSelection == "INFT":
        if examSelection == "Engineering Mathematics III (Unit Tests)":
            fig1 = px.histogram(data, x="ENGINEERING MATHEMATICS 3 UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="ENGINEERING MATHEMATICS 3 UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="ENGINEERING MATHEMATICS 3 AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["ENGINEERING MATHEMATICS 3 UT1"].mean()
            ut2Avg = data["ENGINEERING MATHEMATICS 3 UT2"].mean()
            utAvg = data["ENGINEERING MATHEMATICS 3 AVG"].mean()

            belowPassing = data[data["ENGINEERING MATHEMATICS 3 AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ENGINEERING MATHEMATICS 3 UT1", "ENGINEERING MATHEMATICS 3 UT2", "ENGINEERING MATHEMATICS 3 AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Data Structure and Analysis (Unit Tests)":
            fig1 = px.histogram(data, x="DATA STRUCTURE AND ANALYSIS UT1 ", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="DATA STRUCTURE AND ANALYSIS  UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="DATA STRUCTURE AND ANALYSIS AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["DATA STRUCTURE AND ANALYSIS UT1 "].mean()
            ut2Avg = data["DATA STRUCTURE AND ANALYSIS  UT2"].mean()
            utAvg = data["DATA STRUCTURE AND ANALYSIS AVG"].mean()

            belowPassing = data[data["DATA STRUCTURE AND ANALYSIS AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "DATA STRUCTURE AND ANALYSIS UT1 ", "DATA STRUCTURE AND ANALYSIS  UT2", "DATA STRUCTURE AND ANALYSIS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Database Management System ( Unit Tests)":
            fig1 = px.histogram(data, x="DATABASE MANAGEMENT SYSTEM UT1 ", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="DATABASE MANAGEMENT SYSTEM UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="DATABASE MANAGEMENT SYSTEM AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["DATABASE MANAGEMENT SYSTEM UT1 "].mean()
            ut2Avg = data["DATABASE MANAGEMENT SYSTEM UT2"].mean()
            utAvg = data["DATABASE MANAGEMENT SYSTEM AVG"].mean()

            belowPassing = data[data["DATABASE MANAGEMENT SYSTEM AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "DATABASE MANAGEMENT SYSTEM UT1 ", "DATABASE MANAGEMENT SYSTEM UT2", "DATABASE MANAGEMENT SYSTEM AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Principle Of Communication ( Unit Tests)":
            fig1 = px.histogram(data, x="PRINCIPLES OF COMMUNICATION UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="PRINCIPLES OF COMMUNICATION UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="PRINCIPLES OF COMMUNICATION AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["PRINCIPLES OF COMMUNICATION UT1"].mean()
            ut2Avg = data["PRINCIPLES OF COMMUNICATION UT2"].mean()
            utAvg = data["PRINCIPLES OF COMMUNICATION AVG"].mean()

            belowPassing = data[data["PRINCIPLES OF COMMUNICATION AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "PRINCIPLES OF COMMUNICATION UT1", "PRINCIPLES OF COMMUNICATION UT2", "PRINCIPLES OF COMMUNICATION AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Paradigms and Computer programming Fundamentals (Unit Tests)":
            fig1 = px.histogram(data, x="PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(
                x="PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS AVG", data=data, palette="BuGn_r")

            ut1Avg = data["PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT1"].mean()
            ut2Avg = data["PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT2"].mean()
            utAvg = data["PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS AVG"].mean()

            belowPassing = data[data["PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME", "PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT1", "PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT2", "PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

    if semSelection == "Semester 4" and deptSelection == "INFT":
        if examSelection == "Engineering Mathematics-IV (Unit Tests)":
            fig1 = px.histogram(data, x="APPLIED MATHEMATICS 4 UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="APPLIED MATHEMATICS 4 UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="APPLIED MATHEMATICS 4 AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["APPLIED MATHEMATICS 4 UT1"].mean()
            ut2Avg = data["APPLIED MATHEMATICS 4 UT2"].mean()
            utAvg = data["APPLIED MATHEMATICS 4 AVG"].mean()

            belowPassing = data[data["APPLIED MATHEMATICS 4 AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "APPLIED MATHEMATICS 4 UT1", "APPLIED MATHEMATICS 4 UT2", "APPLIED MATHEMATICS 4 AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Computer Network and Network Design (Unit Tests)":
            fig1 = px.histogram(data, x="COMPUTER NETWORKING UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="COMPUTER NETWORKING UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="COMPUTER NETWORKING AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["COMPUTER NETWORKING UT1"].mean()
            ut2Avg = data["COMPUTER NETWORKING UT2"].mean()
            utAvg = data["COMPUTER NETWORKING AVG"].mean()

            belowPassing = data[data["COMPUTER NETWORKING AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "COMPUTER NETWORKING UT1", "COMPUTER NETWORKING UT2", "COMPUTER NETWORKING AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Computer Organization and Architecture (Unit Tests)":
            fig1 = px.histogram(data, x="COMPUTER ORGANISATION AND ARCHITECTURE UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="COMPUTER ORGANISATION AND ARCHITECTUREUT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="COMPUTER ORGANISATION AND ARCHITECTURE AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["COMPUTER ORGANISATION AND ARCHITECTURE UT1"].mean()
            ut2Avg = data["COMPUTER ORGANISATION AND ARCHITECTUREUT2"].mean()
            utAvg = data["COMPUTER ORGANISATION AND ARCHITECTURE AVG"].mean()

            belowPassing = data[data["COMPUTER ORGANISATION AND ARCHITECTURE AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "COMPUTER ORGANISATION AND ARCHITECTURE UT1", "COMPUTER ORGANISATION AND ARCHITECTUREUT2", "COMPUTER ORGANISATION AND ARCHITECTURE AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Automata Theory (Unit Tests)":
            fig1 = px.histogram(data, x="AUTOMATA THEORY UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="AUTOMATA THEORY UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="AUTOMATA THEORY AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["AUTOMATA THEORY UT1"].mean()
            ut2Avg = data["AUTOMATA THEORY UT2"].mean()
            utAvg = data["AUTOMATA THEORY AVG"].mean()

            belowPassing = data[data["AUTOMATA THEORY AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "AUTOMATA THEORY UT1", "AUTOMATA THEORY UT2", "AUTOMATA THEORY AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Operating System (Unit Tests)":
            fig1 = px.histogram(data, x="OPERATING SYTEM UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="OPERATING SYSTEMS UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="OPERATING SYSTEMS  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["OPERATING SYTEM UT1"].mean()
            ut2Avg = data["OPERATING SYSTEMS UT2"].mean()
            utAvg = data["OPERATING SYSTEMS  AVG"].mean()

            belowPassing = data[data["OPERATING SYSTEMS  AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "OPERATING SYTEM UT1", "OPERATING SYSTEMS UT2", "OPERATING SYSTEMS  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

    if semSelection == "Semester 3" and deptSelection == "CMPN":
        if examSelection == "Discrete structure & graph theory (Unit Tests)":
            fig1 = px.histogram(data, x="DISCRETE STRUCTURE AND GRAPH THEORY UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="DISCRETE STRUCTURE AND GRAPH THEORY UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="DISCRETE STRUCTURE AND GRAPH THEORY AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["DISCRETE STRUCTURE AND GRAPH THEORY UT1"].mean()
            ut2Avg = data["DISCRETE STRUCTURE AND GRAPH THEORY UT2"].mean()
            utAvg = data["DISCRETE STRUCTURE AND GRAPH THEORY AVG"].mean()

            belowPassing = data[data["DISCRETE STRUCTURE AND GRAPH THEORY AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "DISCRETE STRUCTURE AND GRAPH THEORY UT1", "DISCRETE STRUCTURE AND GRAPH THEORY UT2", "DISCRETE STRUCTURE AND GRAPH THEORY AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Digital logic & computer architecture (Unit Tests)":
            fig1 = px.histogram(data, x="DIGITAL LOGIC AND COMPUTER ARCHITECTURE UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="DIGITAL LOGIC AND COMPUTER ARCHITECTURE UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="DIGITAL LOGIC AND COMPUTER ARCHITECTURE AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["DIGITAL LOGIC AND COMPUTER ARCHITECTURE UT1"].mean()
            ut2Avg = data["DIGITAL LOGIC AND COMPUTER ARCHITECTURE UT2"].mean()
            utAvg = data["DIGITAL LOGIC AND COMPUTER ARCHITECTURE AVG"].mean()

            belowPassing = data[data["DIGITAL LOGIC AND COMPUTER ARCHITECTURE AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "DIGITAL LOGIC AND COMPUTER ARCHITECTURE UT1", "DIGITAL LOGIC AND COMPUTER ARCHITECTURE UT2", "DIGITAL LOGIC AND COMPUTER ARCHITECTURE AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Computer graphics (Unit Tests)":
            fig1 = px.histogram(data, x="COMPUTER GRAPHICS UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="COMPUTER GRAPHICS UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="COMPUTER GRAPHICS AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["COMPUTER GRAPHICS UT1"].mean()
            ut2Avg = data["COMPUTER GRAPHICS UT2"].mean()
            utAvg = data["COMPUTER GRAPHICS AVG"].mean()

            belowPassing = data[data["COMPUTER GRAPHICS AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "COMPUTER GRAPHICS UT1", "COMPUTER GRAPHICS UT2", "COMPUTER GRAPHICS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Data structure (Unit Tests)":
            fig1 = px.histogram(data, x="DATA STRUCTURE UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="DATA STRUCTURE UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="DATA STRUCTURE AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["DATA STRUCTURE UT1"].mean()
            ut2Avg = data["DATA STRUCTURE UT2"].mean()
            utAvg = data["DATA STRUCTURE AVG"].mean()

            belowPassing = data[data["DATA STRUCTURE AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "DATA STRUCTURE UT1", "DATA STRUCTURE UT2", "DATA STRUCTURE AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Engineering mathematics (Unit Tests)":
            fig1 = px.histogram(data, x="ENGINEERING MATHEMATICS 3 UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="ENGINEERING MATHEMATICS 3 UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="ENGINEERING MATHEMATICS 3 AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["ENGINEERING MATHEMATICS 3 UT1"].mean()
            ut2Avg = data["ENGINEERING MATHEMATICS 3 UT2"].mean()
            utAvg = data["ENGINEERING MATHEMATICS 3 AVG"].mean()

            belowPassing = data[data["ENGINEERING MATHEMATICS 3 AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ENGINEERING MATHEMATICS 3 UT1", "ENGINEERING MATHEMATICS 3 UT2", "ENGINEERING MATHEMATICS 3 AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

    if semSelection == "Semester 3" and deptSelection == "EXTC":
        if examSelection == "Applied mathematics-III (Unit Tests)":
            fig1 = px.histogram(data, x="APPLIED MATHEMATICS-III UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="APPLIED MATHEMATICS-III UT2", marginal="box",
                                hover_data=data.columns)
            fig3 = plt.figure(figsize=(16, 4))
            sns.countplot(x="APPLIED MATHEMATICS-III  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg = data["APPLIED MATHEMATICS-III UT1"].mean()
            ut2Avg = data["APPLIED MATHEMATICS-III UT2"].mean()
            utAvg = data["APPLIED MATHEMATICS-III  AVG"].mean()

            belowPassing = data[data["APPLIED MATHEMATICS-III  AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "APPLIED MATHEMATICS-III UT1", "APPLIED MATHEMATICS-III UT2", "APPLIED MATHEMATICS-III  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Digital Logic Design (Unit Tests)":
            fig1 = px.histogram(data, x="DIGITAL LOGIC DESIGN UT1", marginal="box",
                                hover_data=data.columns)
            fig2 = px.histogram(data, x="DIGITAL LOGIC DESIGN UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="DIGITAL LOGIC DESIGN AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["DIGITAL LOGIC DESIGN UT1"].mean()
            ut2Avg=data["DIGITAL LOGIC DESIGN UT2"].mean()
            utAvg=data["DIGITAL LOGIC DESIGN AVG"].mean()

            belowPassing=data[data["DIGITAL LOGIC DESIGN AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "DIGITAL LOGIC DESIGN UT1", "DIGITAL LOGIC DESIGN UT2", "DIGITAL LOGIC DESIGN AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Electronic Devices and Circuits (Unit Tests)":
            fig1=px.histogram(data, x="ELECTRONIC DEVICES AND CIRCUITS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ELECTRONIC DEVICES AND CIRCUITS UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ELECTRONIC DEVICES AND CIRCUITS  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ELECTRONIC DEVICES AND CIRCUITS UT1"].mean()
            ut2Avg=data["ELECTRONIC DEVICES AND CIRCUITS UT2"].mean()
            utAvg=data["ELECTRONIC DEVICES AND CIRCUITS  AVG"].mean()

            belowPassing=data[data["ELECTRONIC DEVICES AND CIRCUITS  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ELECTRONIC DEVICES AND CIRCUITS UT1", "ELECTRONIC DEVICES AND CIRCUITS UT2", "ELECTRONIC DEVICES AND CIRCUITS  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Electrical Networks (Unit Tests)":
            fig1=px.histogram(data, x="ELECTRICAL NETWORKS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ELECTRICAL NETWORKS UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ELECTRICAL NETWORKS AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ELECTRICAL NETWORKS UT1"].mean()
            ut2Avg=data["ELECTRICAL NETWORKS UT2"].mean()
            utAvg=data["ELECTRICAL NETWORKS AVG"].mean()

            belowPassing=data[data["ELECTRICAL NETWORKS AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ELECTRICAL NETWORKS UT1", "ELECTRICAL NETWORKS UT2", "ELECTRICAL NETWORKS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Electronic Instrumentation (Unit Tests)":
            fig1=px.histogram(data, x="ELECTRONIC INSTRUMENTATION UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ELECTRONIC INSTRUMENTATION  UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ELECTRONIC INSTRUMENTATION  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ELECTRONIC INSTRUMENTATION UT1"].mean()
            ut2Avg=data["ELECTRONIC INSTRUMENTATION  UT2"].mean()
            utAvg=data["ELECTRONIC INSTRUMENTATION  AVG"].mean()

            belowPassing=data[data["ELECTRONIC INSTRUMENTATION  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ELECTRONIC INSTRUMENTATION UT1", "ELECTRONIC INSTRUMENTATION  UT2", "ELECTRONIC INSTRUMENTATION  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

    if semSelection == "Semester 4" and deptSelection == "EXTC":
        if examSelection == "Applied Mathematics-IV (Unit Tests)":
            fig1=px.histogram(data, x="APPLIED MATHEMATICS 4 UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="APPLIED MATHEMATICS 4 UT2 ", marginal="box",
                                hover_data=data.columns)
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="APPLIED MATHEMATICS 4 AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["APPLIED MATHEMATICS 4 UT1"].mean()
            ut2Avg=data["APPLIED MATHEMATICS 4 UT2 "].mean()
            utAvg=data["APPLIED MATHEMATICS 4 AVG"].mean()

            belowPassing=data[data["APPLIED MATHEMATICS 4 AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "APPLIED MATHEMATICS 4 UT1", "APPLIED MATHEMATICS 4 UT2 ", "APPLIED MATHEMATICS 4 AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Analog Electronics (Unit Tests)":
            fig1=px.histogram(data, x="ANALOG ELECTRONICS -II UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ANALOG ELECTRONICS -II  UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ANALOG ELECTRONICS -II  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ANALOG ELECTRONICS -II UT1"].mean()
            ut2Avg=data["ANALOG ELECTRONICS -II  UT2"].mean()
            utAvg=data["ANALOG ELECTRONICS -II  AVG"].mean()

            belowPassing=data[data["ANALOG ELECTRONICS -II  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ANALOG ELECTRONICS -II UT1", "ANALOG ELECTRONICS -II  UT2", "ANALOG ELECTRONICS -II  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Wave Theory and Propagation (Unit Tests)":
            fig1=px.histogram(data, x="WAVE THEORY AND PROPAGATION UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="WAVE THEORY AND PROPAGATION  UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="WAVE THEORY AND PROPAGATION  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["WAVE THEORY AND PROPAGATION UT1"].mean()
            ut2Avg=data["WAVE THEORY AND PROPAGATION  UT2"].mean()
            utAvg=data["WAVE THEORY AND PROPAGATION  AVG"].mean()

            belowPassing=data[data["WAVE THEORY AND PROPAGATION  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "WAVE THEORY AND PROPAGATION UT1", "WAVE THEORY AND PROPAGATION  UT2", "WAVE THEORY AND PROPAGATION  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Microprocessor and Peripherals (Unit Tests)":
            fig1=px.histogram(data, x="MICROPROCESSORS AND PERIPHERALS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="MICROPROCESSORS AND PERIPHERALS UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="MICROPROCESSORS AND PERIPHERALS AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["MICROPROCESSORS AND PERIPHERALS UT1"].mean()
            ut2Avg=data["MICROPROCESSORS AND PERIPHERALS UT2"].mean()
            utAvg=data["MICROPROCESSORS AND PERIPHERALS AVG"].mean()

            belowPassing=data[data["MICROPROCESSORS AND PERIPHERALS AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "MICROPROCESSORS AND PERIPHERALS UT1", "MICROPROCESSORS AND PERIPHERALS UT2", "MICROPROCESSORS AND PERIPHERALS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Signal And Systems (Unit Tests)":
            fig1=px.histogram(data, x="SIGNALS AND SYSTEMS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="SIGNALS AND SYSTEMS UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="SIGNALS AND SYSTEMS  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["SIGNALS AND SYSTEMS UT1"].mean()
            ut2Avg=data["SIGNALS AND SYSTEMS UT2"].mean()
            utAvg=data["SIGNALS AND SYSTEMS  AVG"].mean()

            belowPassing=data[data["SIGNALS AND SYSTEMS  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "SIGNALS AND SYSTEMS UT1", "SIGNALS AND SYSTEMS UT2", "SIGNALS AND SYSTEMS  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Control Systems (Unit Tests)":
            fig1=px.histogram(data, x="CONTROL SYSTEMS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="CONTROL SYSTEMS  UT2 ")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="CONTROL SYSTEMS  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["CONTROL SYSTEMS UT1"].mean()
            ut2Avg=data["CONTROL SYSTEMS  UT2 "].mean()
            utAvg=data["CONTROL SYSTEMS  AVG"].mean()

            belowPassing=data[data["CONTROL SYSTEMS  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "CONTROL SYSTEMS UT1", "CONTROL SYSTEMS  UT2 ", "CONTROL SYSTEMS  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

    if semSelection == "Semester 3" and deptSelection == "ETRX":
        if examSelection == "Applied Mathematics-III (Unit Tests)":
            fig1=px.histogram(data, x="APPLIED MATHEMATICS -III UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="APPLIED MATHEMATICS -III UT2", marginal="box",
                                hover_data=data.columns)
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="APPLIED MATHEMATICS -III AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["APPLIED MATHEMATICS -III UT1"].mean()
            ut2Avg=data["APPLIED MATHEMATICS -III UT2"].mean()
            utAvg=data["APPLIED MATHEMATICS -III AVG"].mean()

            belowPassing=data[data["APPLIED MATHEMATICS -III AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "APPLIED MATHEMATICS -III UT1", "APPLIED MATHEMATICS -III UT2", "APPLIED MATHEMATICS -III AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Electronic Devices and Circuits I (Unit Tests)":
            fig1=px.histogram(data, x="ELECTRONIC DEVICES AND CIRCUITS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ELECTRONIC DEVICES AND CIRCUITS UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ELECTRONIC DEVICES AND CIRCUITS  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ELECTRONIC DEVICES AND CIRCUITS UT1"].mean()
            ut2Avg=data["ELECTRONIC DEVICES AND CIRCUITS UT2"].mean()
            utAvg=data["ELECTRONIC DEVICES AND CIRCUITS  AVG"].mean()

            belowPassing=data[data["ELECTRONIC DEVICES AND CIRCUITS  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ELECTRONIC DEVICES AND CIRCUITS UT1", "ELECTRONIC DEVICES AND CIRCUITS UT2", "ELECTRONIC DEVICES AND CIRCUITS  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Digital Circuit Design (Unit Tests)":
            fig1=px.histogram(data, x="DIGITAL CIRCUIT DESIGN UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="DIGITAL CIRCUIT DESIGN UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="DIGITAL CIRCUIT DESIGN AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["DIGITAL CIRCUIT DESIGN UT1"].mean()
            ut2Avg=data["DIGITAL CIRCUIT DESIGN UT2"].mean()
            utAvg=data["DIGITAL CIRCUIT DESIGN AVG"].mean()

            belowPassing=data[data["DIGITAL CIRCUIT DESIGN AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "DIGITAL CIRCUIT DESIGN UT1", "DIGITAL CIRCUIT DESIGN UT2", "DIGITAL CIRCUIT DESIGN AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Electrical Network Analysis and Synthesis (Unit Tests)":
            fig1=px.histogram(data, x="ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS UT1"].mean()
            ut2Avg=data["ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS UT2"].mean()
            utAvg=data["ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS AVG"].mean()

            belowPassing=data[data["ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS UT1", "ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS UT2", "ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Electronic Instruments And Measurements (Unit Tests)":
            fig1=px.histogram(data, x="ELECTRONICS INSTRUMENTS AND MEASUREMENTS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ELECTRONICS INSTRUMENTS AND MEASUREMENTS UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ELECTRONICS INSTRUMENTS AND MEASUREMENTS AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ELECTRONICS INSTRUMENTS AND MEASUREMENTS UT1"].mean()
            ut2Avg=data["ELECTRONICS INSTRUMENTS AND MEASUREMENTS UT2"].mean()
            utAvg=data["ELECTRONICS INSTRUMENTS AND MEASUREMENTS AVG"].mean()

            belowPassing=data[data["ELECTRONICS INSTRUMENTS AND MEASUREMENTS AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ELECTRONICS INSTRUMENTS AND MEASUREMENTS UT1", "ELECTRONICS INSTRUMENTS AND MEASUREMENTS UT2", "ELECTRONICS INSTRUMENTS AND MEASUREMENTS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

    if semSelection == "Semester 4" and deptSelection == "ETRX":
        if examSelection == "Applied Mathematics IV (Unit Tests)":
            fig1=px.histogram(data, x="APPLIED MATHEMATICS - IV UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="APPLIED MATHEMATICS - IV UT2", marginal="box",
                                hover_data=data.columns)
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="APPLIED MATHEMATICS - IV AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["APPLIED MATHEMATICS - IV UT1"].mean()
            ut2Avg=data["APPLIED MATHEMATICS - IV UT2"].mean()
            utAvg=data["APPLIED MATHEMATICS - IV AVG"].mean()

            belowPassing=data[data["APPLIED MATHEMATICS - IV AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "APPLIED MATHEMATICS - IV UT1", "APPLIED MATHEMATICS - IV UT2", "APPLIED MATHEMATICS - IV AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Electronic Devices and Circuits (Unit Tests)":
            fig1=px.histogram(data, x="ELECTRONIC DEVICES AND CIRCUITS II UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ELECTRONIC DEVICES AND CIRCUITS II UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ELECTRONIC DEVICES AND CIRCUITS II AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ELECTRONIC DEVICES AND CIRCUITS II UT1"].mean()
            ut2Avg=data["ELECTRONIC DEVICES AND CIRCUITS II UT2"].mean()
            utAvg=data["ELECTRONIC DEVICES AND CIRCUITS II AVG"].mean()

            belowPassing=data[data["ELECTRONIC DEVICES AND CIRCUITS II AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ELECTRONIC DEVICES AND CIRCUITS II UT1", "ELECTRONIC DEVICES AND CIRCUITS II UT2", "ELECTRONIC DEVICES AND CIRCUITS II AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Microprocessors And Applications (Unit Tests)":
            fig1=px.histogram(data, x="MICROPROCESSORS AND APPLICATIONS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="MICROPROCESSORS AND APPLICATIONS UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="MICROPROCESSORS AND APPLICATIONS AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["MICROPROCESSORS AND APPLICATIONS UT1"].mean()
            ut2Avg=data["MICROPROCESSORS AND APPLICATIONS UT2"].mean()
            utAvg=data["MICROPROCESSORS AND APPLICATIONS AVG"].mean()

            belowPassing=data[data["MICROPROCESSORS AND APPLICATIONS AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "MICROPROCESSORS AND APPLICATIONS UT1", "MICROPROCESSORS AND APPLICATIONS UT2", "MICROPROCESSORS AND APPLICATIONS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Digital System Design (Unit Tests)":
            fig1=px.histogram(data, x="DIGITAL SYSTEM DESIGN UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="DIGITAL SYSTEM DESIGN  UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="DIGITAL SYSTEM DESIGN  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["DIGITAL SYSTEM DESIGN UT1"].mean()
            ut2Avg=data["DIGITAL SYSTEM DESIGN  UT2"].mean()
            utAvg=data["DIGITAL SYSTEM DESIGN  AVG"].mean()

            belowPassing=data[data["DIGITAL SYSTEM DESIGN  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "DIGITAL SYSTEM DESIGN UT1", "DIGITAL SYSTEM DESIGN  UT2", "DIGITAL SYSTEM DESIGN  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Principle Of Communication Engineering (Unit Tests)":
            fig1=px.histogram(data, x="PRINCIPLES OF COMMUNICATION ENGINEERING UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="PRINCIPLES OF COMMUNICATION ENGINEERING UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="PRINCIPLES OF COMMUNICATION ENGINEERING AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["PRINCIPLES OF COMMUNICATION ENGINEERING UT1"].mean()
            ut2Avg=data["PRINCIPLES OF COMMUNICATION ENGINEERING UT2"].mean()
            utAvg=data["PRINCIPLES OF COMMUNICATION ENGINEERING AVG"].mean()

            belowPassing=data[data["PRINCIPLES OF COMMUNICATION ENGINEERING AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "PRINCIPLES OF COMMUNICATION ENGINEERING UT1", "PRINCIPLES OF COMMUNICATION ENGINEERING UT2", "PRINCIPLES OF COMMUNICATION ENGINEERING AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Linear Control Systems (Unit Tests)":
            fig1=px.histogram(data, x="LINEAR CONTROL SYSTEMS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="LINEAR CONTROL SYSTEMS  UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="LINEAR CONTROL SYSTEMS  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["LINEAR CONTROL SYSTEMS UT1"].mean()
            ut2Avg=data["LINEAR CONTROL SYSTEMS  UT2"].mean()
            utAvg=data["LINEAR CONTROL SYSTEMS  AVG"].mean()

            belowPassing=data[data["LINEAR CONTROL SYSTEMS  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "LINEAR CONTROL SYSTEMS UT1", "LINEAR CONTROL SYSTEMS  UT2", "LINEAR CONTROL SYSTEMS  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

    if semSelection == "Semester 3" and deptSelection == "INSTRU":
        if examSelection == "Engineering Mathematics- III (Unit Tests)":
            fig1=px.histogram(data, x="ENGINEERING MATHEMATICS 3 UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ENGINEERING MATHEMATICS 3 UT2", marginal="box",
                                hover_data=data.columns)
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ENGINEERING MATHEMATICS 3 AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ENGINEERING MATHEMATICS 3 UT1"].mean()
            ut2Avg=data["ENGINEERING MATHEMATICS 3 UT2"].mean()
            utAvg=data["ENGINEERING MATHEMATICS 3 AVG"].mean()

            belowPassing=data[data["ENGINEERING MATHEMATICS 3 AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ENGINEERING MATHEMATICS 3 UT1", "ENGINEERING MATHEMATICS 3 UT2", "ENGINEERING MATHEMATICS 3 AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Transducers- I (Unit Tests)":
            fig1=px.histogram(data, x="TRANSDUCERS -I UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="TRANSDUCERS -I  UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="TRANSDUCERS -I  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["TRANSDUCERS -I UT1"].mean()
            ut2Avg=data["TRANSDUCERS -I  UT2"].mean()
            utAvg=data["TRANSDUCERS -I  AVG"].mean()

            belowPassing=data[data["TRANSDUCERS -I  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "TRANSDUCERS -I UT1", "TRANSDUCERS -I  UT2", "TRANSDUCERS -I  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Analog Electronics (Unit Tests)":
            fig1=px.histogram(data, x="ANALOG ELECTRONICS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ANALOG ELECTRONICS UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ANALOG ELECTRONICS AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ANALOG ELECTRONICS UT1"].mean()
            ut2Avg=data["ANALOG ELECTRONICS UT2"].mean()
            utAvg=data["ANALOG ELECTRONICS AVG"].mean()

            belowPassing=data[data["ANALOG ELECTRONICS AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ANALOG ELECTRONICS UT1", "ANALOG ELECTRONICS UT2", "ANALOG ELECTRONICS AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Digital Electronics (Unit Tests)":
            fig1=px.histogram(data, x="DIGITAL ELECTRONICS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="DIGITAL ELECTRONICS  UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="DIGITAL ELECTRONICS  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["DIGITAL ELECTRONICS UT1"].mean()
            ut2Avg=data["DIGITAL ELECTRONICS  UT2"].mean()
            utAvg=data["DIGITAL ELECTRONICS  AVG"].mean()

            belowPassing=data[data["DIGITAL ELECTRONICS  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "DIGITAL ELECTRONICS UT1", "DIGITAL ELECTRONICS  UT2", "DIGITAL ELECTRONICS  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Electrical Networks and Measurements (Unit Tests)":
            fig1=px.histogram(data, x="ELECTRICAL NETWORKS AND MEASUREMENTS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ELECTRICAL NETWORKS AND MEASUREMENTS  UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ELECTRICAL NETWORKS AND MEASUREMENTS  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ELECTRICAL NETWORKS AND MEASUREMENTS UT1"].mean()
            ut2Avg=data["ELECTRICAL NETWORKS AND MEASUREMENTS  UT2"].mean()
            utAvg=data["ELECTRICAL NETWORKS AND MEASUREMENTS  AVG"].mean()

            belowPassing=data[data["ELECTRICAL NETWORKS AND MEASUREMENTS  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ELECTRICAL NETWORKS AND MEASUREMENTS UT1", "ELECTRICAL NETWORKS AND MEASUREMENTS  UT2", "ELECTRICAL NETWORKS AND MEASUREMENTS  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Object Oriented Programing (Unit Tests)":
            fig1=px.histogram(data, x="OBJECT ORIENTED PROGRAMMING UT1 ", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="OBJECT ORIENTED PROGRAMMING UT2 ")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="OBJECT ORIENTED PROGRAMMING  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["OBJECT ORIENTED PROGRAMMING UT1 "].mean()
            ut2Avg=data["OBJECT ORIENTED PROGRAMMING UT2 "].mean()
            utAvg=data["OBJECT ORIENTED PROGRAMMING  AVG"].mean()

            belowPassing=data[data["OBJECT ORIENTED PROGRAMMING  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "OBJECT ORIENTED PROGRAMMING UT1 ", "OBJECT ORIENTED PROGRAMMING UT2 ", "OBJECT ORIENTED PROGRAMMING  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

    if semSelection == "Semester 4" and deptSelection == "INSTRU":
        if examSelection == "Engineering Mathematics- IV (Unit Tests)":
            fig1=px.histogram(data, x="ENGINEERING MATHEMATICS 4 UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="ENGINEERING MATHEMATICS 4  UT2", marginal="box",
                                hover_data=data.columns)
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="ENGINEERING MATHEMATICS 4  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["ENGINEERING MATHEMATICS 4 UT1"].mean()
            ut2Avg=data["ENGINEERING MATHEMATICS 4  UT2"].mean()
            utAvg=data["ENGINEERING MATHEMATICS 4  AVG"].mean()

            belowPassing=data[data["ENGINEERING MATHEMATICS 4  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "ENGINEERING MATHEMATICS 4 UT1", "ENGINEERING MATHEMATICS 4  UT2", "ENGINEERING MATHEMATICS 4  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Transducers- II (Unit Tests)":
            fig1=px.histogram(data, x="TRANSDUCERS-II UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="TRANSDUCERS-II UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="TRANSDUCERS-II AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["TRANSDUCERS-II UT1"].mean()
            ut2Avg=data["TRANSDUCERS-II UT2"].mean()
            utAvg=data["TRANSDUCERS-II AVG"].mean()

            belowPassing=data[data["TRANSDUCERS-II AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "TRANSDUCERS-II UT1", "TRANSDUCERS-II UT2", "TRANSDUCERS-II AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Signal Conditioning & Circuit Design (Unit Tests)":
            fig1=px.histogram(data, x="SIGNAL CONDITIONING AND CIRCUIT DESIGN UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="SIGNAL CONDITIONING AND CIRCUIT DESIGN UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="SIGNAL CONDITIONING AND CIRCUIT DESIGN AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["SIGNAL CONDITIONING AND CIRCUIT DESIGN UT1"].mean()
            ut2Avg=data["SIGNAL CONDITIONING AND CIRCUIT DESIGN UT2"].mean()
            utAvg=data["SIGNAL CONDITIONING AND CIRCUIT DESIGN AVG"].mean()

            belowPassing=data[data["SIGNAL CONDITIONING AND CIRCUIT DESIGN AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "SIGNAL CONDITIONING AND CIRCUIT DESIGN UT1", "SIGNAL CONDITIONING AND CIRCUIT DESIGN UT2", "SIGNAL CONDITIONING AND CIRCUIT DESIGN AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Feedback Control Systems (Unit Tests)":
            fig1=px.histogram(data, x="FEEDBACK CONTROL SYSTEMS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="FEEDBACK CONTROL SYSTEMS  UT2 ")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="FEEDBACK CONTROL SYSTEMS  AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["FEEDBACK CONTROL SYSTEMS UT1"].mean()
            ut2Avg=data["FEEDBACK CONTROL SYSTEMS  UT2 "].mean()
            utAvg=data["FEEDBACK CONTROL SYSTEMS  AVG"].mean()

            belowPassing=data[data["FEEDBACK CONTROL SYSTEMS  AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "FEEDBACK CONTROL SYSTEMS UT1", "FEEDBACK CONTROL SYSTEMS  UT2 ", "FEEDBACK CONTROL SYSTEMS  AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing

        elif examSelection == "Control System Components (Unit Tests)":
            fig1=px.histogram(data, x="CONTROL SYSTEM COMPONENTS UT1", marginal="box",
                                hover_data=data.columns)
            fig2=px.histogram(data, x="CONTROL SYSTEM COMPONENTS  UT2")
            fig3=plt.figure(figsize=(16, 4))
            sns.countplot(x="CONTROL SYSTEM COMPONENTS   AVG",
                          data=data, palette="BuGn_r")

            ut1Avg=data["CONTROL SYSTEM COMPONENTS UT1"].mean()
            ut2Avg=data["CONTROL SYSTEM COMPONENTS  UT2"].mean()
            utAvg=data["CONTROL SYSTEM COMPONENTS   AVG"].mean()

            belowPassing=data[data["CONTROL SYSTEM COMPONENTS   AVG"] < 7]
            belowPassing=belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME",
                                         "CONTROL SYSTEM COMPONENTS UT1", "CONTROL SYSTEM COMPONENTS  UT2", "CONTROL SYSTEM COMPONENTS   AVG"]]
            return fig1, fig2, fig3, ut1Avg, ut2Avg, utAvg, belowPassing



plot1, plot2, plot3, x, y, z, data1 = plot1(examSelection)

leftChart, rightChart = st.columns(2)

with leftChart:
    st.plotly_chart(plot1)
    st.markdown(
        f"<h6>Average marks in {examSelection} - {round(x)}</h6>", True)

with rightChart:
    st.plotly_chart(plot2)
    st.markdown(
        f"<h6>Average marks in {examSelection} - {round(y)}</h6>", True)

st.markdown("<br>", True)
st.pyplot(plot3)
st.markdown(f"<h6>Average marks in {examSelection} - {round(z)}</h6>", True)
st.markdown("<br>", True)

st.markdown(
    f"<h6>Students having marks below 7 in {examSelection} - </h6>", True)
    
st.dataframe(data1, 1300, 400)


st.markdown("---")


# individual report card

st.markdown(f"<h5>Search for a particular student's detail in {deptSelection} department - </h5>", True)
studentSelection = st.selectbox(
    label="Select Student",
    options=dataSelection["NAME"].unique(),
)

df4 = dataSelection[dataSelection["NAME"] == studentSelection]
st.markdown("<br><br>", True)


leftSide, rightSide = st.columns(2)

with leftSide:
    st.markdown(f"Name - <b>{df4.iloc[0]['NAME']}</b>", True)
    st.markdown(f"Batch - <b>{df4.iloc[0]['BATCH']}</b>", True)
    st.markdown(f"Department - <b>{df4.iloc[0]['DEPARTMENT']}</b>", True)


with rightSide:
    st.markdown(
        f"Division - <b>{df4.iloc[0]['CLASS AND SECTION']}</b>", True)
    st.markdown(f"Roll number - <b>{df4.iloc[0]['ROLL NO.']}</b>", True)
    st.markdown(f"SGPA for {semSelection} - <b>{df4.iloc[0]['Overall CGPA']}</b>", True)


st.markdown("<br>", True)

with st.expander(f"Subject wise Marks of {df4.iloc[0]['NAME']} - "):
    if semSelection == "Semester 1":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Engineering Physics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['PHY UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['PHY UT2']}", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['PHY AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['PHY S1']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Engineering Chemistry -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['CHEM UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['CHEM UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['CHEM AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['CHEM S1']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Engineering Mathematics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['MATHS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['MATHS UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['MATHS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['MATHS S1']}</b>", True)

        with marksRight :
            st.markdown("<h6> Basics of Electrical Engineering -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['BEE UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['BEE UT2 ']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['BEE AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['BEE S1 ']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Engineering Mechanics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['MECH UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['MECH UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['MECH AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['MECH S1']}</b>", True)

    if semSelection == "Semester 2":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Engineering Physics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['PHY UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['PHY UT2']}", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['PHY AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['PHY S2']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Engineering Chemistry -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['CHEM UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['CHEM UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['CHEM AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['CHEM S2']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Engineering Mathematics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['MATHS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['MATHS UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['MATHS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['MATHS S2']}</b>", True)

        with marksRight :
            st.markdown("<h6> C Programming -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['C PROG UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['C PROG UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['C PROG AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['C PROG S2']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Engineering Drawing -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ED UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ED UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ED AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ED S2']}</b>", True)
    
    if semSelection == "Semester 3" and deptSelection == "INFT":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Engineering Mathematics 3 -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 S3']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Data Structure and Analysis -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['DATA STRUCTURE AND ANALYSIS UT1 ']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['DATA STRUCTURE AND ANALYSIS  UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['DATA STRUCTURE AND ANALYSIS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['DATA STRUCTURE AND ANALYSIS S3']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Database Management System -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['DATABASE MANAGEMENT SYSTEM UT1 ']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['DATABASE MANAGEMENT SYSTEM UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['DATABASE MANAGEMENT SYSTEM AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['DATABASE MANAGEMENT SYSTEM S3']}</b>", True)

        with marksRight :
            st.markdown("<h6> Principles of Communication -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['PRINCIPLES OF COMMUNICATION UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['PRINCIPLES OF COMMUNICATION UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['PRINCIPLES OF COMMUNICATION AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['PRINCIPLES OF COMMUNICATION  S3']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Paradigms and computer programming fundamentals -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS S3']}</b>", True)
    
    if semSelection == "Semester 4" and deptSelection == "INFT":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Applied Mathematics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['APPLIED MATHEMATICS 4 UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['APPLIED MATHEMATICS 4 UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['APPLIED MATHEMATICS 4 AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['APPLIED MATHEMATICS 4 S4']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Computer Networking -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['COMPUTER NETWORKING UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['COMPUTER NETWORKING UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['COMPUTER NETWORKING AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['COMPUTER NETWORKING S4']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Computer Organization and its Architecture -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['COMPUTER ORGANISATION AND ARCHITECTURE UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['COMPUTER ORGANISATION AND ARCHITECTUREUT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['COMPUTER ORGANISATION AND ARCHITECTURE AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['COMPUTER ORGANISATION AND ARCHITECTURE S4']}</b>", True)

        with marksRight :
            st.markdown("<h6> Automata Theory -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['AUTOMATA THEORY UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['AUTOMATA THEORY UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['AUTOMATA THEORY AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['AUTOMATA THEORYS4']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Operating Systems -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['OPERATING SYTEM UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['OPERATING SYSTEMS UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['OPERATING SYSTEMS  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['OPERATING SYSTEM S4']}</b>", True)
    
    if semSelection == "Semester 5" and deptSelection == "INFT":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Internet Programming -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['INTERNET PROGRAMMING UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['INTERNET PROGRAMMING UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['INTERNET PROGRAMMINGAVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['INTERNET PROGRAMMING S5']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Computer Networking and Security -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['COMPUTER NETWORKING AND SECURITY UT1 ']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['COMPUTER NETWORKING AND SECURITY UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['COMPUTER NETWORKING AND SECURITYAVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['COMPUTER NETWORKING AND SECURITY S5']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Entrepreneurship and E-Business -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ENTREPRENEURSHIP AND E-BUSINESS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ENTREPRENEURSHIP AND E-BUSINESS UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ENTREPRENEURSHIP AND E-BUSINESS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ENTREPRENEURSHIP E-BUSINESS S5']}</b>", True)

        with marksRight :
            st.markdown("<h6> Software Engineering -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['SOFTWARE ENGINEERING UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['SOFTWARE ENGINEERING UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['SOFTWARE ENGINEERING AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['SOFTWARE ENGINEERING S5']}</b>", True)
            
            st.markdown("<br>", True)

            if df4.iloc[0]['ADVANCE DATAMANAGEMENT TECHNOLOGIESAVG'] == 0:
                st.markdown()
            else:
                st.markdown("<h6> Advance Data Management Technologies -  </h6>", True)
                st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ADVANCE DATAMANAGEMENT TECHNOLOGIES UT1 ']}<b>", True)
                st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ADVANCE DATAMANAGEMENT TECHNOLOGIES UT2']}<b>", True)
                st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ADVANCE DATAMANAGEMENT TECHNOLOGIESAVG']}</b>", True)
                st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ADVANCE DATAMANAGEMENT TECHNOLOGIES S5']}</b>", True)
        
            st.markdown("<br>", True)

            if df4.iloc[0]['ADVANCE DATA STRUCTURE AND ANALYSIS AVG'] == 0:
                st.markdown()
            else:
                st.markdown("<h6> Advance Data Structure and Analysis -  </h6>", True)
                st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ADVANCE DATA STRUCTURE AND ANALYSIS UT1 ']}<b>", True)
                st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ADVANCE DATA STRUCTURE AND ANALYSIS UT2']}<b>", True)
                st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ADVANCE DATA STRUCTURE AND ANALYSIS AVG']}</b>", True)
                st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ADVANCE DATA STRUCTURE AND ANALYSIS S5']}</b>", True)
    
    if semSelection == "Semester 6" and deptSelection == "INFT":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Web X.0 -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['WEB X.0 UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['WEB X.0 UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['WEB X.0 AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['WEB X S6']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Artifical Intelligence and Data Science -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ARTIFICIAL INTELLIGENCE AND DATA SCIENCE UT1 ']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ARTIFICIAL INTELLIGENCE AND DATA SCIENCE UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ARTIFICIAL INTELLIGENCE AND DATA SCIENCE AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['AIDS S6']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Data Mining and Business Intelligence -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['DATA MINING AND BUSINESS INTELLIGENCE UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['DATA MINING AND BUSINESS INTELLIGENCE UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['DATA MINING AND BUSINESS INTELLIGENCE AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['DMBI S6']}</b>", True)

        with marksRight :
            st.markdown("<h6> Wireless Technology -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['WIRELESS TECHNOLOGY UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['WT UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['WT AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['WT S6']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Ethical Hacking and Forensics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['EHF UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['EHF UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['EHF AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['EHF S6']}</b>", True)
    
    if semSelection == "Semester 3" and deptSelection == "CMPN":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Engineering Mathematics 3 -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 S3']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Discrete Structure and Graph Theory -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['DISCRETE STRUCTURE AND GRAPH THEORY UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['DISCRETE STRUCTURE AND GRAPH THEORY UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['DISCRETE STRUCTURE AND GRAPH THEORY AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['DISCRETE STRUCTURE AND GRAPH THEORY S3']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Digital Logic and Computer Architecture -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['DIGITAL LOGIC AND COMPUTER ARCHITECTURE UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['DIGITAL LOGIC AND COMPUTER ARCHITECTURE UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['DIGITAL LOGIC AND COMPUTER ARCHITECTURE AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['DIGITAL LOGIC AND COMPUTER ARCHITECTURE S3']}</b>", True)

        with marksRight :
            st.markdown("<h6> Computer Graphics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['COMPUTER GRAPHICS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['COMPUTER GRAPHICS UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['COMPUTER GRAPHICS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['COMPUTER GRAPHICS S3']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Data Structures -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['DATA STRUCTURE UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['DATA STRUCTURE UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['DATA STRUCTURE AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['DATA STRUCTURE S3']}</b>", True)
    
    if semSelection == "Semester 3" and deptSelection == "INSTRU":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Engineering Mathematics 3 -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 3 S3']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Transducers - I -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['TRANSDUCERS -I UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['TRANSDUCERS -I  UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['TRANSDUCERS -I  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['TRANSDUCERS- I S3']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Analog Electronics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ANALOG ELECTRONICS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ANALOG ELECTRONICS UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ANALOG ELECTRONICS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ANALOG ELECTRONICS S3']}</b>", True)

        with marksRight :
            st.markdown("<h6> Digital Electronics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['DIGITAL ELECTRONICS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['DIGITAL ELECTRONICS  UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['DIGITAL ELECTRONICS  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['DIGITAL ELECTRONICS S3']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Electrical Networks and Measurements -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ELECTRICAL NETWORKS AND MEASUREMENTS UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ELECTRICAL NETWORKS AND MEASUREMENTS  UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ELECTRICAL NETWORKS AND MEASUREMENTS  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ELECTRICAL NETWORKS AND MEASUREMENTS S3']}</b>", True)

            st.markdown("<br>", True)
            
            st.markdown("<h6> Object Oriented Programming -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['OBJECT ORIENTED PROGRAMMING UT1 ']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['OBJECT ORIENTED PROGRAMMING UT2 ']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['OBJECT ORIENTED PROGRAMMING  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['OBJECT ORIENTED PROGRAMMING S3']}</b>", True)
    
    if semSelection == "Semester 4" and deptSelection == "INSTRU":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Engineering Mathematics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 4 UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 4  UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 4  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ENGINEERING MATHEMATICS 4 S4']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Transducers - II -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['TRANSDUCERS-II UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['TRANSDUCERS-II UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['TRANSDUCERS-II AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['TRANSDUCERS-II  S4']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Signal Conditioning and Circuit Design -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['SIGNAL CONDITIONING AND CIRCUIT DESIGN UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['SIGNAL CONDITIONING AND CIRCUIT DESIGN UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['SIGNAL CONDITIONING AND CIRCUIT DESIGN AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['SIGNAL CONDITIONING AND CIRCUIT DESIGN S4']}</b>", True)

        with marksRight :
            st.markdown("<h6> Feedback Control Systems -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['FEEDBACK CONTROL SYSTEMS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['FEEDBACK CONTROL SYSTEMS  UT2 ']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['FEEDBACK CONTROL SYSTEMS  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['FEEDBACK CONTROL SYSTEMS  S4']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Control System Components -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['CONTROL SYSTEM COMPONENTS UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['CONTROL SYSTEM COMPONENTS  UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['CONTROL SYSTEM COMPONENTS   AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['CONTROL SYSTEM COMPONENTS S4']}</b>", True)
    
    if semSelection == "Semester 3" and deptSelection == "ETRX":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Engineering Mathematics 3 -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['APPLIED MATHEMATICS -III UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['APPLIED MATHEMATICS -III UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['APPLIED MATHEMATICS -III AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['APPLIED MATHEMATICS -III  S3']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Electronic Decives and Circuits - I -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS S3']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Digital Circuit Design -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['DIGITAL CIRCUIT DESIGN UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['DIGITAL CIRCUIT DESIGN UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['DIGITAL CIRCUIT DESIGN AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['DIGITAL CIRCUIT DESIGN S3']}</b>", True)

        with marksRight :
            st.markdown("<h6> Electrical Network Analysis and Synthesis -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ELECTRICAL NETWORK ANALYSIS AND SYNTHESIS  S3']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Electronics Instruments and Measurements -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ELECTRONICS INSTRUMENTS AND MEASUREMENTS UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ELECTRONICS INSTRUMENTS AND MEASUREMENTS UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ELECTRONICS INSTRUMENTS AND MEASUREMENTS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ELECTRONICS INSTRUMENTS AND MEASUREMENTS S3']}</b>", True)
    
    if semSelection == "Semester 4" and deptSelection == "ETRX":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Engineering Mathematics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['APPLIED MATHEMATICS - IV UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['APPLIED MATHEMATICS - IV UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['APPLIED MATHEMATICS - IV AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['APPLIED MATHEMATICS - IV S4']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Electronic Devices and Circuits - II -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS II UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS II UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS II AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS II S4']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Microprocessors and applications -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['MICROPROCESSORS AND APPLICATIONS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['MICROPROCESSORS AND APPLICATIONS UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['MICROPROCESSORS AND APPLICATIONS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['MICROPROCESSORS AND APPLICATIONS  S4']}</b>", True)

        with marksRight :
            st.markdown("<h6> Digital System Design -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['DIGITAL SYSTEM DESIGN UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['DIGITAL SYSTEM DESIGN  UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['DIGITAL SYSTEM DESIGN  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['DIGITAL SYSTEM DESIGN S4']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Principles of Communication Engineering -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['PRINCIPLES OF COMMUNICATION ENGINEERING UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['PRINCIPLES OF COMMUNICATION ENGINEERING UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['PRINCIPLES OF COMMUNICATION ENGINEERING AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['PRINCIPLES OF COMMUNICATION ENGINEERING S4']}</b>", True)

            st.markdown("<br>", True)
            
            st.markdown("<h6> Linear Control Systems -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['LINEAR CONTROL SYSTEMS UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['LINEAR CONTROL SYSTEMS  UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['LINEAR CONTROL SYSTEMS  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['LINEAR CONTROL SYSTEMS  S4']}</b>", True)

    if semSelection == "Semester 3" and deptSelection == "EXTC":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Applied Mathematics III -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['APPLIED MATHEMATICS-III UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['APPLIED MATHEMATICS-III UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['APPLIED MATHEMATICS-III  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['APPLIED MATHEMATICS-III S3']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Digital Logic Design -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['DIGITAL LOGIC DESIGN UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['DIGITAL LOGIC DESIGN UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['DIGITAL LOGIC DESIGN AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['DIGITAL LOGIC DESIGN S3']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Electronic Devices and circuits -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ELECTRONIC DEVICES AND CIRCUITS S3']}</b>", True)

        with marksRight :
            st.markdown("<h6> Electrical Networks  -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ELECTRICAL NETWORKS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ELECTRICAL NETWORKS UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ELECTRICAL NETWORKS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ELECTRICAL NETWORKS S3']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Electronics Instrumentation -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ELECTRONIC INSTRUMENTATION UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ELECTRONIC INSTRUMENTATION  UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ELECTRONIC INSTRUMENTATION  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ELECTRONIC INSTRUMENTATION S3']}</b>", True)
    
    if semSelection == "Semester 4" and deptSelection == "EXTC":
        marksLeft, marksRight = st.columns(2)

        with marksLeft :
            st.markdown("<h6> Applied Mathematics Mathematics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['APPLIED MATHEMATICS 4 UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['APPLIED MATHEMATICS 4 UT2 ']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['APPLIED MATHEMATICS 4 AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['APPLIED MATHEMATICS 4 S4']}</b>", True)

            st.markdown("<br>", True)

            st.markdown("<h6> Analog Electronics -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['ANALOG ELECTRONICS -II UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['ANALOG ELECTRONICS -II  UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['ANALOG ELECTRONICS -II  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['ANALOG ELECTRONICS -II  S4']}</b>", True)
            
            st.markdown("<br>", True)

            st.markdown("<h6> Wave theory and Propagation -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['WAVE THEORY AND PROPAGATION UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['WAVE THEORY AND PROPAGATION  UT2']}</b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['WAVE THEORY AND PROPAGATION  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['WAVE THEORY AND PROPAGATION  S4']}</b>", True)

        with marksRight :
            st.markdown("<h6> Microprocessors and Peripherals -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['MICROPROCESSORS AND PERIPHERALS UT1']}</b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['MICROPROCESSORS AND PERIPHERALS UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['MICROPROCESSORS AND PERIPHERALS AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['MICROPROCESSORS AND PERIPHERALS S4']}</b>", True)
            
            st.markdown("<br>", True)
            
            st.markdown("<h6> Signals and Systems -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['SIGNALS AND SYSTEMS UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['SIGNALS AND SYSTEMS UT2']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['SIGNALS AND SYSTEMS  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['SIGNALS AND SYSTEMS S4']}</b>", True)

            st.markdown("<br>", True)
            
            st.markdown("<h6> Control Systems -  </h6>", True)
            st.markdown(f"Internal Assesment 1 - <b>{df4.iloc[0]['CONTROL SYSTEMS UT1']}<b>", True)
            st.markdown(f"Internal Assesment 2 - <b>{df4.iloc[0]['CONTROL SYSTEMS  UT2 ']}<b>", True)
            st.markdown(f"Average marks obtained - <b>{df4.iloc[0]['CONTROL SYSTEMS  AVG']}</b>", True)
            st.markdown(f"Marks obtained in Semester exam - <b>{df4.iloc[0]['CONTROL SYSTEMS   S4']}</b>", True)


st.markdown("---")


# hiding some default items given by streamlit
# hide_styles = """
# <style>
# MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}
# </style>
# """

# st.markdown(hide_styles, unsafe_allow_html = True)

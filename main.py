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
        options=["Semester 1", "Semester 2", "Semester 3", "Semester 4",
                 "Semester 5", "Semester 6", "Semester 7", "Semester 8"]
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
             "ROLL NO.", "NAME", "Overall CGPA"]])

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
                 "Electrical Networks (Unit Tests)", "Electronic Instrumentation (Unit Tests)", "Presentation and Communication Technology (Unit Tests)"]
    )

if deptSelection == "EXTC" and semSelection == "Semester 4":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Applied Mathematics-IV (Unit Tests)", "Electronics and circuit Devices -II (Unit Tests)", "Electromagnetic Wave Theory (Unit Tests)",
                 "Microprocessor and Microcontroller (Unit Tests)", "Signal And Systems (Unit Tests)", "Principle Of Control Systems (Unit Tests)"]
    )

if deptSelection == "ETRX" and semSelection == "Semester 3":
    examSelection = st.selectbox(
        label="Select the type of examination and subject - ",
        options=["Applied Mathematics-III (Unit Tests)", "Electronic Devices and Circuits I (Unit Tests)", "Digital Circuit Design (Unit Tests)",
                 "Electrical Network Analysis nd Synthesis (Unit Tests)", "Electronic Instruments And Measurements (Unit Tests)"]
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
                 "Feedback Control Systems (Unit Tests)", "Control System Components (Unit Tests)", "Virtual Instrumentation (Unit Tests)"]
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

            belowPassing = data[data["MATHS AVG"] < 7]
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

    if semSelection == "Semester 3":
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

            belowPassing = data[data["PRINCIPLES OF COMMUNICATION AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME", "PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT1",
                                         "PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT2", "PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS AVG"]]
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

            belowPassing = data[data["PRINCIPLES OF COMMUNICATION AVG"] < 7]
            belowPassing = belowPassing[["DEPARTMENT", "CLASS AND SECTION", "ROLL NO.", "NAME", "PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT1",
                                         "PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS UT2", "PARADIGMS AND COMPUTER PROGRAMMING FUNDAMENTALS AVG"]]
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
st.dataframe(data1)


st.markdown("---")



# individual report card

st.markdown(
    f"<h5>Search for a particular student's detail in {deptSelection} department - </h5>", True)
studentSelection = st.selectbox(
    label="Select Student",
    options=dataSelection["NAME"].unique(),
)

df4 = dataSelection[dataSelection["NAME"] == studentSelection]
st.markdown("<br>", True)

st.markdown("<br>", True)

leftSide, rightSide = st.columns(2)

with leftSide:
    st.markdown(f"<h6>Name - {df4.iloc[0]['NAME']}</h6>", True)
    st.markdown(f"<h6>Batch - {df4.iloc[0]['BATCH']}</h6>", True)
    st.markdown(f"<h6>Department - {df4.iloc[0]['DEPARTMENT']}</h6>", True)
      

with rightSide:
    st.markdown(
        f"<h6>Division - {df4.iloc[0]['CLASS AND SECTION']}</h6>", True)
    st.markdown(f"<h6>Roll number - {df4.iloc[0]['ROLL NO.']}</h6>", True)



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

import streamlit as st
import pickle
from PIL import Image

def main():
    def set_background_image(image_url):
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("{image_url}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True)
    set_background_image('https://i.pinimg.com/736x/63/82/69/638269a8da27db2d89a7f2a39bb31fd0.jpg')


    st.markdown(
        """
        <style>
        /* Set all text to black */
        * {
            color: #783823 !important;
        }
        /* Set dropdown text to white */
        [data-baseweb="select"] .css-1wa3eu0 {
        color: white !important;
        }

        /* Set dropdown options text to their default color */
        [data-baseweb="select"] {
            color: #333 !important;
            
        }

        /* Set the predict button text to its default color */
        button {
            color: white !important;
            background-color: #ad9884 !important; /* Blue button */
        }
        </style>
        """,
        unsafe_allow_html=True
    )








    #page title and header image:
    try:
        st.title(":bar_chart: **ONLINE SHOPPING PURCHASE PREDICTION**")
        # img = Image.open("online_shopping_image.jpg")
        # st.image(img, width=500)
    except FileNotFoundError:
        st.warning("Image file 'Online_shopping_image.jpg' not found. Please ensure the file exists in the correct path.")

    st.sidebar.title("Select Page:")
    page = st.sidebar.radio("Go to", ["Home", "About", "Prediction" , "Contact"])

    st.markdown("""
            <style>
            div[data-baseweb="select"] {
        background-color: #000033;

        border-radius: 2px;
        padding: 2px;
    }

             # @keyframes zoomEffect {
             #        0% { background-size: 150%; }
             #        100% { background-size: 140%; }
             #    }
                [data-testid="stSidebar"] {
                    background: url("https://i.pinimg.com/736x/63/82/69/638269a8da27db2d89a7f2a39bb31fd0.jpg") no-repeat center center;
                    background-size: cover;
                    margin-top: 58px;
                    animation: zoomEffect 0.45s infinite alternate;
                }
               </style>
        """, unsafe_allow_html=True)



    if page == "Home":

        st.title("Welcome to the **Online Shopping Purchase Prediction**.")
        st.write(" This tool is designed to help higher management and top level executives predict whether Customers are likely to purchase a product from their shopping platform")
        st.write("Based on various personal and professional factors, The prediction uses a trained machine learning model to accurately predict customer intention.")
        st.header("**How it works:**")
        st.write("- Input relevant details.")
        st.write("- Click on the `Predict` button to view the result.")
        st.write("- Use the insights to make informed decisions regarding Business Growth.")
        st.markdown(
            "### 🔗 Resources\n"
            "You can access the Colab notebook for this project using the following link:\n\n"
            "[Open Colab Notebook]https://colab.research.google.com/drive/1i5zlH-HAXBK1ehU6neAQSu978tlP6Lto?usp=sharing")

    elif page == "About":
        st.title("📄 About This Project:")

        # Dataset Description
        st.header("📊 Online Shoppers Intention Dataset")
        st.write("""
        The **Online Shoppers Intention Dataset** is designed to predict whether a user will make a purchase on an e-commerce website. 
        It consists of **10,000+ records** and features extracted from website session logs, including user behavior, browsing history, and engagement metrics.
        """)


        st.header("Key Features")
        st.markdown("""
        - **User Behavior:** Page visits, session duration, bounce rates, exit rates.
        - **Engagement Metrics:** Special day effects, page values, product-related interactions.
        - **Technical Aspects:** Operating system, browser, region, and traffic type.
        - **Target Variable:** `Revenue` (0 = No Purchase, 1 = Purchase).
        """)


        st.header("📈 Business Impact")
        st.write("""
        - Helps e-commerce businesses **optimize their website experience** to improve conversion rates.
        - Enables targeted marketing based on **visitor behavior patterns**.""")


        st.header(" Methodology")
        st.write("""
        We applied various **machine learning models**, including:
        - **K-Nearest Neighbors (KNN)**
        - **Support Vector Machine (SVM)**
        - **Decision Tree (DT)**
        - **Random Forest (RF)**
        - **AdaBoost**
        - **XGBoost**""")

    elif page == "Prediction":
        st.title("Prediction")

        with st.expander("Administrative and Information Details"):

            administrative = st.slider(
                "Number of Administrative Pages Viewed",
                min_value=0,
                max_value=27,
                value=1,
                step=1
            )

            administrative_duration = st.slider(
                "Administrative Duration (in seconds)",
                 min_value=0.0,
                 max_value=3500.0,
                 value=0.0,
                 step=10.1)

            informational = st.slider(
                 "Number of Informational Pages Viewed",
                  min_value=0,
                  max_value=24,
                  value=1,
                  step=1
            )

            informational_duration = st.slider(
                 "Informational Duration (in seconds)",
                  min_value=0.0,
                  max_value=2600.0,
                  value=0.0,
                  step=10.1
            )

        with ((st.expander("Product Related Page Details"))):

            product_related_duration = st.slider(
                "Product Related Duration (in seconds)",
                 min_value=0.0,
                 max_value=64000.0,
                 value=0.0,
                 step=100.1
            )

            ProductRelated=st.text_input("Enter number of product-related pages viewed:",value=1)
            try:
                ProductRelated = int(ProductRelated)
                if ProductRelated<0 or ProductRelated>705:
                    st.error("Product Related Pages must be between 0 and 705")
            except ValueError:
                   st.error("Please enter a valid integer for Product Related Pages")

            BounceRates = st.text_input("Bounce Rates(visitors who leave the website after viewing only one page)", value="0.0")


            try:
                BounceRates = float(BounceRates)
                if BounceRates<0.0 or BounceRates>0.2:
                    st.error("Bounce Rates must be between 0.0 and 0.2")
            except ValueError:
                st.error("Please enter a valid number for Bounce Rates")

            ExitRates = st.text_input("Exit Rates(visitors who leave the website after a specific page)", value="0.0")


            try:
                ExitRates = float(ExitRates)
                if ExitRates<0.0 or ExitRates>0.2:
                    st.error("Exit Rates must be between 0.0 and 0.2")
            except ValueError:
                st.error("Please enter a valid number for Exit Rates")

            PageValues = st.text_input("Page Values", value="0.0")


            try:
                PageValues = float(PageValues)
                if PageValues<0.0 or PageValues>361.76:
                    st.error("Page Values must be between 0.0 and 361.76")
            except ValueError:
                st.error("Please enter a valid number for Page Values")

        # (Normal Day vs. Special Day)
        special_day_binary = st.radio(
            "Is it a Special Day?",
            options=["No", "Yes"],
            key="special_day",
            index=0
        )


        special_day_code = 1 if special_day_binary == "Yes" else 0

        # Mapping
        os_mapping = {
            "Windows": 2,
            "macOS": 1,
            "Linux": 3,
            "Other": 4  # Assign "Other" to code 4
        }


        selected_os = st.selectbox(
            "Operating System",
            options=["Windows", "macOS", "Linux", "Other"],
            index=0
        )

        # Convert selection to original code
        os_code = os_mapping[selected_os]

        #  mapping
        browser_mapping = {
            "Chrome": 2,
            "Firefox": 1,
            "Safari": 3,
            "Edge": 4,
            "Opera": 5,
            "Brave": 6,
            "Other (Less Common)": 7,  # Merging less common browsers (7-13)
        }


        selected_browser = st.selectbox(
            "Select Browser",
            options=list(browser_mapping.keys()),
            index=0
        )

        # Convert selection to dataset's numerical code
        browser_code = browser_mapping[selected_browser]

        region_mapping = {
            "North America": 1,
            "Europe": 3,
            "Asia": 4,
            "South America": 2,
            "Australia": 6,
            "Africa": 7,
            "Middle East": 9,
            "Central America": 8,
            "Other": 5
        }


        selected_region = st.selectbox(
            "Select Region",
            options=list(region_mapping.keys()),
            index=0
        )

        # Convert selection to dataset's numerical code
        region_code = region_mapping[selected_region]


        traffic_mapping = {
            "Direct Traffic": 1,
            "Organic Search": 2,
            "Referral": 3,
            "Paid Search": 4,
            "Social Media": 5,
            "Email Campaign": 6,
            "Display Ads": 7,
            "Affiliate Marketing": 8,
            "Other": 9,
            "Other Type 10": 10,
            "Other Type 11": 11,
            "Other Type 12": 12,
            "Other Type 13": 13,
            "Other Type 14": 14,
            "Other Type 15": 15,
            "Other Type 16": 16,
            "Other Type 17": 17,
            "Other Type 18": 18,
            "Other Type 19": 19,
            "Other Type 20": 20
        }


        selected_traffic = st.selectbox(
            "Select Traffic Type",
            options=list(traffic_mapping.keys()),
            index=1
        )

        # Convert selection to dataset's numerical code
        traffic_code = traffic_mapping[selected_traffic]

        Weekend = st.radio(
            "Visit Day",
            options=["Weekday", "Weekend"],
            key="weekend",
            index=0,
        )
        if Weekend=="Weekend":
            w=1
        elif Weekend=="Weekday":
            w=0

        # Mapping between full month names and dataset column names
        month_mapping = {
            "January": None,  # Not in dataset
            "February": "Month_Feb",
            "March": "Month_Mar",
            "April": None,  # Not in dataset
            "May": "Month_May",
            "June": "Month_Jun",
            "July": "Month_Jul",
            "August": "Month_Aug",
            "September": "Month_Sep",
            "October": "Month_Oct",
            "November": "Month_Nov",
            "December": "Month_Dec"
        }

        month_features = {
            "Month_Aug": 0.0, "Month_Dec": 0.0, "Month_Feb": 0.0,
            "Month_Jul": 0.0, "Month_Jun": 0.0, "Month_Mar": 0.0,
            "Month_May": 0.0, "Month_Nov": 0.0, "Month_Oct": 0.0,
            "Month_Sep": 0.0
        }


        selected_month = st.selectbox(
            "Select Month",
            options=list(month_mapping.keys()),
            index=0
        )


        if selected_month not in ["January", "April"]:
            month_column = month_mapping[selected_month]
            if month_column:
                month_features[month_column] = 1.0

        visitor_type_features = {
            "VisitorType_New_Visitor": 0.0,
            "VisitorType_Other": 0.0,
            "VisitorType_Returning_Visitor": 0.0
        }


        visitor_type = st.radio(
            "Visitor Type",
            options=["New Visitor", "Returning Visitor", "Other"],
            key="visitor_type",
            index=1
        )

        if visitor_type == "New Visitor":
            visitor_type_features["VisitorType_New_Visitor"] = 1
        elif visitor_type == "Returning Visitor":
            visitor_type_features["VisitorType_Returning_Visitor"] = 1
        elif visitor_type == "Other":
            visitor_type_features["VisitorType_Other"] = 1


        features=[administrative,administrative_duration,informational,informational_duration,ProductRelated,product_related_duration,BounceRates,ExitRates,PageValues,special_day_code,os_code,browser_code,region_code,traffic_code,w,]+ list(month_features.values()) + [
                  visitor_type_features["VisitorType_New_Visitor"],visitor_type_features["VisitorType_Returning_Visitor"],visitor_type_features["VisitorType_Other"]]
        scaler=pickle.load(open('xb_scaler.sav','rb'))
        model=pickle.load(open('xb_model.sav','rb'))
        pred=st.button("PREDICT")

        if pred:
            result=model.predict(scaler.transform([features]))
            if result==0:
                st.write("NO PURCHASE BY CUSTOMER")
            else:
                st.write("CUSTOMER HAS PURCHASED A PRODUCT")


    elif page == "Contact":
        st.title("📞 Contact Page")
        st.write("For Inquiries, you can reach me at:")
        st.write("📧 Email: shahabasali751@gmail.com")


main()

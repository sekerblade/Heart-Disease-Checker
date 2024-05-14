import streamlit as st
import pandas as pd
import time
import pickle
import pandas as pd

col1, col2, col3 = st.columns([1,2,3])

col1.page_link("main.py", label="หน้าหลัก", icon="🏠")
col2.page_link("pages/about-heart-disease.py", label="ข้อมูลเกี่ยวกับโรคหัวใจ", icon="1️⃣")
col3.page_link("pages/information.py", label="ติดต่อผู้เชี่ยวชาญ", icon="2️⃣", disabled=False)

st.write("-----------------------------")
st.title('ระบบทำนายโรคหัวใจ')
    #progress_bar = st.progress(0)
st.subheader('คุณกำลังสงสัยเกี่ยวกับสุขภาพหัวใจของคุณอยู่หรือเปล่า? ')
st.subheader('เราจะช่วยคุณลองวินิจฉัยดู !')

st.write('หากต้องการทำนายสถานะโรคหัวใจของคุณ เพียงทำตามขั้นตอนต่อไปนี้ได้เลย:')
st.write('1. กรอกฟอร์มทางด้านซ้ายให้ครบถ้วน')
st.write('2. กดที่ปุ่ม "ทำนาย" แล้วรอผลประเมินได้เลย')

st.write('ขอย้ำว่า ผลการประเมินที่ได้รับจากโปรแกรมนี้ไม่สามารถใช้แทนการตัดสินใจของแพทย์ได้ การตรวจรักษาเพิ่มเติมขึ้นอยู่กับดุลยพินิจและการปรึกษากันระหว่างแพทย์กับตัวท่าน')
#st.write('ผลการประเมินนี้ห้ามนำไปใช้อ้างอิงในการค้า เช่น การทำประกันชีวิต และไม่สามารถใช้กับผู้ป่วยโรคลิ้นหัวใจหรือโรคหัวใจเต้นผิดจังหวะได้')

    #tab1, tab2 = st.tabs(["🗃 User Input", "📈 Chart"])

    #$tab1.write('User Parameters')


    #function Input Parameters from User

def bins_bmi_calculate():
        weight = st.sidebar.number_input("กำหนดน้ำหนักของคุณ (กิโลกรัม)", placeholder="", min_value=0, max_value=200)
        height = st.sidebar.number_input('กำหนดส่วนสูงของคุณ (เมตร)',min_value=0.0,max_value=2.5,value=1.5)
        bmi = (weight /( height * height));
        #print(bmi)
        label = ''
        if bmi < 18.5 :  label = '3'
        elif (bmi >= 18.5) & (bmi <= 22.90) : label = '0'
        elif (bmi >= 22.91) & (bmi <= 24.90) : label = '1'
        elif (bmi >= 24.91) & (bmi <= 29.90) : label = '2'
        elif bmi >= 29.91 :  label = '4'
        return label

def bins_sleepTime_calculate():
        sleeping = st.sidebar.number_input("ชั่วโมงการนอนเฉลื่ยของคุณคือ (ชั่วโมง)", placeholder="", min_value=1, max_value=24,value=8)
        #print(sleeping)
        labels = ''
        if sleeping > 10 : labels = '2'
        elif (sleeping >= 7) & (sleeping <= 10) : labels = '0'
        elif sleeping < 7 : labels = '1'
        return labels

def bins_ageCategory_calculate():
        ac = st.sidebar.selectbox('กำหนดช่วงอายุ (ปี)',('18 - 24','25 - 29','30 - 34','35 - 39','40 - 44','45 - 49','50 - 54','55 - 59','60 - 64','65 - 69','70 - 74','75 - 79','80 ขึ้นไป',))
        labelss = ''
        if ac == '18 - 24': labelss = '0'
        elif ac == '25 - 29': labelss = '1'
        elif ac == '30 - 34': labelss = '2'
        elif ac == '35 - 39': labelss = '3'
        elif ac == '40 - 44': labelss = '4'
        elif ac == '45 - 49': labelss = '5'
        elif ac == '50 - 54': labelss = '6'
        elif ac == '55 - 59': labelss = '7'
        elif ac == '60 - 64': labelss = '8'
        elif ac == '65 - 69': labelss = '9'
        elif ac == '70 - 74': labelss = '10'
        elif ac == '75 - 79': labelss = '11'
        elif ac == '80 ขึ้นไป': labelss = '12'
        return labelss

def bins_genHealth_calculate():
        gh = st.sidebar.selectbox('สุขภาพโดยทั่วไปของคุณเป็นอย่างไร?',('แย่','ปกติ','ดี','ดีมาก','ดีเยี่ยม'))
        param = ''
        if gh == 'แย่': param = '0'
        elif gh == 'ปกติ': param = '1'
        elif gh == 'ดี': param = '2'
        elif gh == 'ดีเยี่ยม': param = '3'
        elif gh == 'ดีมาก': param = '4'
        return param

def user_input_feature():
        st.sidebar.image("images/heart-fav.png", width=100)
        #st.sidebar.title('หน้าต่างนำทาง')
        st.sidebar.title('ฟอร์มกรอกข้อมูล')
        bmi_bins = bins_bmi_calculate()
        ##Bmi = st.sidebar.slider('กำหนดค่าดัชนีมวลกายของคุณ',0.0, 50.0, 25.0)
        Smoking = st.sidebar.selectbox('คุณเคยสูบบุหรี่อย่างน้อย 100 มวนตลอดชีวิต (ประมาณ 5 ซอง) หรือไม่?',('ไม่','ใช่',))
        AlcoholDrinking = st.sidebar.selectbox('คุณดื่มแอลกอฮอล์มากกว่า 14 แก้ว(ผู้ชาย) หรือมากกว่า 7 แก้ว(ผู้หญิง) ในหนึ่งสัปดาห์หรือไม่?',('ไม่','ใช่',))
        Stroke = st.sidebar.selectbox('เป็นโรคหลอดเลือดสมองหรือไม่?',('ไม่','ใช่',))
        PhysicalHealth = st.sidebar.number_input('ในช่วง 30 วันที่ผ่านมา มีกี่วันที่สุขภาพกายของคุณไม่ค่อยดี? (วัน)',max_value=30,min_value=0)
        MentalHealth = st.sidebar.number_input('ในช่วง 30 วันที่ผ่านมา มีกี่วันที่สุขภาพจิตของคุณไม่ค่อยดี? (วัน)',max_value=30,min_value=0)
        DiffWalking = st.sidebar.selectbox('มีปัญหาในการเดินหรือขึ้นบันไดหรือไม่?',('ไม่','ใช่',))
        Sex = st.sidebar.selectbox('กำหนดเพศ',('ชาย','หญิง',))
        AgeCategory = bins_ageCategory_calculate()
        Race = st.sidebar.selectbox('กำหนดเชื้อชาติ',('ชาติพันธ์ุผิวขาว','ชาติพันธ์ุผิวดำ','ชาติพันธ์ุเอเชีย','ชนพื้นเมืองอเมริกัน','ชาติพันธ์ุวัฒนธรรมสเปน','อื่นๆ'))
        Diabetic = st.sidebar.selectbox('เป็นโรคเบาหวานหรือไม่?',('ไม่','ใช่',))
        PhysicalActivity = st.sidebar.selectbox('คุณเป็นคนที่ออกกำลังกายเป็นประจำหรือไม่?',('ไม่','ใช่',))
        GenHealth = bins_genHealth_calculate()
        SleepTime = bins_sleepTime_calculate()
        Asthma = st.sidebar.selectbox('เป็นโรคหอบหืดหรือไม่?',('ไม่','ใช่',))
        KidneyDisease = st.sidebar.selectbox('เป็นโรคไตหรือไม่?',('ไม่','ใช่',))
        SkinCancer = st.sidebar.selectbox('เป็นโรคมะเร็งผิวหนังหรือไม่?',('ไม่','ใช่',))
        data = {
                ##'Bmi' : Bmi,
                'Bmi' : bmi_bins,
                'Smoking' :  Smoking,
                'AlcoholDrinking' : AlcoholDrinking,
                'Stroke' : Stroke,
                'PhysicalHealth' : PhysicalHealth,
                'MentalHealth' : MentalHealth,
                'DiffWalking' : DiffWalking,
                'Sex' : Sex,
                'AgeCategory' : AgeCategory,
                'Race' : Race,
                'Diabetic' : Diabetic,
                'PhysicalActivity' : PhysicalActivity,
                'GenHealth' : GenHealth,
                'SleepTime' : SleepTime,
                'Asthma' : Asthma,
                'KidneyDisease' : KidneyDisease,
                'SkinCancer' : SkinCancer}
        features = pd.DataFrame(data, index=[0])
        return features

df = user_input_feature();
    #tab1.dataframe(df)

    #function translate user input parameters
def translate_user_input():
        translations = {'ไม่': 'No', 'ใช่': 'Yes','ชาย':'Male','หญิง': 'Female'}
        transRace = {'ชาติพันธ์ุผิวขาว':'White','ชาติพันธ์ุผิวดำ':'Black','ชาติพันธ์ุเอเชีย':'Asian','ชนพื้นเมืองอเมริกัน':'American Indian/Alaskan Native','ชาติพันธ์ุวัฒนธรรมสเปน':'Hispanic','อื่นๆ':'Other'}
        translateData ={
                        'Smoking' : df['Smoking'].map(translations),
                        'AlcoholDrinking' : df['AlcoholDrinking'].map(translations),
                        'Stroke' : df['Stroke'].map(translations),
                        'PhysicalHealth' : df['PhysicalHealth'],
                        'MentalHealth' : df['MentalHealth'],
                        'DiffWalking' : df['DiffWalking'].map(translations),
                        'Sex' : df['Sex'].map(translations),
                        'AgeCategory' : df['AgeCategory'],
                        'Race' : df['Race'].map(transRace),
                        'Diabetic' : df['Diabetic'].map(translations),
                        'PhysicalActivity' : df['PhysicalActivity'].map(translations),
                        'GenHealth' : df['GenHealth'],                 
                        'Asthma' : df['Asthma'].map(translations),
                        'KidneyDisease' : df['KidneyDisease'].map(translations),
                        'SkinCancer' : df['SkinCancer'].map(translations),
                        'BMICategory' : df['Bmi'],
                        'SleepTimeCategory' : df['SleepTime'],
        }
        new_df = pd.DataFrame(translateData, index=[0])
        return new_df

trans_df = translate_user_input()
    #tab1.write('Translated User Input Parameters'),
    #tab1.dataframe(trans_df)
df_preprocessed = trans_df

columns_to_encode = ['BMICategory', 'SleepTimeCategory', 'AgeCategory', 'GenHealth']

for column in columns_to_encode:
        df_preprocessed[column] = df_preprocessed[column].astype(float)


if 'clicked' not in st.session_state:
        st.session_state.clicked = False

def click_button():
        st.session_state.clicked = True
        run_progress_bar()

def run_progress_bar():
        #progress_text = "ระบบกำลังดำเนินการคำนวณผลลัพธ์"
        #for perc_completed in range(100):
        #    time.sleep(0.03)
        #    progress_bar.progress(perc_completed+1, text=progress_text)

        with st.spinner('กำลังประมวลผลลัพธ์...'):
            time.sleep(2.5)
        
def check_NO():
        
        Smok = [0,0]
        Alc  = [0,0]
        Str  = [0,0]
        Dif  = [0,0]
        sex  = [0,0]
        Phy  = [0,0]
        Ast  = [0,0]
        Kid  = [0,0]
        Ski  = [0,0]
        race = [0,0,0,0,0,0]
        Dia  = [0,0]

        if df_preprocessed['Smoking'][0] == 'No': Smok[0] = 1
        else : Smok[1] = 1
        if df_preprocessed['AlcoholDrinking'][0] == 'No': Alc[0] = 1 
        else : Alc[1] = 1 
        if df_preprocessed['Stroke'][0] == 'No': Str[0] = 1 
        else : Str[1] = 1 
        if df_preprocessed['DiffWalking'][0] == 'No': Dif[0] = 1 
        else : Dif[1] = 1 
        if df_preprocessed['Sex'][0] == 'No': sex[0] = 1 
        else : sex[1] = 1 
        if df_preprocessed['PhysicalActivity'][0] == 'No': Phy[0] = 1 
        else : Phy[1] = 1 
        if df_preprocessed['Asthma'][0] == 'No': Ast[0] = 1 
        else : Ast[1] = 1 
        if df_preprocessed['KidneyDisease'][0] == 'No': Kid[0] = 1 
        else : Kid[1] = 1 
        if df_preprocessed['SkinCancer'][0] == 'No': Ski[0] = 1 
        else : Ski[1] = 1 
        if df_preprocessed['Diabetic'][0] == 'No': Dia[0] = 1 
        else : Dia[1] = 1 

        if df_preprocessed['Race'][0] == 'Race_American Indian/Alaskan Native': race[0] = 1 
        elif df_preprocessed['Race'][0] == 'Asian': race[1] = 1
        elif df_preprocessed['Race'][0] == 'Black': race[2] = 1
        elif df_preprocessed['Race'][0] == 'Hispanic': race[3] = 1
        elif df_preprocessed['Race'][0] == 'Other': race[4] = 1
        elif df_preprocessed['Race'][0] == 'White': race[5] = 1

        user_input = {
        'Smoking_No': Smok[0],
        'Smoking_Yes': Smok[1],
        'AlcoholDrinking_No': Alc[0],
        'AlcoholDrinking_Yes': Alc[1],
        'Stroke_No': Str[0],
        'Stroke_Yes': Str[1],
        'DiffWalking_No': Dif[0],
        'DiffWalking_Yes': Dif[1],
        'Sex_Female': sex[0],
        'Sex_Male': sex[1],
        'Race_American Indian/Alaskan Native': race[0],
        'Race_Asian': race[1],
        'Race_Black': race[2],
        'Race_Hispanic': race[3],
        'Race_Other': race[4],
        'Race_White': race[5],
        'Diabetic_No': Dia[0],
        'Diabetic_No, borderline diabetes': 0,
        'Diabetic_Yes': Dia[1],
        'Diabetic_Yes (during pregnancy)': 0,
        'PhysicalActivity_No': Phy[0],
        'PhysicalActivity_Yes': Phy[1],
        'Asthma_No': Ast[0],
        'Asthma_Yes': Ast[1],
        'KidneyDisease_No': Kid[0],
        'KidneyDisease_Yes': Kid[1],
        'SkinCancer_No': Ski[0],
        'SkinCancer_Yes': Ski[1],
        'PhysicalHealth': df_preprocessed['PhysicalHealth'][0],
        'MentalHealth':df_preprocessed['MentalHealth'][0],
        'AgeCategory': df_preprocessed['AgeCategory'][0],  # For example, corresponding to 30-39 years
        'GenHealth': df_preprocessed['GenHealth'][0],
        'BMICategory': df_preprocessed['BMICategory'][0],  # For example, corresponding to 23-24.9
        'SleepTimeCategory': df_preprocessed['SleepTimeCategory'][0]  # For example, corresponding to 7-9 hours
    }
        final_df = pd.DataFrame(user_input, index=[0])
        for column in final_df.columns:
            final_df[column] = final_df[column].astype(float)

        return final_df
        
pre_prediction = check_NO()
    #tab1.dataframe(pre_prediction)
    #print(pre_prediction.dtypes)
    #print(pre_prediction.head())

LOG_MODEL_PATH = 'best_model_logistic.pkl'
#LOG_MODEL_PATH = 'logistic_regression_model.pkl'

with open(LOG_MODEL_PATH, 'rb') as f:
        logistic_regression_model = pickle.load(f)

predictions = logistic_regression_model.predict_proba(pre_prediction)[:, 1]

    #st.write(predictions)

final_result = (predictions*100)
final_result_asfloat = final_result[0].astype(float)

col1 , col2 = st.columns([1, 2],gap="large")

with col1:
    submit = st.button(label='ทำนาย', type="primary", on_click=click_button, help='กดปุ่มเพื่อทำนายผลลัพธ์')
    if submit:
        if final_result_asfloat < 50.0:
         st.markdown(
            f'<span style="color:green; font-size:24px;">ความน่าจะเป็นที่คุณจะเป็นโรคหัวใจคือ  {final_result_asfloat:.2f}  % คุณสุขภาพดี!</span>',
            unsafe_allow_html=True
         )
         st.image('images/good.jpg', width=350, caption='Dr. Heart Kub')
        else:
         st.markdown(
            f'<span style="color:red; font-size:24px;">ความน่าจะเป็นที่คุณจะเป็นโรคหัวใจคือ  {final_result_asfloat:.2f}  % สุขภาพของคุณมีความเสี่ยงต่อการเป็นโรคหัวใจ</span>',
            unsafe_allow_html=True
         )
         st.image('images/bad.jfif', width=350, caption='Dr. Heart Kub')
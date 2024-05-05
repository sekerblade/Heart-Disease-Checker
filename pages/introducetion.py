import streamlit as st

from main import user_input_feature

col1, col2, col3 = st.columns([1,2,3])

col1.page_link("main.py", label="หน้าหลัก", icon="🏠")
col2.page_link("pages/about.py", label="ข้อมูลเกี่ยวกับโรคหัวใจ", icon="1️⃣")
col3.page_link("pages/introducetion.py", label="ติดต่อผู้เชี่ยวชาญ", icon="2️⃣", disabled=False)
 
st.title("ข้อมูลที่ติดต่อของศูนย์โรคหัวใจ")

st.subheader("สายด่วนโรคหัวใจ โทร. 1668 ")
st.markdown("""
  **ชื่อฝ่าย/ศูนย์**

 สถาบันทรวงอก 
 
 
 **ที่อยู่** 74 ถ.ติวานนท์ ต.บางกระสอ อ.เมือง นนทบุรี 11000

- เบอร์โทรศัพท์หน่วยงาน   02-547-0999
- เฟสบุ๊ค https://www.facebook.com/CentralChestInstituteOfThailand/?locale=th_TH

- เว็บไซต์หน่วยงาน     https://www.ccit.go.th/?fbclid=IwAR2TCzVFJ9jF77KJFnqvkFLkWuluwxiGGyIZYXNRQHmNcQPL2wTrpqgXylQ
        """)
st.image("images/central-chest.jpeg" ,caption="สถาบันทรวงอก")


st.markdown("""
  **ชื่อฝ่าย/ศูนย์**

 ศูนย์หัวใจสิริกิติ์ภาคตะวันออกเฉียงเหนือ
 
 
**ที่อยู่** 123 ถนนมิตรภาพ หมู่ 16 ตำบลในเมือง อำเภอเมือง จังหวัดขอนแก่น 40002

- เบอร์โทรศัพท์หน่วยงาน   0 4323 2700

- เว็บไซต์หน่วยงาน     https://heart.kku.ac.th/index.php?option=com_content&view=article&id=145&Itemid=1211
        """)
st.image("images/sirikit-heart.jpeg" ,caption="ศูนย์หัวใจสิริกิติ์ภาคตะวันออกเฉียงเหนือ")
st.markdown("""
  **ชื่อฝ่าย/ศูนย์**

ศูนย์โรคหัวใจ โรงพยาบาลจุฬาลงกรณ์ สภากาชาดไทย


**ที่อยู่** อาคารภูมิสิริมังคลานุสรณ์ ชั้น 4 โซน D

- เบอร์โทรศัพท์หน่วยงาน   02-256-4000 (ต่อ 80442-80445)

- เว็บไซต์หน่วยงาน     https://chulalongkornhospital.go.th/cardiovascularmedicine/
        """)
st.image("images/chula-heart.jpeg" ,caption="ศูนย์โรคหัวใจ โรงพยาบาลจุฬาลงกรณ์ สภากาชาดไทย")
st.markdown("""
  **ชื่อฝ่าย/ศูนย์**

 ศูนย์โรคหัวใจ โรงพยาบาลบำรุงราษฐ์

- เบอร์โทรศัพท์หน่วยงาน   02-066-8888   (เวลา 20.00-08.00) 065-509-9198   (เวลา 08.00-20.00)
- แอดไลน์ @biheartcenter

- เว็บไซต์หน่วยงาน     https://www.bumrungrad.com/th/blog-news/line-heart-center
        """)
st.image("images/bumrad-heart.webp" ,caption="ศูนย์โรคหัวใจ  โรงพยาบาลบำรุงราษฐ์")

st.sidebar.image("images/heart-sidebar.png", width=100)
import streamlit as st

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide และกำหนด Title
st.set_page_config(
    page_title="Drink Recommendation Portal",
    page_icon="🧊",
    layout="wide",
)

# Custom CSS ตกแต่งธีมสีฟ้าคลีนๆ (Clean Blue Theme)
st.markdown(
    """
    <style>
    /* ตั้งค่าพื้นหลังหลักของเว็บให้เป็นสีขาวสะอาดตา */
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    /* สไตล์ของการ์ด (Card) */
    .card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: all 0.3s ease;
    }
    
    /* เอฟเฟกต์เมื่อเอาเมาส์ชี้การ์ด ขอบจะเปลี่ยนเป็นสีฟ้าสว่างขึ้น */
    .card:hover {
        border-color: #38bdf8;
        box-shadow: 0 10px 15px -3px rgba(56, 189, 248, 0.15);
        transform: translateY(-2px);
    }
    
    /* หัวข้อในการ์ด */
    .card-title {
        font-size: 1.15rem;
        font-weight: 600;
        margin-bottom: 8px;
        color: #0f172a;
    }
    
    /* คำอธิบายในการ์ด */
    .card-desc {
        font-size: 0.9rem;
        color: #64748b;
        margin-bottom: 24px;
        min-height: 40px;
    }
    
    /* ปุ่มกดลิงก์ (สีฟ้าพาสเทล/น้ำเงินเข้มคลีนๆ) */
    .custom-btn {
        display: block;
        width: 100%;
        background-color: #0284c7;
        color: white;
        text-align: center;
        padding: 10px 0;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    
    .custom-btn:hover {
        background-color: #0369a1;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# หัวข้อหน้าเว็บ
st.markdown(
    "<h2 style='text-align: center; margin-bottom: 40px; color: #0f172a;'>🧊 รวมงาน Recommendation</h2>",
    unsafe_allow_html=True,
)

# ข้อมูลการ์ดทั้ง 3 ช่อง
cards = [
    {
        "icon": "⚔️",
        "title": "Drink Recommender System ด้วย Graph",
        "desc": "วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการสั่ง Drink",
        "url": "https://colab.research.google.com/drive/1cFFUUkU0ceVjAmpGGb1tFRdwrc63MHnT?usp=sharing",
        "btn_text": "เปิดระบบ ➔",
    },
    {
        "icon": "📊",
        "title": "วิเคราะห์ความสัมพันธ์ Drink & User",
        "desc": "จัดการข้อมูล User และ Drink ด้วยฐานข้อมูลกราฟ Neo4j",
        "url": "https://colab.research.google.com/drive/15EkYZchP1E09enM5Qk4kIBcA8SpzxOiA?usp=sharing",
        "btn_text": "เปิดระบบ ➔",
    },
    {
        "icon": "🎯",
        "title": "ระบบแนะนำ Drink",
        "desc": "แนะนำ Drink จากความสัมพันธ์และ Drink ที่เพื่อนเคยสั่ง",
        "url": "https://drink-graph-recommendation-019-pvrsrplg8hnmtfupwhp8ss.streamlit.app/",
        "btn_text": "เปิดระบบ ➔",
    },
]

# แสดงผลการ์ดแบบ 3 คอลัมน์
cols = st.columns(3)
for i, col in enumerate(cols):
    with col:
        c = cards[i]
        st.markdown(
            f"""
            <div class="card">
                <div style="font-size: 1.5rem; margin-bottom: 12px;">{c['icon']}</div>
                <div class="card-title">{c['title']}</div>
                <div class="card-desc">{c['desc']}</div>
                <a href="{c['url']}" target="_blank" class="custom-btn">{c['btn_text']}</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
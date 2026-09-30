import streamlit as st

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide และกำหนด Title
st.set_page_config(
    page_title="Drink Recommendation Portal",
    page_icon="💬",
    layout="wide",
)

# Custom CSS เพื่อตกแต่งสีและหน้าตาให้ใกล้เคียงภาพต้นฉบับ
st.markdown(
    """
    <style>
    .stApp {
        background-color: #110f1c;
        color: #ffffff;
    }
    .card {
        background-color: #1e1a32;
        border: 1px solid #2d274c;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    .card:hover {
        border-color: #a855f7;
    }
    .card-title {
        font-size: 1.15rem;
        font-weight: 600;
        margin-bottom: 8px;
        color: #ffffff;
    }
    .card-desc {
        font-size: 0.9rem;
        color: #9ca3af;
        margin-bottom: 24px;
        min-height: 40px;
    }
    .custom-btn {
        display: block;
        width: 100%;
        background-color: #6b21a8;
        color: white;
        text-align: center;
        padding: 10px 0;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    .custom-btn:hover {
        background-color: #7e22ce;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# หัวข้อหน้าเว็บ
st.markdown(
    "<h2 style='text-align: center; margin-bottom: 40px;'>💬 รวมงาน Recommendation</h2>",
    unsafe_allow_html=True,
)

# ข้อมูลการ์ดต่างๆ (สามารถเปลี่ยนลิงก์ตรง url ได้เลย)
cards = [
    {
        "icon": "⚔️",
        "title": "โครงสร้างข้อมูล Drink & User",
        "desc": "วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการสั่ง Drink",
        "url": "https://colab.research.google.com/drive/1cFFUUkU0ceVjAmpGGb1tFRdwrc63MHnT?usp=sharing",
        "btn_text": "เปิดระบบ ➔",
    },
    {
        "icon": "📊",
        "title": "วิเคราะห์ความสัมพันธ์ Drink & User",
        "desc": "kจัดการข้อมูล User และ Drink ด้วยฐานข้อมูลกราฟ Neo4j",
        "url": "https://colab.research.google.com/drive/15EkYZchP1E09enM5Qk4kIBcA8SpzxOiA?usp=sharing",
        "btn_text": "เปิดระบบ ➔",
    },
    {
        "icon": "🎯",
        "title": "ระบบแนะนำ Drink",
        "desc": "แนะนำ Drink จากความสัมพันธ์และ Drink ที่เพื่อนเคยสั่ง",
        "url": "ใส่ลิงก์ของคุณตรงนี้_3",
        "btn_text": "เปิดระบบ ➔",
    },
]

# แถวบน (3 คอลัมน์)
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


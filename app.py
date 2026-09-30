import streamlit as st

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide และกำหนด Title
st.set_page_config(
    page_title="Anime Recommendation Portal",
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
    "<h2 style='text-align: center; margin-bottom: 40px;'>💬 รวมโปรเจกต์ระบบ Anime Recommendation ของเรา</h2>",
    unsafe_allow_html=True,
)

# ข้อมูลการ์ดต่างๆ (สามารถเปลี่ยนลิงก์ตรง url ได้เลย)
cards = [
    {
        "icon": "⚔️",
        "title": "โครงสร้างข้อมูล Anime & User",
        "desc": "จัดการข้อมูล User และ Anime ด้วยฐานข้อมูลกราฟ Neo4j",
        "url": "ใส่ลิงก์ของคุณตรงนี้_1",
        "btn_text": "เปิดระบบ ➔",
    },
    {
        "icon": "📊",
        "title": "วิเคราะห์ความสัมพันธ์ User",
        "desc": "วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการดู Anime",
        "url": "ใส่ลิงก์ของคุณตรงนี้_2",
        "btn_text": "เปิดระบบ ➔",
    },
    {
        "icon": "🎯",
        "title": "ระบบแนะนำ Anime",
        "desc": "แนะนำ Anime จากความสัมพันธ์และ Anime ที่เพื่อนเคยดู",
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

# แถวล่าง (การ์ด Neo4j Database แบบในภาพ)
col_bottom1, col_bottom2, col_bottom3 = st.columns(3)
with col_bottom1:
    st.markdown(
        """
        <div class="card">
            <div style="font-size: 1.5rem; margin-bottom: 12px;">🗄️</div>
            <div class="card-title">Neo4j Database</div>
            <div class="card-desc">ฐานข้อมูลกราฟที่จัดเก็บ User, Anime และความสัมพันธ์</div>
            <a href="ใส่ลิงก์ของคุณตรงนี้_4" target="_blank" class="custom-btn">เปิดเว็บไซต์ ➔</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
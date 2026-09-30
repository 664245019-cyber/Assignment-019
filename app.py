import streamlit as st

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide และกำหนด Title
st.set_page_config(
    page_title="Drink Recommendation Portal",
    page_icon="🧊",
    layout="wide",
)

# Custom CSS ตกแต่งดีไซน์ใหม่ให้พรีเมียมและสะอาดตา
st.markdown(
    """
    <style>
    /* ตั้งค่าพื้นหลังหลักของเว็บให้เป็นสีเทาอ่อนสะอาดตา */
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    /* สไตล์ของการ์ด (Card) ให้มีความนูนและโค้งมนสวยงาม */
    .card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 28px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
    }
    
    /* เอฟเฟกต์เมื่อเอาเมาส์ชี้การ์ด */
    .card:hover {
        border-color: #38bdf8;
        box-shadow: 0 20px 25px -5px rgba(56, 189, 248, 0.12), 0 8px 10px -6px rgba(56, 189, 248, 0.1);
        transform: translateY(-6px);
    }
    
    /* ป้ายหมวดหมู่จิ๋วบนการ์ด */
    .card-badge {
        display: inline-block;
        background-color: #e0f2fe;
        color: #0369a1;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 20px;
        margin-bottom: 12px;
        width: fit-content;
    }
    
    /* หัวข้อในการ์ด */
    .card-title {
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 10px;
        color: #0f172a;
        line-height: 1.4;
    }
    
    /* คำอธิบายในการ์ด */
    .card-desc {
        font-size: 0.9rem;
        color: #64748b;
        margin-bottom: 24px;
        line-height: 1.5;
        flex-grow: 1;
    }
    
    /* ปุ่มกดลิงก์แบบ Gradient สวยงาม */
    .custom-btn {
        display: block;
        width: 100%;
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: white !important;
        text-align: center;
        padding: 12px 0;
        border-radius: 14px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.95rem;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
        transition: all 0.2s ease;
    }
    
    .custom-btn:hover {
        background: linear-gradient(135deg, #0369a1 0%, #075985 100%);
        box-shadow: 0 6px 15px rgba(2, 132, 199, 0.35);
        transform: translateY(-1px);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# หัวข้อหน้าเว็บพร้อม Gradient Text
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px; margin-bottom: 40px;'>
        <h1 style='font-weight: 800; color: #0f172a; font-size: 2.5rem; margin-bottom: 10px;'>
            🧊 Drink Recommendation Portal
        </h1>
        <p style='color: #64748b; font-size: 1.1rem;'>
            ศูนย์รวมระบบแนะนำเครื่องดื่มอัจฉริยะด้วยเทคโนโลยี Graph Database และ Machine Learning
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ข้อมูลการ์ดทั้ง 3 ช่อง (เพิ่ม Badge แยกประเภทให้ดูโปรขึ้น)
cards = [
    {
        "icon": "⚔️",
        "badge": "Google Colab",
        "title": "Graph Analysis Model",
        "desc": "วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการสั่งเครื่องดื่มเชิงลึกด้วย Graph Algorithms",
        "url": "https://colab.research.google.com/drive/1cFFUUkU0ceVjAmpGGb1tFRdwrc63MHnT?usp=sharing",
        "btn_text": "เปิดใช้งานบน Colab ➔",
    },
    {
        "icon": "📊",
        "badge": "Neo4j Database",
        "title": "Neo4j Graph Recommender",
        "desc": "ระบบแนะนำเครื่องดื่มที่มีประสิทธิภาพสูงด้วยโครงสร้างฐานข้อมูลแบบกราฟ Neo4j",
        "url": "https://colab.research.google.com/drive/15EkYZchP1E09enM5Qk4kIBcA8SpzxOiA?usp=sharing",
        "btn_text": "เปิดใช้งานบน Colab ➔",
    },
    {
        "icon": "🎯",
        "badge": "Web Application",
        "title": "Streamlit Web Portal",
        "desc": "ใช้งานระบบแนะนำเครื่องดื่มผ่านหน้าเว็บอินเทอร์เฟซสำเร็จรูป สะดวกและรวดเร็ว",
        "url": "https://drink-graph-recommendation-019-pvrsrplg8hnmtfupwhp8ss.streamlit.app/",
        "btn_text": "เข้าสู่เว็บไซต์ ➔",
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
                <div>
                    <div style="font-size: 2rem; margin-bottom: 12px;">{c['icon']}</div>
                    <div class="card-badge">{c['badge']}</div>
                    <div class="card-title">{c['title']}</div>
                    <div class="card-desc">{c['desc']}</div>
                </div>
                <a href="{c['url']}" target="_blank" class="custom-btn">{c['btn_text']}</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Footer เล็กๆ ด้านล่าง
st.markdown(
    """
    <div style='text-align: center; color: #94a3b8; font-size: 0.85rem; margin-top: 50px; margin-bottom: 20px;'>
        Drink Recommendation Portal • Powered by Streamlit & Graph Technology
    </div>
    """,
    unsafe_allow_html=True,
)
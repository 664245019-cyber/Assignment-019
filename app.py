import streamlit as st

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide และกำหนด Title
st.set_page_config(
    page_title="Drink Recommendation Portal",
    page_icon="🧊",
    layout="wide",
)

# Custom CSS ตกแต่งดีไซน์ให้พรีเมียมและสะอาดตา
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
        padding: 24px;
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
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 10px;
        color: #0f172a;
        line-height: 1.4;
    }
    
    /* คำอธิบายในการ์ด */
    .card-desc {
        font-size: 0.85rem;
        color: #64748b;
        margin-bottom: 20px;
        line-height: 1.5;
        flex-grow: 1;
    }
    
    /* ปุ่มกดหลักแบบ Gradient */
    .custom-btn {
        display: block;
        width: 100%;
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: white !important;
        text-align: center;
        padding: 10px 0;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.85rem;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
        transition: all 0.2s ease;
        margin-bottom: 8px;
    }
    
    .custom-btn:hover {
        background: linear-gradient(135deg, #0369a1 0%, #075985 100%);
        box-shadow: 0 6px 15px rgba(2, 132, 199, 0.35);
        transform: translateY(-1px);
        color: white !important;
    }

    /* ปุ่มกด GitHub รอง */
    .github-btn {
        display: block;
        width: 100%;
        background-color: #f1f5f9;
        color: #334155 !important;
        text-align: center;
        padding: 9px 0;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.85rem;
        border: 1px solid #e2e8f0;
        transition: all 0.2s ease;
    }

    .github-btn:hover {
        background-color: #e2e8f0;
        color: #0f172a !important;
        transform: translateY(-1px);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# หัวข้อหน้าเว็บพร้อม Gradient Text
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px; margin-bottom: 30px;'>
        <h1 style='font-weight: 800; color: #0f172a; font-size: 2.3rem; margin-bottom: 10px;'>
            🧊 Drink Recommendation Portal
        </h1>
        <p style='color: #64748b; font-size: 1.05rem;'>
            ศูนย์รวมระบบแนะนำเครื่องดื่มอัจฉริยะด้วยเทคโนโลยี Graph Database และเอกสารคู่มือการใช้งาน
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# สร้าง Layout 4 คอลัมน์
cols = st.columns(4)

# การ์ดที่ 1: Graph Analysis Model
with cols[0]:
    st.markdown(
        """
        <div class="card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 12px;">⚔️</div>
                <div class="card-badge">Google Colab</div>
                <div class="card-title">Graph Analysis Model</div>
                <div class="card-desc">วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการสั่งเครื่องดื่มเชิงลึกด้วย Graph Algorithms</div>
            </div>
            <div>
                <a href="https://colab.research.google.com/drive/1cFFUUkU0ceVjAmpGGb1tFRdwrc63MHnT?usp=sharing" target="_blank" class="custom-btn">เปิดใช้งาน ➔</a>
                <a href="https://github.com/YOUR_GITHUB_LINK_1" target="_blank" class="github-btn">🐱 ดูโค้ดบน GitHub</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# การ์ดที่ 2: Neo4j Graph Recommender
with cols[1]:
    st.markdown(
        """
        <div class="card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 12px;">📊</div>
                <div class="card-badge">Neo4j Database</div>
                <div class="card-title">Neo4j Recommender</div>
                <div class="card-desc">ระบบแนะนำเครื่องดื่มที่มีประสิทธิภาพสูงด้วยโครงสร้างฐานข้อมูลแบบกราฟ Neo4j</div>
            </div>
            <div>
                <a href="https://colab.research.google.com/drive/15EkYZchP1E09enM5Qk4kIBcA8SpzxOiA?usp=sharing" target="_blank" class="custom-btn">เปิดใช้งาน ➔</a>
                <a href="https://github.com/YOUR_GITHUB_LINK_2" target="_blank" class="github-btn">🐱 ดูโค้ดบน GitHub</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# การ์ดที่ 3: Streamlit Web Portal
with cols[2]:
    st.markdown(
        """
        <div class="card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 12px;">🎯</div>
                <div class="card-badge">Web Application</div>
                <div class="card-title">Streamlit Web Portal</div>
                <div class="card-desc">ใช้งานระบบแนะนำเครื่องดื่มผ่านหน้าเว็บอินเทอร์เฟซสำเร็จรูป สะดวกและรวดเร็ว</div>
            </div>
            <div>
                <a href="https://drink-graph-recommendation-019-pvrsrplg8hnmtfupwhp8ss.streamlit.app/" target="_blank" class="custom-btn">เข้าสู่เว็บไซต์ ➔</a>
                <a href="https://github.com/YOUR_GITHUB_LINK_3" target="_blank" class="github-btn">🐱 ดูโค้ดบน GitHub</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# การ์ดที่ 4: สำหรับดาวน์โหลดไฟล์ PDF
with cols[3]:
    st.markdown(
        """
        <div class="card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 12px;">📥</div>
                <div class="card-badge">Documentation</div>
                <div class="card-title">Neo4j_งานของผู้เรียน_ระบบชมรม</div>
                <div class="card-desc">Neo4j_งานของผู้เรียน_ระบบชมรม PDF</div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    
    # ปุ่มดาวน์โหลด PDF
    try:
        with open("664245019_club.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            
        st.download_button(
            label="📄 ดาวน์โหลด PDF",
            data=pdf_bytes,
            file_name="664245019_club.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    except FileNotFoundError:
        st.warning("⚠ ไม่พบไฟล์ PDF")

    # ลิงก์ GitHub สำหรับช่องที่ 4
    st.markdown(
        """
            <a href="https://github.com/YOUR_GITHUB_LINK_4" target="_blank" class="github-btn" style="margin-top: 8px;">🐱 ดูโค้ดบน GitHub</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer เล็กๆ ด้านล่าง
st.markdown(
    """
    <div style='text-align: center; color: #94a3b8; font-size: 0.85rem; margin-top: 40px; margin-bottom: 20px;'>
        Drink Recommendation Portal • Powered by นายคณิศร จันทรสูตร 664245019
    </div>
    """,
    unsafe_allow_html=True,
)
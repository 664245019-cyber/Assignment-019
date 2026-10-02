```python
import streamlit as st
import base64

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="Drink Recommendation Portal",
    page_icon="🧊",
    layout="wide",
)

# =========================
# Custom CSS
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }

    .card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02),
                    0 2px 4px -1px rgba(0, 0, 0, 0.02);
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
        min-height: 330px;
        box-sizing: border-box;
    }

    .card:hover {
        border-color: #38bdf8;
        box-shadow: 0 20px 25px -5px rgba(56, 189, 248, 0.12),
                    0 8px 10px -6px rgba(56, 189, 248, 0.1);
        transform: translateY(-6px);
    }

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

    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 10px;
        color: #0f172a;
        line-height: 1.4;
    }

    .card-desc {
        font-size: 0.85rem;
        color: #64748b;
        margin-bottom: 20px;
        line-height: 1.5;
        flex-grow: 1;
    }

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

# =========================
# หัวข้อ
# =========================
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px; margin-bottom: 30px;'>
        <h1 style='font-weight: 800; color: #0f172a; font-size: 2.3rem; margin-bottom: 10px;'>
            🧊 รวมงานระบบแนะนำ และ การบ้านทั้งหมด
        </h1>
        <p style='color: #64748b; font-size: 1.05rem;'>
            เลือกงานที่ต้องการเปิดดูได้จากการ์ดด้านล่าง
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================
# ฟังก์ชันแปลง PDF เป็น Base64
# =========================
def get_pdf_link(filename):
    try:
        with open(filename, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        return f"data:application/pdf;base64,{base64_pdf}"

    except FileNotFoundError:
        return "#"


# =========================
# PDF แต่ละไฟล์
# =========================

drink_pdf_link = get_pdf_link(
    "Drink_Recommendation_Presentation_019.pdf"
)

club_pdf_link = get_pdf_link(
    "664245019_club.pdf"
)

book_pdf_link = get_pdf_link(
    "ตอบคำถามBook Recommend.pdf"
)


# =========================
# สร้าง Layout 5 คอลัมน์
# =========================
cols = st.columns(5)


# =========================
# การ์ดที่ 1
# Graph Analysis Model
# =========================
with cols[0]:
    st.markdown(
        """
        <div class="card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 12px;">⚔️</div>

                <div class="card-badge">Google Colab</div>

                <div class="card-title">
                    แนะนำเครื่องดื่มด้วย Graph Analysis
                </div>

                <div class="card-desc">
                    วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการสั่งเครื่องดื่มเชิงลึกด้วย Graph Algorithms
                </div>
            </div>

            <div>
                <a href="https://colab.research.google.com/drive/1cFFUUkU0ceVjAmpGGb1tFRdwrc63MHnT?usp=sharing"
                   target="_blank"
                   class="custom-btn">
                    เปิดใช้งาน ➔
                </a>

                <a href="https://github.com/664245019-cyber/Assignment-019/blob/main/664245019_Drink_reccomend.ipynb"
                   target="_blank"
                   class="github-btn">
                    🐱 ดูโค้ดบน GitHub
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================
# การ์ดที่ 2
# Neo4j Graph Recommender
# =========================
with cols[1]:
    st.markdown(
        """
        <div class="card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 12px;">📊</div>

                <div class="card-badge">Neo4j Database</div>

                <div class="card-title">
                    แนะนำเครื่องดื่มด้วย Neo4j
                </div>

                <div class="card-desc">
                    ระบบแนะนำเครื่องดื่มที่มีประสิทธิภาพสูงด้วยโครงสร้างฐานข้อมูลแบบกราฟ Neo4j
                </div>
            </div>

            <div>
                <a href="https://colab.research.google.com/drive/15EkYZchP1E09enM5Qk4kIBcA8SpzxOiA?usp=sharing"
                   target="_blank"
                   class="custom-btn">
                    เปิดใช้งาน ➔
                </a>

                <a href="https://github.com/664245019-cyber/Assignment-019/blob/main/664245019_Drink_reccomend_neo4j.ipynb"
                   target="_blank"
                   class="github-btn">
                    🐱 ดูโค้ดบน GitHub
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================
# การ์ดที่ 3
# Streamlit Web Portal
# =========================
with cols[2]:
    st.markdown(
        f"""
        <div class="card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 12px;">🎯</div>

                <div class="card-badge">Web Application</div>

                <div class="card-title">
                    ระบบแนะนำเครื่องดื่ม
                </div>

                <div class="card-desc">
                    ใช้งานระบบแนะนำเครื่องดื่มผ่านหน้าเว็บอินเทอร์เฟซสำเร็จรูป สะดวกและรวดเร็ว
                </div>
            </div>

            <div>
                <a href="https://drink-graph-recommendation-019-pvrsrplg8hnmtfupwhp8ss.streamlit.app/"
                   target="_blank"
                   class="custom-btn">
                    เข้าสู่เว็บไซต์ ➔
                </a>

                <a href="{drink_pdf_link}"
                   download="Drink_Recommendation_Presentation_019.pdf"
                   class="custom-btn">
                    📄 ดาวน์โหลด PDF
                </a>

                <a href="https://github.com/664245019-cyber/Drink-Graph-Recommendation-019"
                   target="_blank"
                   class="github-btn">
                    🐱 ดูโค้ดบน GitHub
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================
# การ์ดที่ 4
# ระบบชมรม Neo4j
# =========================
with cols[3]:
    st.markdown(
        f"""
        <div class="card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 12px;">📥</div>

                <div class="card-badge">Documentation</div>

                <div class="card-title">
                    ระบบชมรมด้วย Neo4j
                </div>

                <div class="card-desc">
                    งานระบบชมรม: นักศึกษา ชมรม ความสัมพันธ์ และคำสั่ง Cypher พร้อมเอกสาร PDF
                </div>
            </div>

            <div>
                <a href="{club_pdf_link}"
                   download="664245019_club.pdf"
                   class="custom-btn">
                    📄 ดาวน์โหลด PDF
                </a>

                <a href="https://github.com/664245019-cyber/Assignment-019/blob/main/664245019_club.pdf"
                   target="_blank"
                   class="github-btn">
                    🐱 ดูงานบน GitHub
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================
# การ์ดที่ 5
# Book Recommend System
# =========================
with cols[4]:
    st.markdown(
        f"""
        <div class="card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 12px;">📚</div>

                <div class="card-badge">Documentation</div>

                <div class="card-title">
                    Book Recommend System
                </div>

                <div class="card-desc">
                    งานตอบคำถามระบบแนะนำหนังสือ: นักศึกษา ความสัมพันธ์ และคำสั่ง Cypher พร้อมเอกสาร PDF
                </div>
            </div>

            <div>
                <a href="{book_pdf_link}"
                   download="ตอบคำถามBook Recommend.pdf"
                   class="custom-btn">
                    📄 ดาวน์โหลด PDF
                </a>

                <a href="https://github.com/664245019-cyber/Assignment-019/blob/main/ตอบคำถามBook Recommend.pdf"
                   target="_blank"
                   class="github-btn">
                    🐱 ดูงานบน GitHub
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================
# Footer
# =========================
st.markdown(
    """
    <div style='text-align: center; color: #94a3b8; font-size: 1rem;
                margin-top: 40px; margin-bottom: 20px;'>
        All Assignment Portal • 664245019 คณิศร จันทรสูตร
    </div>
    """,
    unsafe_allow_html=True,
)

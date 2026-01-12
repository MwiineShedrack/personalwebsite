import streamlit as st
from PIL import Image
import datetime

# ────────────────────────────────────────────────
# Page config
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="Shedrack's Personal Website",
    page_icon="👨‍🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better look (dark/light theme friendly)
st.markdown("""
    <style>
    .main {background-color: #f9fafb;}
    h1, h2 {color: #1e3a8a;}
    .stTabs [data-baseweb="tab-list"] {gap: 8px;}
    .stTabs [data-baseweb="tab"] {padding: 8px 16px; border-radius: 6px;}
    .profile-img {border-radius: 50%; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
    .card {background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Sidebar - Navigation & Quick Links
# ────────────────────────────────────────────────
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to", [
        "🏠 Home & Profile",
        "📝 Blog & Articles",
        "🔬 Research Papers",
        "🛠 Apps & Projects",
        "📧 Contact"
    ], label_visibility="collapsed")

    st.divider()
    st.markdown("**Quick Links**")
    st.markdown("[LinkedIn](https://linkedin.com/in/shedrack)")
    st.markdown("[GitHub](https://github.com/shedrack)")
    st.markdown("[Twitter/X](https://x.com/shedrack)")

    st.divider()
    st.caption(f"© {datetime.date.today().year} Shedrack • Nairobi, Kenya")

# ────────────────────────────────────────────────
# Main Content - Based on selected page
# ────────────────────────────────────────────────
if page == "🏠 Home & Profile":
    st.title("Welcome to Shedrack's Website")
    st.caption("Researcher, Developer, and Innovator in Nairobi")

    # Profile section
    col1, col2 = st.columns([1, 3])
    with col1:
        # Replace with your actual profile picture path or URL
        profile_pic = Image.open("profile.jpg")  # Assume you have a 'profile.jpg' in the same folder
        st.image(profile_pic, width=200, caption="Shedrack", use_column_width=True, output_format="auto")

    with col2:
        st.header("About Me")
        st.markdown("""
        Hello! I'm Shedrack, a passionate researcher and developer based in Nairobi, Kenya. 
        With a background in [Your Field, e.g., AI and Data Science], I focus on [brief bio, e.g., building innovative apps and conducting research in machine learning and data analytics].
        
        - **Education**: [e.g., MSc in Computer Science from University of Nairobi]
        - **Experience**: [e.g., 5+ years in tech, working on AI projects]
        - **Interests**: [e.g., Open-source, AI ethics, African tech innovation]
        
        Feel free to explore my work below!
        """)

    st.divider()
    st.subheader("Latest Updates")
    st.markdown("- Published new paper on [topic] - Check Research section")
    st.markdown("- Launched new Streamlit app for [purpose] - See Apps section")
    st.markdown("- Blog post: [title] - Read in Blog")

elif page == "📝 Blog & Articles":
    st.title("Blog & Articles")
    st.caption("My thoughts on research, tech, and more")

    # Example blog posts - you can add more as markdown or load from files
    with st.expander("Post 1: Title of Your First Article (Date)", expanded=True):
        st.markdown("""
        ### Introduction
        [Your content here...]
        
        ### Key Points
        - Point 1
        - Point 2
        
        Read full article: [Link to PDF or external site]
        """)

    with st.expander("Post 2: Another Article Title (Date)"):
        st.markdown("[Content...]")

    st.info("New posts coming soon! Contact me to suggest topics.")

elif page == "🔬 Research Papers":
    st.title("Research Papers")
    st.caption("My published work and ongoing research")

    # List papers with links
    papers = [
        {
            "title": "Paper 1: Title of Research Paper",
            "description": "Brief abstract or summary...",
            "link": "https://arxiv.org/abs/xxxx.xxxx",
            "date": "2025"
        },
        {
            "title": "Paper 2: Another Paper",
            "description": "Summary...",
            "link": "https://doi.org/xxxx",
            "date": "2024"
        }
    ]

    for paper in papers:
        with st.container(border=True):
            st.markdown(f"**{paper['title']}** ({paper['date']})")
            st.markdown(paper['description'])
            st.markdown(f"[Read Paper]({paper['link']})")

    st.info("Upload or add more papers via code updates.")

elif page == "🛠 Apps & Projects":
    st.title("Apps & Projects")
    st.caption("Tools and applications I've built")

    # List projects with links
    projects = [
        {
            "name": "App 1: Data Analytics Dashboard",
            "description": "A Streamlit app for data exploration...",
            "link": "https://your-app-url.streamlit.app"
        },
        {
            "name": "App 2: AI Insights Tool",
            "description": "Semantic search and insights generator...",
            "link": "https://another-app.streamlit.app"
        }
    ]

    cols = st.columns(2)
    for i, proj in enumerate(projects):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"**{proj['name']}**")
                st.markdown(proj['description'])
                st.button("Open App", on_click=lambda url=proj['link']: st.markdown(f"[Launch]({url})"))

    st.info("More projects in development!")

elif page == "📧 Contact":
    st.title("Get in Touch")
    st.caption("Feel free to reach out!")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            # Placeholder for actual email sending (use smtplib or service like SendGrid)
            st.success(f"Thanks {name}! Your message has been sent (simulated).")
            # In real: send email logic here

    st.divider()
    st.markdown("**Email**: shedrack@example.com")
    st.markdown("**Phone**: +254-XXX-XXX-XXX")
    st.markdown("**Location**: Nairobi, Kenya")

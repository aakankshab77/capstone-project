"""
Prompt Engineering Platform (PEP) - Streamlit Frontend
Main entry point with authentication and navigation.
"""
import streamlit as st
import requests
from datetime import datetime

# Page config must be first
st.set_page_config(
    page_title="Prompt Engineering Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# API base URL
API_BASE = "http://localhost:8000/api/v1"

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "token" not in st.session_state:
    st.session_state.token = None
if "user" not in st.session_state:
    st.session_state.user = None
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "api_key_configured" not in st.session_state:
    st.session_state.api_key_configured = False


def api_request(method, endpoint, data=None, params=None):
    """Make an API request with authentication."""
    url = f"{API_BASE}{endpoint}"
    headers = (
        {"Authorization": f"Bearer {st.session_state.token}"}
        if st.session_state.token
        else {}
    )

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=30)

        elif method == "POST":
            if endpoint == "/login":
                response = requests.post(
                    url,
                    headers=headers,
                    data={
                        "username": data["email"],
                        "password": data["password"],
                    },
                    timeout=60,
                )
            else:
                response = requests.post(
                    url,
                    headers=headers,
                    json=data,
                    timeout=60,
                )

        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data, timeout=30)

        elif method == "DELETE":
            response = requests.delete(url, headers=headers, timeout=30)

        else:
            return None

        if response.status_code == 401:
            st.session_state.authenticated = False
            st.session_state.token = None
            st.session_state.user = None
            st.rerun()

        return response.json() if response.status_code < 500 else None

    except requests.exceptions.ConnectionError:
        st.error("🚨 Cannot connect to backend. Make sure the API server is running.")
        return None

    except Exception as e:
        st.error(f"⚠️ API Error: {str(e)}")
        return None


# ===================== AUTHENTICATION UI =====================

def show_login_page():
    """Show login/signup page."""
    st.markdown("""
    <style>
    .auth-container {
        max-width: 450px;
        margin: 60px auto;
        padding: 40px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    .auth-title {
        color: white;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    .auth-subtitle {
        color: rgba(255,255,255,0.8);
        text-align: center;
        margin-bottom: 30px;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        st.markdown('<h1 class="auth-title">🤖 PEP</h1>', unsafe_allow_html=True)
        st.markdown('<p class="auth-subtitle">Prompt Engineering Platform</p>', unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🔑 Login", "📝 Sign Up"])
        
        with tab1:
            with st.form("login_form"):
                email = st.text_input("Email", placeholder="Enter your email")
                password = st.text_input("Password", type="password", placeholder="Enter your password")
                submitted = st.form_submit_button("Login", use_container_width=True)
                
                if submitted:
                    if email and password:
                        result = api_request("POST", "/login", {"email": email, "password": password})
                        st.write(result)
                        if result and "access_token" in result:
                            st.session_state.token = result["access_token"]
                            st.session_state.user = result
                            st.session_state.authenticated = True
                            st.success("✅ Login successful!")
                            st.rerun()
                        else:
                            st.error("❌ Invalid email or password")
                    else:
                        st.warning("Please fill in all fields")
        
        with tab2:
            with st.form("signup_form"):
                name = st.text_input("Full Name", placeholder="Enter your name")
                email = st.text_input("Email", placeholder="Enter your email")
                password = st.text_input("Password", type="password", placeholder="Create a password")
                confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
                submitted = st.form_submit_button("Sign Up", use_container_width=True)
                
                if submitted:
                    if name and email and password and confirm_password:
                        if password == confirm_password:
                            result = api_request("POST", "/signup", {"name": name, "email": email, "password": password})
                            if result and "access_token" in result:
                                st.session_state.token = result["access_token"]
                                st.session_state.user = result
                                st.session_state.authenticated = True
                                st.success("✅ Account created successfully!")
                                st.rerun()
                            else:
                                error_msg = result.get("detail", "Registration failed") if result else "Registration failed"
                                st.error(f"❌ {error_msg}")
                        else:
                            st.error("❌ Passwords don't match")
                    else:
                        st.warning("Please fill in all fields")
        
        st.markdown('</div>', unsafe_allow_html=True)


# ===================== SIDEBAR NAVIGATION =====================

def show_sidebar():
    """Show sidebar navigation."""
    with st.sidebar:
        st.markdown("## 🤖 PEP")
        st.markdown("---")
        
        # User info
        if st.session_state.user:
            st.markdown(f"👤 **{st.session_state.user.get('name', 'User')}**")
            st.markdown(f"📧 {st.session_state.user.get('email', '')}")
            st.markdown(f"🎭 Role: `{st.session_state.user.get('role', 'user')}`")
            st.markdown("---")
        
        # Navigation
        pages = {
            "🏠 Home": "Home",
            "📄 RAG Chat": "RAG Chat",
            "📝 Prompt Builder": "Prompt Builder",
            "📂 Prompt Library": "Prompt Library",
            "📊 Analytics": "Analytics",
            "💰 Cost Tracker": "Cost Tracker",
            "⚖ A/B Testing": "A/B Testing",
            "📜 History": "History",
            "⚙ Settings": "Settings",
        }
        
        for label, page_name in pages.items():
            if st.button(label, use_container_width=True, 
                         type="secondary" if st.session_state.page != page_name else "primary"):
                st.session_state.page = page_name
                st.rerun()
        
        st.markdown("---")
        
        # API status
        st.markdown("### 🔌 API Status")
        try:
            health = requests.get("http://127.0.0.1:8000/health", timeout=3)
            if health.status_code == 200:
                st.success("🟢 Connected")
            else:
                st.error("🔴 Disconnected")
        except:
            st.error("🔴 Disconnected")
        
        # Logout
        if st.button("🚪 Logout", use_container_width=True, type="secondary"):
            st.session_state.authenticated = False
            st.session_state.token = None
            st.session_state.user = None
            st.session_state.page = "Home"
            st.rerun()


# ===================== PAGE ROUTER =====================

# Main app flow
if not st.session_state.authenticated:
    show_login_page()
else:
    show_sidebar()
    
    # Route to appropriate page
    page = st.session_state.page
    
    if page == "Home":
        from pages.dashboard import show_dashboard
        show_dashboard(api_request)
    elif page == "Prompt Builder":
        from pages.prompt_builder import show_prompt_builder
        show_prompt_builder(api_request)
    elif page == "Prompt Library":
        from pages.prompt_library import show_prompt_library
        show_prompt_library(api_request)
    elif page == "Analytics":
        from pages.analytics import show_analytics
        show_analytics(api_request)
    elif page == "Cost Tracker":
        from pages.cost_tracker import show_cost_tracker
        show_cost_tracker(api_request)
    elif page == "A/B Testing":
        from pages.ab_testing import show_ab_testing
        show_ab_testing(api_request)
    elif page == "History":
        from pages.history import show_history
        show_history(api_request)
    elif page == "RAG Chat":
        from pages.rag_chat import show_rag_chat
        show_rag_chat(api_request)
    elif page == "Settings":
        from pages.settings import show_settings
        show_settings(api_request)


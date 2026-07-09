import streamlit as st
from scraper import scrape_website
from agent import analyze_company_data

# 1. Config and Styling
st.set_page_config(page_title="Competitor Intelligence Agent", page_icon="🕵️‍♂️", layout="wide")

st.title("🕵️‍♂️ B2B Competitor Intelligence Agent")
st.write("Scrape any startup homepage instantly and use Gemini 3.5 Flash to extract structured business intelligence.")

# 2. Sidebar Configuration for Credentials
with st.sidebar:
    st.header("🔑 Authentication")
    api_key = st.text_input("Enter Gemini API Key:", type="password")
    st.markdown("---")
    st.write("💡 *Tip: This agent works best on product-based B2B or SaaS startup homepages.*")

# 3. Main Form Inputs
url_to_analyze = st.text_input("Target Startup URL:", placeholder="https://example.com")

# 4. Core Execution Flow
if st.button("Run Market Analysis", type="primary"):
    if not api_key:
        st.error("Please provide your Gemini API Key in the sidebar.")
    elif not url_to_analyze:
        st.warning("Please enter a target URL to scan.")
    else:
        # Step 1: Scrape the data
        with st.spinner("🕷️ Launching crawler and extracting website text..."):
            raw_text = scrape_website(url_to_analyze)
            
        if "Error" in raw_text:
            st.error(raw_text)
        else:
            # Step 2: Pass data to the agent
            with st.spinner("🧠 Initializing Gemini 3.5 Flash data parsing..."):
                structured_report = analyze_company_data(raw_text, api_key)
            
            # Step 3: Render the Results Dashboard
            if "Error" in structured_report:
                st.error(structured_report["Error"])
            else:
                st.success("🎯 Analysis Complete!")
                
                # Create visual metrics cards or clean text displays
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("💡 Core Value Proposition")
                    st.info(structured_report.get("Value_Proposition", "N/A"))
                    
                    st.subheader("💰 Pricing Strategy")
                    st.success(structured_report.get("Pricing_Model", "N/A"))
                    
                with col2:
                    st.subheader("🎯 Ideal Target Audience")
                    st.warning(structured_report.get("Target_Audience", "N/A"))
                    
                # Optional: Show the raw JSON payload below for developers
                with st.expander("🛠️ View Raw JSON Response"):
                    st.json(structured_report)

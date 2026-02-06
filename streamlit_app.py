import streamlit as st
import pandas as pd
import io

# Page Configuration - MUST be the first Streamlit command
st.set_page_config(
    page_title="BI - Classify Region",
    page_icon="🗺️",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    .uploadedFile {
        border-radius: 10px;
        padding: 20px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1 {
        color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)

# Define regions
mien_bac = [
    'hanoi', 'hai phong', 'quang ninh', 'hai duong', 'hung yen', 'nam dinh',
    'ninh binh', 'thai binh', 'vinh phuc', 'ha giang', 'cao bang', 'bac kan',
    'lang son', 'tuyen quang', 'thai nguyen', 'phu tho', 'bac giang', 'lao cai',
    'yen bai', 'dien bien', 'hoa binh', 'lai chau', 'son la', 'bac ninh'
]

mien_trung = [
    'thanh hoa', 'nghe an', 'ha tinh', 'quang binh', 'quang tri', 'thua thien hue', 'hue',
    'da nang', 'quang nam', 'quang ngai', 'binh dinh', 'phu yen', 'khanh hoa', 'nha trang',
    'ninh thuan', 'binh thuan', 'kon tum', 'gia lai', 'dak lak', 'dak nong', 'lam dong', 'da lat'
]

mien_nam = [
    'ho chi minh', 'hcm', 'binh duong', 'dong nai', 'tay ninh', 'ba ria', 'vung tau',
    'long an', 'tien giang', 'ben tre', 'tra vinh', 'vinh long', 'dong thap',
    'an giang', 'kien giang', 'can tho', 'hau giang', 'soc trang', 'bac lieu', 'ca mau', 'binh phuoc'
]

def phan_loai_mien(dia_chi):
    if pd.isna(dia_chi):
        return "Other"
        
    # Chuyển địa chỉ về chữ thường để so sánh chính xác
    dia_chi_lower = str(dia_chi).lower()

    # Kiểm tra miền Nam trước (vì TP.HCM xuất hiện nhiều nhất)
    for tinh in mien_nam:
        if tinh in dia_chi_lower:
            return 'Southside'

    # Kiểm tra miền Bắc
    for tinh in mien_bac:
        if tinh in dia_chi_lower:
            return 'Northside'

    # Kiểm tra miền Trung
    for tinh in mien_trung:
        if tinh in dia_chi_lower:
            return 'Central'

    return "Other" # Không tìm thấy từ khóa phù hợp

# Sidebar for Inputs
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/854/854878.png", width=100) # Generic map icon
    st.title("Settings")
    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])
    
    st.info("Upload an Excel file containing address data to get started.")

# Main Content
st.title("BI - Classify Region")
st.markdown("### Automate your geographical data classification")
st.divider()

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        
        # Drop unnamed columns
        cols_to_drop = df.columns[df.columns.str.contains('Unnamed', case=False, na=False)]
        if not cols_to_drop.empty:
            df.drop(columns=cols_to_drop, inplace=True)
            
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Data Setup")
            columns = df.columns.tolist()
            if columns:
                selected_column = st.selectbox("Choose Address Column", options=columns)
                
                if st.button("🚀 Run Classification"):
                    # Process
                    df["Region"] = df[selected_column].apply(phan_loai_mien)
                    
                    # Store result in session state to persist after reload (optional simple optimization)
                    st.session_state['classified_df'] = df
                    st.session_state['processed'] = True
            else:
                st.warning("No columns found in the file.")

        # Display Results
        if st.session_state.get('processed'):
            df_result = st.session_state['classified_df']
            
            # Metrics
            st.divider()
            m1, m2, m3 = st.columns(3)
            m1.metric("Total Records", len(df_result))
            m2.metric("Unique Regions", df_result["Region"].nunique())
            m3.metric("Most Common", df_result["Region"].mode()[0] if not df_result["Region"].empty else "N/A")
            
            # Charts and Data
            st.subheader("Classification Results")
            c1, c2 = st.columns([2, 1])
            
            with c1:
                st.dataframe(df_result.head(10), width="stretch")
                
            with c2:
                region_counts = df_result["Region"].value_counts()
                st.bar_chart(region_counts)
            
            # Download
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_result.to_excel(writer, index=False)
            data = output.getvalue()
            
            st.download_button(
                label="⬇️ Download Result",
                data=data,
                file_name="classified_regions.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    # Empty State
    st.markdown("""
    <div style='text-align: center; padding: 50px; color: #666;'>
        <h2>👋 Welcome!</h2>
        <p>Please upload an Excel file from the sidebar to begin.</p>
    </div>
    """, unsafe_allow_html=True)

# BI - Region Classifier 🗺️

A modern Streamlit web application designed to automate geographical data classification from Excel files into North, Central, and South regions of Vietnam.

## 🚀 Features

- **Excel Upload**: Support for `.xlsx` and `.xls` files.
- **Smart Column Selection**: Choose which column contains the address data.
- **Automated Classification**: Categorizes addresses into:
  - **Northside** (Mien Bac)
  - **Central** (Mien Trung)
  - **Southside** (Mien Nam)
- **Data Visualization**: Real-time region distribution metrics and charts.
- **Export**: Download the processed data as a new Excel file.
- **Responsive UI**: Clean, sidebar-based interface with custom styling.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tuancompa2610/BI-Region-Classifier.git
   cd BI-Region-Classifier
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Run the app**:
   ```bash
   streamlit run streamlit_app.py
   ```

2. **How to use**:
   - Upload your Excel file via the sidebar.
   - Select the column that contains the addresses/provinces.
   - Click **Run Classification**.
   - Review results and download the final Excel file.

## 📦 Project Structure

- `streamlit_app.py`: The main web application logic and UI.
- `classify_region.py`: Original script containing classification logic.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Files to exclude from Git.

## 🌐 Deployment

This app is designed to be easily deployed on **Streamlit Cloud**. Simply connect your GitHub repository and point to `streamlit_app.py`.

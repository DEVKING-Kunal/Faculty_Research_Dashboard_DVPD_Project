# NITJ Research Admin Dashboard

A comprehensive Research Analytics Dashboard built using Streamlit and Plotly. This application is designed for academic institutions (specifically customized for NIT Jalandhar) to track, visualize, and analyze faculty research performance such as publications, citations, H-index, and global collaborations.

---

## Key Features

### Interactive Overview
- Real-time metrics for total faculty, publications, citations, and average H-Index.

### Dynamic Data Loading
- Upload your own CSV file and map columns using the sidebar.
- Option to load built-in demo data for testing.

### Impact Leaderboard
- Automated ranking based on an Impact Score:
  - Citations (40%)
  - H-Index (40%)
  - Total Publications (20%)

### Advanced Analytics
- Department-wise research performance.
- H-index distribution box plots.
- “Quantity vs Quality” scatter visualization.
- Global collaboration maps.

### Smart Search
- Fuzzy search for faculty names using `thefuzz`.

### EduAdmin Theme
- Clean, minimal UI with custom CSS styling.

---

## Tech Stack
- Python 3.8+
- Streamlit
- Pandas
- Plotly
- TheFuzz
- NumPy

---

## Installation & Setup

### 1. Clone the Repository
git clone https://github.com/yourusername/nitj-research-dashboard.git  
cd nitj-research-dashboard

### 2. Create a Virtual Environment (optional)
python -m venv venv

### Activate the environment  
Windows:  
venv\Scripts\activate

Mac/Linux:  
source venv/bin/activate

### 3. Install Dependencies
pip install streamlit pandas plotly numpy thefuzz

### 4. Run the Dashboard
streamlit run app.py

---

## Data Format (CSV)

Your CSV does not need exact column names since you can map fields in the sidebar.  
The recommended fields are:

| Column Name        | Description                     | Type    |
|--------------------|---------------------------------|---------|
| name               | Faculty Name                    | String  |
| department         | Department Name                 | String  |
| designation        | Job Title                       | String  |
| total_publications | Publication Count               | Integer |
| citations_box      | Total Citations                 | Integer |
| h_index            | H-Index                         | Integer |

Note:  
If I10_Index, Research_Area, or Country are missing, defaults are generated so charts do not break.

---

## Image Assets

Place the following images in the project root for the Faculty Profile page:

- director.jpg  
- banalaxmi mam.jpeg  

If missing, default placeholder images are used.  
You may replace filenames or update them in the code (around lines 304–305).

---

## Usage Guide

### Sidebar
- Load demo data immediately OR upload your own CSV.
- Map CSV columns using dropdowns.

### Tabs
- **Overview:** Top stats & quick insights.  
- **Leaderboard:** Faculty ranked by Impact Score.  
- **Analytics:** Department charts, scatter plots, H-index distributions.  
- **Faculty Profile:** Search & view individual faculty details.

---

## Contribution
Contributions are welcome!  
Feel free to submit issues or pull requests.

---



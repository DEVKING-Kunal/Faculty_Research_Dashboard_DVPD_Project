# NITJ Research Admin Dashboard

A comprehensive Research Analytics Dashboard built using Streamlit and Plotly.  
This tool is designed for academic institutions (specifically customized for NIT Jalandhar) to track, visualize, and analyze faculty research performance such as publications, citations, H-index, and global collaborations.

---

## Key Features

### Interactive Overview
- Real-time metrics for total faculty, publications, citations, and average H-Index.

### Dynamic Data Loading
- Upload your own CSV file and map columns using the sidebar.
- Option to load built-in demo data for testing.

### Impact Leaderboard
- Automatic ranking of faculty based on an “Impact Score”:
  - Citations (40%)
  - H-Index (40%)
  - Publication count (20%)

### Advanced Analytics
- Department-wise research performance.
- H-Index distribution (box plots).
- “Quantity vs. Quality” scatter analysis.
- Global collaboration maps (choropleth).

### Smart Search
- Fuzzy name search using `thefuzz` for handling typos.

### EduAdmin Theme
- Clean and simple UI enhanced with custom CSS.

---

## Tech Stack
- Python 3.8+
- Streamlit
- Pandas
- Plotly (Express & Graph Objects)
- TheFuzz
- NumPy

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/nitj-research-dashboard.git
cd nitj-research-dashboard
2. Create a Virtual Environment (optional)
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install streamlit pandas plotly numpy thefuzz
4. Run the Dashboard
bash
Copy code
streamlit run app.py
Data Format (CSV Requirements)
Column names do not need to match exactly; they can be mapped in the sidebar.
The data should ideally contain:

Column Name	Description	Type
name	Faculty Name	String
department	Department (CSE, ECE, etc.)	String
designation	Job title (Professor, etc.)	String
total_publications	Number of papers	Integer
citations_box	Total citations	Integer
h_index	H-Index	Integer

Note:
If the CSV does not include I10_Index, Research_Area, or Country, the app will generate default values to avoid breaking visualizations.

Image Assets
The app looks for the following images in the root directory for the Faculty Profile section:

director.jpg

banalaxmi mam.jpeg

If these are not found, the dashboard falls back to default placeholder images.
You can customize this by placing your own images or updating the filenames in the code (around lines 304–305).

Usage Guide
Sidebar Configuration
Load demo data to try the dashboard immediately.

Or upload your CSV file.

Use dropdown menus to map your columns correctly.

Navigation Tabs
Overview: General stats and top contributors.

Leaderboard: Ranking based on impact score.

Analytics: Charts, department insights, distribution plots.

Faculty Profile: Search and view individual faculty details.

Contribution
Contributions are welcome. Feel free to open issues or submit pull requests.


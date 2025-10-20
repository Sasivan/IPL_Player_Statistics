# 🏏 IPL Player Stats Filter – Group 13

A complete **IPL Player Analysis and Filtering System** built using **Python** and **Streamlit**.  
This project enables users to explore, filter, and compare IPL player performance with interactive charts and a modern UI.

---

## 📘 Project Overview

The **IPL Player Stats Filter** simplifies cricket analytics by merging **data cleaning**, **backend logic**, and **interactive visualization**.  
It provides an integrated platform for filtering, comparing, and visualizing IPL player performance.

---

## 🧩 Features

### 🧠 **Phase 1 – Data Preparation**
- Cleaned raw IPL dataset to create a structured dataset.
- Downloaded and linked player images to dataset entries.
- Stored cleaned data in `data/ipl_player_stats_clean.csv`.

| File | Description |
|------|--------------|
| `src/data_cleaning.py` | Cleans and prepares IPL dataset |
| `src/download_player_images.py` | Downloads player images from URLs |
| `data/ipl_player_stats_clean.csv` | Final cleaned CSV file used across the project |

---

### ⚙️ **Phase 2 – Backend Development (Data Handling)**
| File | Description |
|------|--------------|
| `backend/data_loader.py` | Loads IPL CSV data into DataFrame |
| `backend/player_model.py` | Defines `Player` class for structured player data |
| `backend/stats_filter.py` | Provides filtering functions by team, role, avg, SR, etc. |
| `backend/search_sort.py` | Adds search and sorting capabilities |
| `tests/test_backend.py` | Unit tests for verifying backend logic |

---

### 💻 **Phase 3 – UI & Frontend (Streamlit Web App)**
| Task | File | Description |
|------|------|-------------|
| **3.1 Home Page** | `ui/home_page.py` | Displays title, navigation bar, and random player cards |
| **3.2 Filter Page** | `ui/player_filter.py` | Sidebar filters (Team, Role, Avg, SR, etc.) and table view |
| **3.3 Compare Page** | `ui/player_compare.py` | Compare two or more players visually |
| **3.4 Visualization Page** | `ui/visualization.py` | Graphs for runs, averages, and team insights |
| **3.5 About Page** | `ui/about_page.py` | Project credits, team, and mentor details |

---

### 🔗 **Phase 4 – Integration & Testing**
- Integrated all backend modules with Streamlit UI.  
- Streamlit pages dynamically load filtered data, charts, and comparisons.  
- Implemented navigation bar with clickable icons (no sidebar).  
- Tested filtering, data handling, and visualization features.

---

## 🧭 Navigation

A responsive dark-themed navigation bar gives quick access to:
- 🏠 **Home**
- 🔍 **Filter**
- ⚖️ **Compare**
- 📈 **Visualization**
- 👥 **About**

Each section is built as a separate page for modular navigation.

---

## 📁 Folder Structure

```

IPL-Player-Stats-Filter/
│
├── src/
│   ├── data_cleaning.py
│   ├── download_player_images.py
│
├── backend/
│   ├── data_loader.py
│   ├── player_model.py
│   ├── stats_filter.py
│   ├── search_sort.py
│
├── ui/
│   ├── home_page.py
│   ├── player_filter.py
│   ├── player_compare.py
│   ├── visualization.py
│   ├── about_page.py
│
├── data/
│   └── ipl_player_stats_clean.csv
│
├── player_images/
│   ├── *.jpg (Player photos)
│
├── tests/
│   └── test_backend.py
│
├── README.md
└── app.py

````

---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sasivan/IPL-Player-Stats-Filter.git
cd IPL-Player-Stats-Filter
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
streamlit run ui/home_page.py
```

---

## 🧪 Unit Testing

To verify filtering, sorting, and integration logic:

```bash
pytest tests/test_backend.py
```

---

## 🧑‍💻 Team Members

| Name      | Role                    |
| --------- | ----------------------- |
| Dev 1 | Backend Developer       |
| Dev 2 | Frontend & UI Developer |
| Dev 3 | Data Visualization      |
| Dev 4 | Integration & Testing   |

**Group No:** 13

---

## 📚 Dataset Credits

*Web Search Portraits 
---

## 🛠️ Tech Stack

| Category          | Tools / Libraries           |
| ----------------- | --------------------------- |
| **Language**      | Python 3.10+                |
| **UI Framework**  | Streamlit                   |
| **Data Handling** | Pandas, NumPy               |
| **Visualization** | Plotly, Matplotlib, Seaborn |
| **Testing**       | Pytest                      |

---

## ⭐ Future Enhancements

* Add **ML predictions** for player performance.
* Integrate **live IPL API** for real-time stats.
* Add **player comparison radar charts** and season progression graphs.

---

### 🏆 Project By *Group 13 – IPL Player Stats Filter*

**Explore. Filter. Compare. Visualize.**

> *Data meets Cricket, beautifully.*


# 📦 Demo-LLM

An educational repository demonstrating a full-stack product management system. This project is designed as a learning resource for building database-driven web apps, implementing automated testing, and integrating Natural Language Processing (NLP) tools.

## 🚀 Features

*   **Flask Web Server**: A lightweight Python backend handling all application logic.
*   **SQLite Database**: Local, file-based data storage for easy setup and portability.
*   **Dynamic UI**: Powered by **Jinja2** templates for a responsive data-driven experience.
*   **Product Management**: Full routes for viewing, adding, and modifying inventory.
*   **Automated Testing**: Includes a suite of **unit tests using pytest** to ensure code reliability and stability.
*   **AI Integration (In Progress)**: Implementation of **Sentence-BERT (SBERT)** for semantic search and AI-driven features.

## 🛠️ Tech Stack

*   **Python**: 3.11.0 (Built for 3.11, but compatible with most Python 3.x versions).
*   **Framework**: Flask.
*   **Database**: SQLite3.
*   **Testing**: Pytest.
*   **Frontend**: HTML5, CSS3, Jinja2.

## 📚 Documentation & Knowledge Base

The `/docs` folder is an evolving resource for developers and students. It currently includes:

*   **Sentence Transformers**: Concepts and implementation guides for SBERT.
*   **Flask & DB Fundamentals (Expanding)**: Documentation on routing, database schema design, and CRUD operations is being actively added.

## 📖 Installation & Usage

1. **Clone the repo**:
   ```bash
   git clone https://github.com/RaresIovu/Demo-LLM.git
   cd Demo-LLM
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Unit Tests**:
   Before launching, ensure everything is working correctly:
   ```bash
   pytest
   ```

4. **Launch the application**:
   ```bash
   python app.py
   ```
   Access the app at `http://127.0.0.1:5000`.

## 🔮 Future Roadmap

*   [ ] Expand documentation for Flask and SQLite fundamentals.
*   [ ] Integrate AI-based product recommendations.
*   [ ] Implement semantic search using SBERT embeddings.

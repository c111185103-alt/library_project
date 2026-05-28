# 線上簡易圖書館管理系統 (Smart Library Management System)

> **國立高雄科技大學 電子工程系 研究所專案報告**
> * **指導教授：** 陳朝烈 教授
> * **開發環境：** Windows / VS Code
> * **對應題目：** 題目三 (網路) - 設計一套線上(簡易)圖書館管理系統

---

## 專案介紹 (Project Overview)

本專案為一套結合 Web 前端介面與 AI 人工智慧的「線上簡易圖書館管理系統」。不僅實作了基礎的館藏與借閱管理功能，更導入了 **LLM (大型語言模型)** 與 **RAG (檢索增強生成)** 技術，打造出具備「即時館藏感知」能力的 AI 智慧客服中心。

本系統兼具實用性與現代化架構，並透過 **ngrok** 實作內網穿透，使本機伺服器可直接佈署至網際網路，產生公開網址供遠端跨網域存取與實機展示。

---

## 核心功能 (Key Features)

### 1. 基礎圖書館管理 (Library Management)
* **書籍清單展示：** Web 介面即時呈現館內所有書籍狀態。
* **借還書紀錄：** 完整追蹤書籍的借出與歸還歷程。
* **借書期限與逾期管理：** 系統自動計算借閱期限，並醒目標示 **逾期 (Overdue)** 狀態。

### 2. AI 智慧客服中心 (AI Chatbot with RAG)
* **LLM 串接：** 整合 Google **Gemini 3.5-Flash** 語言模型，提供自然流暢的文字客服體驗。
* **RAG 技術導入：** AI 在回覆前會先檢索本機資料庫 (SQLite) 中的「即時館藏清單」與「借閱狀態」作為提示詞背景 (Context)，確保 AI 能準確回答「某本書現在能不能借」等具體問題，拒絕 AI 幻覺。
* **容錯備援機制：** 具備完善的 API 錯誤捕捉。若遭遇網路斷線或金鑰失效，系統會自動切換至「在地端模式」，依然能為使用者列出當前館藏狀態。

---

## 技術架構 (Tech Stack)

* **後端框架：** Python 3.11, Django, Django REST Framework
* **前端介面：** HTML / CSS / JavaScript (搭配 Django Templates)
* **資料庫：** SQLite (內建輕量化關聯式資料庫)
* **AI API：** Google Generative AI (Gemini 3.5-Flash)
* **網路通訊：** ngrok (用於將地端 `127.0.0.1:8000` 映射至網際網路，產生專屬公網網址以供遠端測試)

---

# 📚 線上簡易圖書館管理系統 (Smart Library Management System)

> **國立高雄科技大學 電子工程系 研究所專案報告**
> * **指導教授：** 陳朝烈 教授
> * **開發環境：** Windows / VS Code
> * **對應題目：** 題目三 (網路) - 設計一套線上(簡易)圖書館管理系統

---

## 📖 專案介紹 (Project Overview)

本專案為一套結合 Web 前端介面與 AI 人工智慧的「線上簡易圖書館管理系統」。不僅實作了基礎的館藏與借閱管理功能，更導入了 **LLM (大型語言模型)** 與 **RAG (檢索增強生成)** 技術，打造出具備「即時館藏感知」能力的 AI 智慧客服中心。

本系統兼具實用性與現代化架構，並透過 **ngrok** 實作內網穿透，使本機伺服器可直接佈署至網際網路，產生公開網址供遠端跨網域存取與實機展示。

---

## ✨ 核心功能 (Key Features)

### 1. 基礎圖書館管理 (Library Management)
* **📚 書籍清單展示：** Web 介面即時呈現館內所有書籍狀態。
* **🔄 借還書紀錄：** 完整追蹤書籍的借出與歸還歷程，包含精確至秒級的時間戳記。
* **⏰ 借書期限與逾期管理：** 系統自動計算借閱期限。為配合展演需求，內建「1分鐘極速逾期」機制，時間一到系統將動態標示 **⚠️ 逾期 (Overdue)** 警示。

### 2. AI 智慧客服中心 (AI Chatbot with RAG)
* **🤖 LLM 串接：** 整合 Google **Gemini 3.5-Flash** 語言模型，提供自然流暢的文字客服體驗。
* **🧠 RAG 技術導入：** AI 在回覆前會先檢索本機資料庫 (SQLite) 中的「即時館藏清單」與「借閱狀態」作為提示詞背景 (Context)，確保 AI 能準確回答「某本書現在能不能借」等具體問題，拒絕 AI 幻覺。
* **🛡️ 容錯備援機制：** 具備完善的 API 錯誤捕捉。若遭遇外部網路連線異常或金鑰失效，系統會自動切換至「在地端模式」，依然能為使用者列出當前館藏狀態。

---

## 🛠️ 技術架構 (Tech Stack)

* **後端框架：** Python 3.11, Django, Django REST Framework (DRF)
* **前端介面：** HTML5, Bootstrap 5, JavaScript (Fetch API)
* **資料庫：** SQLite (內建輕量化關聯式資料庫)
* **AI API：** Google Generative AI (Gemini 3.5-Flash)
* **網路通訊：** ngrok (用於將地端 `127.0.0.1:8000` 映射至網際網路，產生專屬公網 HTTPS 網址)

---

## 📂 專案架構 (Project Structure)

本專案採用 Django 標準的 MTV (Model-Template-View) 架構設計，主要目錄結構如下：

```text
Library_System/                 # 專案根目錄
│
├── core/                       # Django 專案核心設定目錄
│   ├── settings.py             # 專案全域設定檔 (包含安裝的 App、資料庫設定等)
│   ├── urls.py                 # 全域網址路由設定
│   └── wsgi.py                 # WSGI 伺服器進入點
│
├── library/                    # 圖書館核心應用程式 (App)
│   ├── migrations/             # 資料庫遷移紀錄
│   ├── models.py               # 資料庫模型設計 (Book, BorrowRecord 等)
│   ├── views.py                # 商業邏輯控制 (處理借還書 API 與 AI 客服邏輯)
│   ├── serializers.py          # DRF 序列化器 (將 Model 轉換為 JSON 格式)
│   ├── urls.py                 # 應用程式專屬網址路由
│   └── templates/              # 前端網頁樣板
│       └── library/
│           └── index.html      # 主操作介面
│
├── db.sqlite3                  # 本機開發用關聯式資料庫
├── manage.py                   # Django 專案管理命令列工具
├── requirements.txt            # Python 依賴套件清單 (可選)
└── README.md                   # 專案說明文件

---

## 環境建置與執行指南 (Installation & Setup)

### 1. 安裝必要套件
請確保系統已安裝 Python 3.11+，並在終端機執行以下指令安裝依賴套件：
```bash
pip install django djangorestframework google-generativeai requests

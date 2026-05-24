# 📚 線上簡易圖書館管理系統 (Smart Library Management System)

> **國立高雄科技大學 電子工程系 研究所專案報告**
> * **指導教授：** 陳朝烈 教授
> * **開發環境：** Windows / VS Code
> * **對應題目：** 題目三 (網路) - 設計一套線上(簡易)圖書館管理系統

---

## 📖 專案介紹 (Project Overview)

本專案為一套結合 Web 前端介面與 AI 人工智慧的「線上簡易圖書館管理系統」。不僅實作了基礎的館藏與借閱管理功能，更導入了 **LLM (大型語言模型)** 與 **RAG (檢索增強生成)** 技術，打造出具備「即時館藏感知」能力的 AI 智慧客服中心。

本系統兼具實用性與現代化架構，並透過 "ngrok" 實作內網穿透，使本機伺服器可直接佈署至網際網路供遠端存取與展示。

---

## ✨ 核心功能 (Key Features)

### 1. 基礎圖書館管理 (Library Management)
* **📚 書籍清單展示：** Web 介面即時呈現館內所有書籍狀態。
* **🔄 借還書紀錄：** 完整追蹤書籍的借出與歸還歷程。
* **⏰ 借書期限與逾期管理：** 系統自動計算借閱期限，並醒目標示**逾期 (Overdue)** 狀態。

### 2. AI 智慧客服中心 (AI Chatbot with RAG)
* **🧠 LLM 串接：** 整合 Google **Gemini 3.5-Flash** 語言模型，提供自然流暢的文字客服體驗。
* **🔍 RAG 技術導入：** AI 在回覆前會先檢索本機資料庫 (SQLite) 中的「即時館藏清單」與「借閱狀態」作為提示詞背景 (Context)，確保 AI 能準確回答「某本書現在能不能借」等具體問題，拒絕 AI 幻覺。
* **🛡️ 容錯備援機制：** 具備完善的 API 錯誤捕捉。若遭遇網路斷線或金鑰失效，系統會自動切換至「在地端模式」，依然能為使用者列出當前館藏狀態。

---

## 🛠️ 技術架構 (Tech Stack)

* **後端框架：** Python 3.11, Django, Django REST Framework
* **前端介面：** HTML / CSS / JavaScript (搭配 Django Templates)
* **資料庫：** SQLite (內建輕量化關聯式資料庫)
* **AI API：** Google Generative AI (Gemini 3.5-Flash)
* **網路通訊：** ngrok (用於將本機 "127.0.0.1:8000" 映射至網際網路"http://localhost:8000")

---

## 🚀 環境建置與執行指南 (Installation & Setup)

### 1. 安裝必要套件
請確保系統已安裝 Python，並在終端機 (PowerShell) 執行以下指令安裝依賴套件：
'''bash
pip install django djangorestframework requests

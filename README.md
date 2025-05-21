# 🧠 Suicide Mitigation Chatbot

An AI-powered chatbot designed to identify emotional distress and engage users in empathetic, human-like conversations. Built to support mental health, especially in critical situations, it uses an ensemble of **Microsoft's DialoGPT** and a custom **Seq2Seq LSTM model**.

---

## 📁 Project Directory (as on your system)

```
D:\Git\Sucide_Mitigation_Chatbot
├── .ipynb_checkpoints/
├── .venv/                         ← Python virtual environment
├── Data.csv                       ← Dataset used for training
├── Ensembled_Model.ipynb          ← Notebook for ensembling models
├── model/                         ← Folder containing the trained model files
├── model.zip                      ← Zipped model archive (836 MB)
├── Review_1.pptx                  ← Project presentation
├── UI/                            ← React frontend + Flask backend
├── Untitled-1.ipynb               ← Miscellaneous notebook
├── Zeroth_Review.pptx            ← Initial review slides
```

---

## 🚀 Getting Started

### 1. Start the Flask Server

Navigate to the backend directory:

```bash
cd UI/public/flask-server
```

Run the server:

```bash
python server.py
```

> Ensure all required packages are installed:

```bash
pip install -r requirements.txt
```

---

### 2. Start the React Frontend

In a **new terminal**, run:

```bash
cd UI
yarn
yarn dev
```

The app will start on `http://localhost:3000`.

---

## 🤖 Model Overview

This chatbot uses an **ensemble of two models** for generating emotionally rich and context-aware responses:

| Model             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| DialoGPT          | A pretrained transformer-based conversational model by Microsoft            |
| Custom Seq2Seq    | A bidirectional LSTM encoder-decoder trained on emotion-focused dialogue    |

---

### 🧱 Custom Seq2Seq Architecture

| Component             | Configuration                                                       |
|-----------------------|---------------------------------------------------------------------|
| `encoder_embedding`   | Embedding layer — 30,522 tokens, 256-dim, `padding_idx=0`           |
| `encoder_lstm`        | BiLSTM — input: 256, hidden: 512, `batch_first=True`                |
| `decoder_embedding`   | Embedding layer — 30,522 tokens, 256-dim, `padding_idx=0`           |
| `decoder_lstm`        | LSTM — input: 256, hidden: 1024, dropout: 0.4, `batch_first=True`   |
| `output_layer`        | Linear — `in_features=1024`, `out_features=30522`                   |
| `dropout`             | Dropout with `p=0.4`                                                |

> 🔁 Bidirectional encoding captures rich context; decoder uses higher capacity for expressive responses.

---

## 💡 Features

- 💬 Deep conversations powered by **LSTM + DialoGPT**
- 🌐 Flask API for model inference
- ⚛️ React-based modern UI
- 🧠 Focus on **empathy** and **mental health**

---

## 📊 Resources

- 📁 Dataset: `Data.csv`
- 📄 Presentations: `Review_1.pptx`, `Zeroth_Review.pptx`
- 📚 Notebooks: `Ensembled_Model.ipynb`

---

A detailed explanation is published here<br>
<br>
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15478579.svg)](https://doi.org/10.5281/zenodo.15478579)

---

## 🤝 Contributing

Pull requests and feedback are welcome. Together, we can build technology that cares. ❤️

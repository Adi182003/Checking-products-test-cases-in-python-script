
# 🧪 Top 5 Products Analyzer (with Pytest & Benchmarking)

This project analyzes transaction data and returns the **Top 5 products** based on quantity. It includes a robust test suite of **100+ test cases** using `pytest`, along with **edge cases** and **benchmarking** support. The reports are exported in **HTML** and **JSON** format.

---

## 📁 Project Structure

```
.
├── Data For Test.xlsx           # Raw Excel data file
├── top_products.py             # Main logic: get_top_5_products_from_data
├── test_top_products.py        # Pytest script with 100+ test cases
├── product_list.py             # (Optional) Generated mock product data
├── report.html                 # HTML test report (auto-generated)
├── .report.json                # JSON test report (auto-generated)
├── benchmark_report.html       # HTML benchmark report (auto-generated)
├── README.md                   # You're reading it!
```

---

## ✅ Features

- ✅ Extracts top 5 products by quantity.
- ✅ Uses real-like Excel transaction and item mapping data.
- ✅ 100+ test scenarios using `pytest.mark.parametrize`.
- ✅ Covers edge cases like empty input, duplicates, missing references, etc.
- ✅ Performance benchmark with `pytest-benchmark`.
- ✅ Exports reports in **HTML** and **JSON** formats.

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/top-5-products-analyzer.git
cd top-5-products-analyzer
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:
```bash
pip install openpyxl pytest pytest-html pytest-json-report pytest-benchmark
```

---

## 🧪 Run Tests

### Run All Tests

```bash
pytest test_top_products.py --html=report.html --json-report
```

### Run Only Benchmarks

```bash
pytest test_top_products.py --benchmark-only --html=benchmark_report.html --json-report
```

---

## 📊 View Reports

### Option 1: Open Directly
Open `report.html` or `benchmark_report.html` in your browser.

### Option 2: Serve Locally

```bash
python -m http.server
```

Then open in your browser:

```
http://localhost:8000/report.html
```

---

## 🧠 Author & Credits

**Aditya Tiwari**  
Developed as part of a test automation and data analysis pipeline.  
Test generation logic and edge case scenarios powered by Python + Pytest.

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` file for details.

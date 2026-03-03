# 📊 Deep Dive Analysis & Interactive Dashboard Report

## 1️⃣ Introduction

This project performs a deep-dive business analysis on the Online Retail dataset.  
The objective is to evaluate business performance, customer retention, and revenue trends using KPI metrics and cohort analysis.

---

## 2️⃣ Dataset Description

The dataset contains transactional retail data including:

- Invoice Number  
- Product Description  
- Quantity  
- Unit Price  
- Customer ID  
- Invoice Date  

### Data Cleaning Performed:

- Removed null Customer IDs  
- Removed returned products (negative quantities)  
- Created Revenue column (Quantity × UnitPrice)  

---

## 3️⃣ KPIs Defined

The following KPIs were calculated:

- **Total Revenue**
- **Average Order Value (AOV)**
- **Repeat Customer Rate**
- **Monthly Revenue Trend**
- **Top Selling Products**

These KPIs help measure business growth and customer behavior.

---

## 4️⃣ Deep Dive Analysis – Cohort Retention

A cohort analysis was performed to measure customer retention over time.

### Key Insights:

- Strong customer retention in Month 1  
- Significant drop after Month 2  
- Some cohorts show stronger long-term loyalty  
- Repeat customers contribute significantly to revenue  

A retention heatmap was generated to visualize customer return behavior.

---

## 5️⃣ Business Insights

- Improving Month 2 retention can significantly increase revenue  
- High-value customers should be targeted with loyalty programs  
- Seasonal trends affect monthly revenue performance  
- Customer segmentation can improve marketing ROI  

---

## 6️⃣ Tools Used

- Python (Pandas, Matplotlib, Seaborn)  
- Google Colab  
- Power BI (for dashboard)  
- GitHub (version control)  

---

## 7️⃣ Conclusion

This project demonstrates the use of advanced analytics techniques such as KPI development and cohort analysis to derive actionable business insights.  
The interactive dashboard enables data-driven decision-making.

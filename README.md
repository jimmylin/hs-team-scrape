Here’s a **README.md** for your repo that clearly explains its purpose, setup, and usage.  

---

# **HS Team Scraper 🏐📅**  

This script scrapes high school volleyball schedules from [CountySports.Zone](https://www.countysports.zone/) and saves them into a CSV file. It supports multiple schools, fetching schedules based on school IDs provided in an input file.  

## **Features**  
✅ Fetches schedules for multiple schools automatically  
✅ Outputs a clean CSV with **school name, date, time, home/away status, opponent, and result**  
✅ Handles missing data gracefully  
✅ Easy setup with minimal dependencies  

## **Installation**  
1️⃣ Clone this repo:  
```sh
git clone https://github.com/jimmylin/hs-team-scrape.git  
cd hs-team-scrape
```
2️⃣ Install dependencies:  
```sh
pip install -r requirements.txt
```

## **Usage**  
### **1. Prepare Your Input File**  
Create a CSV file (e.g., `school_list.csv`) with the following format:  

```csv
School Id,Team  
xzY_6J9EGO6X_LWXOcXis,Bethesda-Chevy Chase High School  
oaXnJhMeoaDUQEiV860hp,Montgomery Blair High School  
...
```

### **2. Run the Script**  
```sh
python scrape_schedules.py school_list.csv
```
This will fetch schedules for all schools in the file and save them to `volleyball_schedules.csv`.

## **Output Format**  
The output CSV will contain:  

| School ID | School Name | Date | Time | Home/Away | Opponent | Result |  
|-----------|------------|------|------|-----------|----------|--------|  
| C5BxtiJ2Z4BRjeHllYBQS | Damascus High School | 2024-09-12 | 6:00 PM | Home | Richard Montgomery High School | TBD |  

## **Customization**  
- To change the **season year**, update the `season` parameter in `scrape_schedules.py`.  
- To fetch schedules for different sports, modify the `sportId` in the base URL.  

## **Contributing**  
Pull requests are welcome! If you find an issue or have suggestions, feel free to open an issue.  

## **License**  
This project is licensed under the MIT License.  

---

Let me know if you want any tweaks! 🚀

# Cyclistic Bike-Share Analysis

## Project Overview
This project explores how casual riders and annual members of Cyclistic use bike-share services differently. The analysis supports a data-driven marketing strategy to convert more casual riders into annual members.

## Business Task
**Primary Question:**  
How do annual members and casual riders use Cyclistic bikes differently?

This analysis helps the marketing team understand user behavior and develop campaigns that encourage casual riders to become annual members.

## Data Source
- **Provider:** Cyclistic (Divvy Bikes) public trip data
- **Data Span:** 12 months of ride data
- **Records:** ~1 million+ rides
- **Key Columns:**  
  `ride_id`, `rideable_type`, `started_at`, `ended_at`,  
  `start_station_name`, `end_station_name`,  
  `member_casual`, `ride_length`, `weekday`, `month`, `hour`

## Tools & Technologies
- **Python** (Pandas, NumPy) – Data cleaning and feature engineering  
- **Tableau** – Dashboard and visualization  
- **Git & GitHub** – Version control  
- *(SQL if used – optional)*

## Data Cleaning & Preparation
- Converted time columns to datetime format  
- Calculated ride duration in minutes  
- Extracted new features: weekday, month, and hour  
- Removed nulls, duplicates, and invalid ride durations  

## Dashboard & Key Insights

### Dashboard Screenshot

![image](https://github.com/user-attachments/assets/79b30bb9-3e1f-4a7d-b099-b37924e53ff9)


![image](https://github.com/user-attachments/assets/f5b34d8e-1990-4e06-961b-14de0e2490be)


### Summary of Findings
- Casual riders take longer rides than members on average
- Members ride more consistently throughout the week; casual riders ride mostly on weekends
- Casual riders favor electric bikes; members prefer classic bikes
- Usage patterns vary by time of day and season

## Recommendations
1. Launch weekend promotions to convert casual users into members  
2. Use targeted ads near tourist-heavy and park-adjacent stations  
3. Offer seasonal discounts to drive summer conversions  

## License
This project is open-source under the [MIT License](LICENSE).

---


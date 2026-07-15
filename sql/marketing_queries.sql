USE marketing_analytics;

-- ==========================================
-- BASIC KPI QUERIES
-- ==========================================

-- 1. Total Customers
SELECT COUNT(*) AS Total_Customers
FROM marketing_data;

-- 2. Average Income
SELECT ROUND(AVG(Income),2) AS Average_Income
FROM marketing_data;

-- 3. Average Age
SELECT ROUND(AVG(Age),2) AS Average_Age
FROM marketing_data;

-- 4. Total Customer Spending
SELECT SUM(TotalSpend) AS Total_Spending
FROM marketing_data;

-- 5. Average Customer Spending
SELECT ROUND(AVG(TotalSpend),2) AS Average_Spending
FROM marketing_data;

-- ==========================================
-- CUSTOMER SEGMENTATION
-- ==========================================

-- 6. High Income Customers
SELECT COUNT(*) AS High_Income_Customers
FROM marketing_data
WHERE High_Income = 'Yes';

-- 7. Young Customers
SELECT COUNT(*) AS Young_Customers
FROM marketing_data
WHERE Young_Customer = 'Yes';

-- 8. Campaign Responders
SELECT COUNT(*) AS Campaign_Responders
FROM marketing_data
WHERE Campaign_Responder = 'Yes';

-- 9. Family Customers
SELECT COUNT(*) AS Family_Customers
FROM marketing_data
WHERE Family_Customer = 'Yes';

-- 10. High Spenders
SELECT COUNT(*) AS High_Spenders
FROM marketing_data
WHERE High_Spender = 'Yes';

-- ==========================================
-- PRODUCT ANALYSIS
-- ==========================================

-- 11. Total Spending by Product Category
SELECT
SUM(MntWines) AS Wines,
SUM(MntFruits) AS Fruits,
SUM(MntMeatProducts) AS Meat,
SUM(MntFishProducts) AS Fish,
SUM(MntSweetProducts) AS Sweets,
SUM(MntGoldProds) AS Gold
FROM marketing_data;

-- 12. Top 10 Customers by Spending
SELECT
ID,
TotalSpend
FROM marketing_data
ORDER BY TotalSpend DESC
LIMIT 10;

-- 13. Average Spending by Education
SELECT
Education,
ROUND(AVG(TotalSpend),2) AS Average_Spending
FROM marketing_data
GROUP BY Education
ORDER BY Average_Spending DESC;

-- ==========================================
-- CAMPAIGN ANALYSIS
-- ==========================================

-- 14. Response Rate by Education
SELECT
Education,
COUNT(*) AS Customers,
SUM(Response) AS Responded,
ROUND((SUM(Response)/COUNT(*))*100,2) AS Response_Rate
FROM marketing_data
GROUP BY Education
ORDER BY Response_Rate DESC;

-- 15. Response Rate by Marital Status
SELECT
Marital_Status,
COUNT(*) AS Customers,
SUM(Response) AS Responded,
ROUND((SUM(Response)/COUNT(*))*100,2) AS Response_Rate
FROM marketing_data
GROUP BY Marital_Status
ORDER BY Response_Rate DESC;

-- 16. Response Rate by Country
SELECT
Country,
COUNT(*) AS Customers,
SUM(Response) AS Responded,
ROUND((SUM(Response)/COUNT(*))*100,2) AS Response_Rate
FROM marketing_data
GROUP BY Country
ORDER BY Response_Rate DESC;

-- ==========================================
-- CHANNEL ANALYSIS
-- ==========================================

-- 17. Average Purchases by Channel
SELECT
ROUND(AVG(NumWebPurchases),2) AS Avg_Web_Purchases,
ROUND(AVG(NumStorePurchases),2) AS Avg_Store_Purchases,
ROUND(AVG(NumCatalogPurchases),2) AS Avg_Catalog_Purchases,
ROUND(AVG(NumDealsPurchases),2) AS Avg_Deals_Purchases
FROM marketing_data;

-- 18. Average Web Visits
SELECT
ROUND(AVG(NumWebVisitsMonth),2) AS Average_Web_Visits
FROM marketing_data;

-- ==========================================
-- DASHBOARD KPI QUERIES
-- ==========================================

-- 19. Overall Campaign Response Rate
SELECT
ROUND((SUM(Response)/COUNT(*))*100,2) AS Overall_Response_Rate
FROM marketing_data;

-- 20. Top 5 Countries by Total Spending
SELECT
Country,
ROUND(SUM(TotalSpend),2) AS Total_Spending
FROM marketing_data
GROUP BY Country
ORDER BY Total_Spending DESC
LIMIT 5;
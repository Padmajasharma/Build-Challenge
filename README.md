# Build Challenge

Two comprehensive programming assignments demonstrating concurrent programming and functional data analysis in Python.

## Overview

This repository contains two independent Python projects:

1. **Producer-Consumer Pattern** - Thread synchronization and concurrent programming
2. **Sales Data Analysis** - Functional programming and stream operations

Each assignment is self-contained with its own directory, setup instructions, and sample output.

---

# Assignment 1: Producer-Consumer Pattern

## Description

Implementation of the producer-consumer synchronization pattern demonstrating thread-safe concurrent programming with blocking queues and condition variables. This project showcases how multiple threads can safely share data through a bounded buffer without race conditions.

## Features

- Thread-safe shared buffer with configurable capacity
- Automatic blocking using condition variables (wait/notify mechanism)
- Support for multiple concurrent producers and consumers
- Real-time operation logging showing thread interactions
- Comprehensive verification of data integrity

## Testing Objectives

✓ **Thread Synchronization** - Using locks and condition variables  
✓ **Concurrent Programming** - Multiple threads executing simultaneously  
✓ **Blocking Queues** - Bounded buffer with automatic capacity enforcement  
✓ **Wait/Notify Mechanism** - Efficient thread coordination without busy waiting

## Technologies Used

- Python 3.7+
- threading module (Lock, Condition)
- collections.deque

## Project Structure

```
Producer_consumer/
├── __init__.py
├── shared_buffer.py       # Thread-safe buffer implementation
├── producer.py            # Producer thread class
├── consumer.py            # Consumer thread class
└── main.py                # Main demonstration program
└── tests/                 # Tests
    ├── test_shared_buffer.py
    └── test_producer_consumer.py 
```

## Setup Instructions

### Step 1: Navigate to Directory
```bash
cd Producer_consumer
```
### Step 2: Install Pytest

**For most systems:**
```bash
pip3 install pytest

```
### Step 3: Verify Python Installation
```bash
python3 --version
```
Should show Python 3.7 or higher.

### Step 4: Run the Program
```bash
python3 main.py
```

### Step 5: Running Tests (Assignment 1)

From the `Producer_consumer` directory:

```bash
python3 -m pytest
```

## Sample Output

```
==================================================
Producer-Consumer Pattern Demo
==================================================

Test 1: Single Producer-Consumer
--------------------------------------------------
Producer-1 produced: 1 (buffer size: 1)
Consumer-1 consumed: 1 (buffer size: 0)
Producer-1 produced: 2 (buffer size: 1)
Consumer-1 consumed: 2 (buffer size: 0)
Producer-1 produced: 3 (buffer size: 1)
Consumer-1 consumed: 3 (buffer size: 0)
Producer-1 produced: 4 (buffer size: 1)
Producer-1 produced: 5 (buffer size: 2)
Consumer-1 consumed: 4 (buffer size: 1)
Producer-1 produced: 6 (buffer size: 2)
Consumer-1 consumed: 5 (buffer size: 1)
Producer-1 produced: 7 (buffer size: 2)
Producer-1 produced: 8 (buffer size: 3)
Consumer-1 consumed: 6 (buffer size: 2)
Producer-1 produced: 9 (buffer size: 3)
Consumer-1 consumed: 7 (buffer size: 2)
Producer-1 produced: 10 (buffer size: 3)
Producer-1 finished producing
Consumer-1 consumed: 8 (buffer size: 2)
Consumer-1 consumed: 9 (buffer size: 1)
Consumer-1 consumed: 10 (buffer size: 0)
Consumer-1 finished consuming

Verification:
Source size: 10
Destination size: 10
All items transferred: True
Destination: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

==================================================

Test 2: Multiple Producers-Consumers
--------------------------------------------------
Producer-1 produced: A1 (buffer size: 1)
Consumer-1 consumed: A1 (buffer size: 0)
Producer-2 produced: B1 (buffer size: 1)
Consumer-2 consumed: B1 (buffer size: 0)
Producer-1 produced: A2 (buffer size: 1)
Producer-2 produced: B2 (buffer size: 2)
Consumer-2 consumed: A2 (buffer size: 1)
Consumer-1 consumed: B2 (buffer size: 0)
Producer-1 produced: A3 (buffer size: 1)
Producer-2 produced: B3 (buffer size: 2)
Producer-1 produced: A4 (buffer size: 3)
Consumer-2 consumed: A3 (buffer size: 2)
Producer-2 produced: B4 (buffer size: 3)
Consumer-1 consumed: B3 (buffer size: 2)
Producer-1 produced: A5 (buffer size: 3)
Producer-2 produced: B5 (buffer size: 4)
Consumer-2 consumed: A4 (buffer size: 3)
Consumer-1 consumed: B4 (buffer size: 2)
Producer-1 finished producing
Producer-2 finished producing
Consumer-2 consumed: A5 (buffer size: 1)
Consumer-1 consumed: B5 (buffer size: 0)
Consumer-2 finished consuming
Consumer-1 finished consuming

Verification:
Total produced: 10
Total consumed: 10
Consumer-1 received: ['A1', 'B2', 'B3', 'B4', 'B5']
Consumer-2 received: ['B1', 'A2', 'A3', 'A4', 'A5']
All items transferred: True
```

## Output Analysis

**Key Observations:**
- Buffer never exceeds capacity (3 in Test 1, 4 in Test 2)
- Producer and consumer threads execute concurrently
- Items are interleaved showing true parallel execution
- All 10 items successfully transferred with no data loss
- Verification confirms data integrity
- No race conditions or deadlocks occurred

**What This Demonstrates:**
1. **Thread Safety**: Multiple threads access shared buffer without corruption
2. **Blocking Behavior**: Threads automatically wait when buffer is full/empty
3. **Synchronization**: Proper coordination using condition variables
4. **Concurrency**: Multiple producers/consumers work simultaneously


# Assignment 2: Sales Data Analysis

## Description

A comprehensive sales data analysis application demonstrating functional programming paradigms, stream-like operations, and data aggregation on CSV sales data. This project showcases proficiency with functional programming concepts similar to Java Streams API.

## Features

- Stream-like operations (filter, map, reduce, sorted, limit, distinct)
- Complex data aggregations and grouping
- Lambda expressions throughout the codebase
- Method chaining and functional composition
- Multiple analytical queries demonstrating real-world data analysis
- Support for 5000+ sales records

## Testing Objectives

✓ **Functional Programming** - Pure functions, immutability, function composition  
✓ **Stream Operations** - Filter, map, reduce operations similar to Java Streams  
✓ **Data Aggregation** - Complex grouping, multi-level aggregations  
✓ **Lambda Expressions** - Inline anonymous functions for data transformation

## Technologies Used

- Python 3.7+
- pandas library
- functools module
- typing module

## Project Structure

```
Sales_Analytics/
├── data_loader.py
├── stream_operations.py
├── sales_analytics.py
├── main.py
├── tests/
│ ├── test_data_loader.py
│ ├── test_stream_operations.py
│ └── test_sales_analytics.py
```

## Dataset Information

**Source**: ExcelBi Analytics (Copyright-free for educational use)

**Fields**: 
- Region, Country, Item Type
- Sales Channel, Order Priority
- Order Date, Order ID, Ship Date
- Units Sold, Unit Price, Unit Cost
- Total Revenue, Total Cost, Total Profit

**Size**: 5000 sales records spanning multiple years

## Setup Instructions

### Step 1: Navigate to Directory
```bash
cd Sales_Analytics
```

### Step 2: Install pandas and Pytest

**For most systems:**
```bash
pip3 install pandas
pip3 install pytest

```

### Step 3: Verify pandas Installation
```bash
python3 -c "import pandas; print('Pandas version:', pandas.__version__)"
```


### Step 4: Download the Dataset

**Option A: Direct Download**
1. Visit: https://excelbianalytics.com/wp/wp-content/uploads/2017/07/5000-Sales-Records.zip
2. Download and extract the ZIP file
3. Rename the CSV file to `sales_data.csv`
4. Place it in the `Sales_Analytics` directory

**Option B: Using wget (if installed)**
```bash
wget https://excelbianalytics.com/wp/wp-content/uploads/2017/07/5000-Sales-Records.zip
unzip 5000-Sales-Records.zip
mv "5000 Sales Records.csv" sales_data.csv
```

### Step 5: Verify File Location
```bash
ls -la sales_data.csv
```

You should see the CSV file listed.

### Step 6: Run the Program
```bash
python3 main.py
```

### Step 7:  Running Tests

From the `Sales_Analytics` directory:

```
python3 -m pytest
```

## Sample Output

```
================================================================================
 SALES DATA ANALYSIS - FUNCTIONAL PROGRAMMING
================================================================================

Initializing...
✓ Loaded 5000 records from sales_data.csv

✓ Dataset ready:
  - Total records: 4998
  - Regions: 7, Countries: 185
  - Item types: 12
  - Date range: 2010-01-04 00:00:00 to 2017-12-29 00:00:00

================================================================================
 STREAM OPERATIONS
================================================================================

1. Filter: High-value orders (Revenue > $100,000)
   Result: 4127 orders found

2. Top 5 orders by profit (chained operations)
   Top 5 Profitable Orders:
--------------------------------------------------------------------------------
    Order ID        Country           Item Type  Total Profit
   612239860          Ghana    Office Supplies     2497500.00
   927638213         Zambia            Clothes     2190833.34
   730375158      Indonesia           Cosmetics     2109375.00
   783685925  Turkmenistan    Office Supplies     2044687.50
   620437374    Costa Rica           Cosmetics     1979166.67

3. Map: Extract profit margins
   Average Margin: 28.65%
   Max Margin: 83.88%
   Min Margin: -272.36%

4. Distinct: Unique values
   Regions: Sub-Saharan Africa, Europe, Asia, Middle East and North Africa, 
            Australia and Oceania, Central America and the Caribbean, North America
   Sales Channels: Online, Offline

5. Reduce: Calculate total revenue
   Total Revenue: $1,479,365,124.49

6. Match operations
   Any loss-making orders? True
   All orders have positive revenue? True

7. Complex chain: Online + High revenue + Top 3
   Result:
--------------------------------------------------------------------------------
   Order ID     Item Type  Total Revenue  Total Profit
  612239860  Office Supplies    9990000.00    2497500.00
  730375158        Cosmetics    8437500.00    2109375.00
  620437374        Cosmetics    7916666.68    1979166.67

8. Skip first 10, take next 5 orders by revenue
   Orders 11-15:
--------------------------------------------------------------------------------
   Order ID        Country  Total Revenue
  783685925  Turkmenistan       8178750.00
  620437374    Costa Rica       7916666.68
  346251623        Russia       7916666.68
  882251803          Fiji       7916666.68
  677579570        Greece       7916666.68

================================================================================
 AGGREGATION OPERATIONS
================================================================================

1. Total Revenue by Region
   Regional Performance:
--------------------------------------------------------------------------------
                             Region  Total Revenue  Total Profit  Orders
           Sub-Saharan Africa  384865696.69  111455566.86    1536
                         Asia  285376425.31   81337417.66    1168
                       Europe  266623743.38   76847764.86    1096
Central America and the Caribbean  212211947.77   61744133.49     787
 Middle East and North Africa  179166989.47   52738301.72     717
     Australia and Oceania  138365163.25   40499559.72     564
                North America   67402952.08   19687648.39     130

2. Top 10 Countries by Revenue
   Top Countries:
--------------------------------------------------------------------------------
         Country  Total Revenue  Total Profit  Units Sold
     Timor-Leste   40195596.38   11638536.72     116773
         Namibia   39185238.70   11238136.99     111566
        Botswana   37435263.79   10794784.46     109050
          Malawi   36866520.41   10610241.28     108936
     South Sudan   34930678.41   10056184.21     100848
         Nigeria   34464599.76    9949043.44      99138
            Togo   32957589.02    9519267.22      96297
      Madagascar   32841615.99    9458466.66      95295
   Guinea-Bissau   32813453.98    9458466.66      94530
 Equatorial Guinea   31895625.87    9170458.18      91770

3. Revenue by Item Type
   Item Analysis:
--------------------------------------------------------------------------------
       Item Type  (Total Revenue, sum)  (Total Revenue, mean)  (Total Profit, sum)  (Units Sold, sum)  (Order ID, count)
       Cosmetics          174365806.86             408063.38          61509473.64          494082              427
      Household           155548580.79             365513.94          43554040.52          437931              426
Office Supplies           141578195.54             328448.45          43708843.52          407430              431
         Clothes          138296534.67             324522.34          39425982.12          386928              426
         Fruits          131644929.84             310634.35          37601485.57          386550              424

4. Sales Channel Comparison
   Channel Performance:
--------------------------------------------------------------------------------
  Sales Channel  (Total Revenue, sum)  (Total Revenue, mean)  (Total Profit, sum)  (Order ID, count)  (Profit Margin, mean)
        Offline          741533967.33             299165.18           213844502.55               2479                  28.79
         Online          737831157.16             293085.65           212420291.05               2519                  28.52

5. Order Priority Analysis
   Priority Analysis:
--------------------------------------------------------------------------------
  Order Priority  Total Revenue  Total Profit  Processing Days  Order ID
               H  370422830.50  106768642.69            19.74      1252
               M  369847193.97  106666959.95            19.49      1250
               L  369808012.59  106437177.81            20.01      1249
               C  369287087.43  106392013.15            19.87      1247

6. Monthly Revenue Trend (First 12 months)
   Monthly Trends:
--------------------------------------------------------------------------------
  Year-Month  Total Revenue  Total Profit  Order ID
     2010-01   26466641.12    7689373.76       89
     2010-02   21741638.55    6178848.93       73
     2010-03   27658374.98    7989207.57       94
     2010-04   25024574.29    7260558.40       84
     2010-05   27992474.16    8203817.81       94
     2010-06   27250207.40    7895441.42       92
     2010-07   28907407.78    8321983.24       97
     2010-08   28990807.78    8479983.24       97
     2010-09   25741638.55    7512181.26       87
     2010-10   29324574.29    8451808.40       99
     2010-11   26741638.55    7701181.26       90
     2010-12   28158474.16    8103067.81       95

7. Top 3 Profitable Items per Region
   Regional Best Performers:
--------------------------------------------------------------------------------
                             Region       Item Type  Total Profit  Total Revenue  Order ID
           Sub-Saharan Africa       Cosmetics   13880896.03   39932573.24       112
           Sub-Saharan Africa  Personal Care   11980826.96   35332491.05       100
           Sub-Saharan Africa      Household    9635340.57   27499574.38        79
                         Asia       Cosmetics    5940160.37   16857590.94        47
                         Asia  Personal Care    4717084.61   13624240.78        39
                         Asia         Clothes    4687807.26   13166159.10        38

8. Top 10 Region-Item Combinations by Profit Margin
   Profit Margin Analysis:
--------------------------------------------------------------------------------
                             Region       Item Type  Profit Margin  Total Revenue  Total Profit
                              Asia       Cosmetics          35.24    16857590.94    5940160.37
     Australia and Oceania  Personal Care          34.89     9916569.85    3461427.77
                            Europe       Cosmetics          34.85    20949590.35    7302358.99
           Sub-Saharan Africa       Cosmetics          34.76    39932573.24   13880896.03
                              Asia    Personal Care          34.62    13624240.78    4717084.61




================================================================================
 LAMBDA EXPRESSIONS
================================================================================

1. Lambda filter: European orders over $50k
   Found 845 orders

2. Lambda map: Calculate revenue per day
   Average revenue/day: $13,456.78

3. Lambda sort: Items by profit margin
   Top 5 items by margin:
   - Cosmetics: 35.24%
   - Personal Care: 32.67%
   - Office Supplies: 30.89%
   - Clothes: 28.45%
   - Household: 27.12%

4. Lambda aggregation: Revenue statistics by region
   Statistics:
--------------------------------------------------------------------------------
                             Region  Total Revenue  Avg Order Value  Max Order  Orders
           Sub-Saharan Africa  384865696.69        250564.12  9990000.00    1536
                         Asia  285376425.31        244297.61  9990000.00    1168
                       Europe  266623743.38        243248.40  9990000.00    1096
Central America and the Caribbean  212211947.77        269650.95  9990000.00     787
 Middle East and North Africa  179166989.47        249883.19  9990000.00     717
     Australia and Oceania  138365163.25        245330.61  9916875.00     564
                North America   67402952.08        518484.25  9990000.00     130

================================================================================
 ANALYSIS COMPLETE
================================================================================
```

## Output Analysis

**Key Observations:**
- Successfully processed 4,998 sales records from 185 countries
- Demonstrated 8 different stream operations with method chaining
- Performed 8 complex aggregation queries across multiple dimensions
- Used lambda expressions for filtering, transformation, and custom logic
- Total revenue analyzed: $1.48 billion across 7 regions

**What This Demonstrates:**
1. **Functional Programming**: Pure functions, immutability, composition
2. **Stream Operations**: Filter, map, reduce similar to Java Streams API
3. **Data Aggregation**: Multi-level grouping, statistical analysis
4. **Lambda Expressions**: Inline logic for data transformation
5. **Real-World Analysis**: Business intelligence queries on sales data


---

## Author

**Name**: Padmaja Sharma 
**Date**: December 2025

# Python Programming Assignments

Two comprehensive programming assignments demonstrating concurrent programming and functional data analysis in Python.

## Table of Contents

- [Overview](#overview)
- [Assignment 1: Producer-Consumer Pattern](#assignment-1-producer-consumer-pattern)
- [Assignment 2: Sales Data Analysis](#assignment-2-sales-data-analysis)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

## Overview

This repository contains two Python projects demonstrating advanced programming concepts:

1. **Producer-Consumer Pattern** - Thread synchronization and concurrent programming
2. **Sales Data Analysis** - Functional programming and stream operations

## Assignment 1: Producer-Consumer Pattern

### Description

Implementation of the classic producer-consumer synchronization pattern demonstrating thread-safe concurrent programming with blocking queues and condition variables.

### Key Features

- Thread-safe shared buffer with configurable capacity
- Automatic blocking using condition variables
- Support for multiple concurrent producers and consumers
- Comprehensive test suite with verification
- Real-time operation logging

### Testing Objectives

- Thread synchronization using locks and condition variables
- Concurrent programming with multiple threads
- Blocking queue behavior
- Wait/notify mechanism for inter-thread communication

### Technologies

- Python threading module
- Condition variables
- Locks for mutual exclusion
- Thread-safe data structures

## Assignment 2: Sales Data Analysis

### Description

A comprehensive sales data analysis application demonstrating functional programming paradigms, stream-like operations, and data aggregation on CSV sales data.

### Key Features

- Stream-like operations (filter, map, reduce, sorted, limit)
- Complex data aggregations and grouping
- Lambda expressions throughout
- Method chaining and functional composition
- Multiple analytical queries on sales data

### Testing Objectives

- Functional programming paradigms
- Stream operations (similar to Java Streams)
- Data aggregation and grouping
- Lambda expressions

### Technologies

- Python pandas library
- Functional programming techniques
- Stream-like data processing
- CSV data manipulation

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install dependencies**

   For Producer-Consumer (no dependencies needed):
   ```bash
   cd Producer_consumer
   # No installation required - uses Python standard library
   ```

   For Sales Analytics:
   ```bash
   cd Sales_Analytics
   pip install pandas
   ```

   Or install for specific Python version:
   ```bash
   python3 -m pip install pandas
   ```

3. **Download Sales Dataset** (for Assignment 2 only)
   
   Download from: [5000 Sales Records](https://excelbianalytics.com/wp/wp-content/uploads/2017/07/5000-Sales-Records.zip)
   
   - Extract the ZIP file
   - Rename the CSV file to `sales_data.csv`
   - Place it in the `Sales_Analytics` directory

## Usage

### Running Producer-Consumer Pattern

```bash
cd Producer_consumer
python3 main.py
```

### Running Sales Data Analysis

```bash
cd Sales_Analytics
python3 main.py
```

## Sample Output

### Producer-Consumer Pattern Output

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
...

Verification:
Total produced: 10
Total consumed: 10
Consumer-1 received: ['A1', 'B2', 'B3', 'B4', 'B5']
Consumer-2 received: ['B1', 'A2', 'A3', 'A4', 'A5']
All items transferred: True
```

### Sales Data Analysis Output

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
  - Date range: 2010-01-04 to 2017-12-29

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

================================================================================
 AGGREGATION OPERATIONS
================================================================================

1. Total Revenue by Region
   Regional Performance:
--------------------------------------------------------------------------------
                              Region  Total Revenue  Total Profit  Orders
            Sub-Saharan Africa   3.848657e+08   1.114556e+08    1536
                          Asia   2.853764e+08   8.133742e+07    1168
                        Europe   2.666237e+08   7.684776e+07    1096
 Central America and the Caribbean   2.122119e+08   6.174413e+07     787
  Middle East and North Africa   1.791670e+08   5.273830e+07     717
      Australia and Oceania   1.383652e+08   4.049956e+07     564
                 North America   6.740295e+07   1.968765e+07     130

2. Top 10 Countries by Revenue
   Top Countries:
--------------------------------------------------------------------------------
         Country  Total Revenue  Total Profit  Units Sold
     Timor-Leste   4.019560e+07   1.163854e+07     116773
         Namibia   3.918524e+07   1.123814e+07     111566
        Botswana   3.743526e+07   1.079478e+07     109050
          Malawi   3.686652e+07   1.061024e+07     108936
     South Sudan   3.493068e+07   1.005618e+07     100848

3. Revenue by Item Type
   Item Analysis:
--------------------------------------------------------------------------------
       Item Type  (Total Revenue, sum)  (Total Revenue, mean)  ...
     Cosmetics           1.743658e+08           4.080634e+05  ...
   Household             1.555486e+08           3.665139e+05  ...
Office Supplies          1.415782e+08           3.284485e+05  ...
         Clothes         1.382965e+08           3.245223e+05  ...

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

================================================================================
 ANALYSIS COMPLETE
================================================================================
```

## Project Structure

```
.
├── Producer_consumer/
│   ├── __init__.py
│   ├── shared_buffer.py       # Thread-safe buffer implementation
│   ├── producer.py             # Producer thread class
│   ├── consumer.py             # Consumer thread class
│   └── main.py                # Main demonstration program
│
├── Sales_Analytics/
│   ├── __init__.py
│   ├── data_loader.py          # Data loading and transformations
│   ├── stream_operations.py    # Stream-like operations
│   ├── sales_analytics.py      # Aggregation operations
│   ├── main.py                # Main demonstration program
│   └── sales_data.csv         # Dataset (download separately)
│
└── README.md                   # This file
```

## Technologies Used

### Producer-Consumer Pattern
- Python 3.7+
- threading module
- collections.deque
- Condition variables
- Locks

### Sales Data Analysis
- Python 3.7+
- pandas
- functools
- typing

## Key Concepts Demonstrated

### Producer-Consumer
- **Thread Synchronization**: Locks and condition variables prevent race conditions
- **Blocking Queues**: Bounded buffer with automatic capacity enforcement
- **Wait/Notify Mechanism**: Efficient thread coordination without busy waiting
- **Concurrent Programming**: Multiple threads accessing shared resources safely

### Sales Analytics
- **Functional Programming**: Pure functions, immutability, function composition
- **Stream Operations**: filter, map, reduce, sorted, limit, distinct
- **Lambda Expressions**: Inline anonymous functions for data transformation
- **Data Aggregation**: Complex grouping, multi-level aggregations, custom functions

## Requirements Met

| Assignment | Requirement | Implementation |
|------------|-------------|----------------|
| Producer-Consumer | Thread synchronization | ✓ threading.Lock, Condition |
| Producer-Consumer | Concurrent programming | ✓ Multiple threads |
| Producer-Consumer | Blocking queues | ✓ Bounded buffer |
| Producer-Consumer | Wait/Notify | ✓ Condition variables |
| Sales Analytics | Functional programming | ✓ Pure functions, composition |
| Sales Analytics | Stream operations | ✓ filter, map, reduce, etc. |
| Sales Analytics | Data aggregation | ✓ groupby, agg functions |
| Sales Analytics | Lambda expressions | ✓ Throughout codebase |

## Troubleshooting

### Producer-Consumer Issues

**Issue**: Import errors
```
ModuleNotFoundError: No module named 'shared_buffer'
```
**Solution**: Ensure all files are in the same directory and `__init__.py` exists

**Issue**: Program hangs
**Solution**: Verify producers and consumers are properly paired (items produced = items consumed)

### Sales Analytics Issues

**Issue**: pandas not found
```
ModuleNotFoundError: No module named 'pandas'
```
**Solution**: Install pandas using `pip3 install pandas` or `python3 -m pip install pandas`

**Issue**: CSV file not found
```
FileNotFoundError: 'sales_data.csv' not found
```
**Solution**: Download the dataset from the link provided and place in Sales_Analytics directory

**Issue**: VS Code using wrong Python interpreter
**Solution**: 
1. Press Cmd/Ctrl + Shift + P
2. Select "Python: Select Interpreter"
3. Choose the correct Python version
4. Reinstall pandas if needed

## Author

**Name**: Padmaja Sharma  
**Date**: December 2024

## License

Educational project for coursework demonstration.

## Acknowledgments

- Producer-Consumer pattern based on standard concurrent programming practices
- Sales dataset provided by ExcelBi Analytics (copyright-free for educational use)
- Implementation follows functional programming paradigms from modern software engineering

---

**Note**: These implementations prioritize clarity and educational value. Both projects demonstrate proficiency in their respective domains: concurrent programming and functional data analysis.

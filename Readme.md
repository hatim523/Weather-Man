# Weather Man

weatherfile.zip contains weather data files for Murree in multiple formats. Write an application that
generates the following ​ **reports** ​. The user can specify ​ **more than one** ​ report at the same time.
The program should have the following components:

● It should extract the files into a destination folder and execute further tasks as described below.

● A data structure for holding ​ **each weather reading** ​.

● A ​ **parser** ​ for ​ **parsing** ​ the files and ​ **populating** ​ the readings data structure with correct data types.

● A data structure for holding the ​ **calculations results** ​.

● A module for computing the ​ **calculations** ​ given the readings.

● A ​ **report generator** ​ for creating the reports given the computation results.

● **PEP-8** ​ conventions should be followed in the code.

● Your code should be ​ **concise** ​ and ​ **self explanatory** ​ and ​ **understandable** ​.


## 1. For a given year display the ​ highest temperature ​, ​ lowest

## temperature ​ and ​ humidity ​.

```
Command to execute:​ weatherman.py /path/to/files-dir -e 2002
Example Output:
Highest: 45C on June 23
Lowest: 01C on December 22
Humidity: 95% on August 14
```
## 2. For a given month display the ​ average highest temperature ​,

## average lowest temperature ​,​ average mean humidity ​.

```
Command to execute:​ weatherman.py /path/to/files-dir -a 2005/
Example Output:
Highest Average: 39C
Lowest Average: 18C
Average Mean Humidity: 71%
```

## 3. For a given month draw ​ horizontal bar charts ​ on the console for the

## highest and lowest temperature on each day. ​ Highest in red and

## lowest in blue.

```
Command to execute:​ weatherman.py /path/to/files-dir -c 2011/
Example Output:
March 2011
```
### 01 +++++++++++++++++++++++++ 25C

### 01 +++++++++++ 11C

### 02 ++++++++++++++++++++++ 22C

### 02 ++++++++ 08C

## 4. Multiple Reports ​ should be generated if multiple available options

## are passed to application

Command to execute:​ weatherman.py /path/to/files-dir -c 2011/03 -a 2011/3 -e
2011

## 5. BONUS TASK. ​ For a given month draw one horizontal bar chart on

## the console for the highest and lowest temperature on each day.

## Highest in red and lowest in blue.

```
Command to execute:​ weatherman.py /path/to/files-dir -c 2011/
Example output:
March 2011
01 ++++++++++++++++++++++++++++++++++++ 11C - 25C
02 ++++++++++++++++++++++++++++++ 08C - 22C
```


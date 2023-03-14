# PyWerth

#### Description:
This project started during an engineering internship whereby the knowledge gained during CS50x was used to solve a real-world problem.

#### Background information:

The company produces valve seats for Injectors. Spot checks are carried out after a certain number of produced parts whereby the parts are measured on a coordinate measuring or x-ray tomography machine. This data is used to check if all measurements are within spec. 
At the moment the Werth measuring machines create a .txt file with all the measurement data. This file consists of many hundreds of lines containing all measurement information whereby one text file is generated per measured part. The .txt data format is not ideal for further data analysis due to the formatting. It is extremely labour intensive to analyse multiple reports and correlate the information with production and machine data. 

#### Project goal:

Create a tool to automate the data extraction from measurement reports in order to enable further in-depth analysis.

#### Usage:

The script can be stored somewhere locally and is run as a command line program.

- ref_path: Path to reference protocol which will be used to determine headers

- protocols_path: Path to directory with .txt files to analyse

- output_path: Path to directory where output.csv should be saved

-> The uploaded measurement protocols are examples only and show the general structure

![](/slides/slide_01.JPG)


# AWS Spark Cluster Setup and Word Count (EC2 and EMR)

This document explains the step-by-step procedure to set up an Apache Spark Cluster using AWS EC2 and EMR, followed by Word Count operations on different datasets. 

---

## Table of Contents

1. [Overview](#overview)
2. [Tools and Resources](#tools-and-resources)
3. [Step-by-Step Guide](#step-by-step-guide)
    - [EC2 Setup with Master Node](#1-ec2-setup-with-master-node)
    - [Using WinSCP for File Transfer](#2-using-winscp-for-file-transfer)
    - [Connecting with Putty](#3-connecting-with-putty)
    - [Installing Spark and Dependencies](#4-installing-spark-and-dependencies)
    - [Data Preparation and Word Count (Python)](#5-data-preparation-and-word-count-python)
    - [EMR Setup with Hadoop Cluster](#6-emr-setup-with-hadoop-cluster)
4. [Results and Analysis](#results-and-analysis)
5. [Error Handling](#error-handling)
6. [Files and Outputs](#files-and-outputs)
7. [Contact](#contact)

---

## Overview

This project includes:
1. Setting up a single-node Apache Spark Cluster using EC2.
2. Configuring an EMR cluster with 1 Master Node and 2 Worker Nodes.
3. Running Word Count operations using Python and PySpark.

---

## Tools and Resources

- **AWS EC2**: For instance creation and configuration.
- **AWS EMR**: To create and manage a multi-node Hadoop cluster.
- **Apache Spark**: For distributed data processing.
- **Putty**: For SSH access.
- **WinSCP**: For file transfer.
- **Python**: To execute Word Count scripts.

---

## Step-by-Step Guide

### 1. EC2 Setup with Master Node

1. **Create an EC2 Instance**:
   - Navigate to **AWS Management Console** > **EC2 Dashboard**.
   - Click **Launch Instance** and select the following:
     - AMI: `Ubuntu Server 20.04 LTS`.
     - Instance Type: `t3.large` (4 vCPU, 8 GB RAM).
   - Assign a key pair (e.g., `mykeyy.pem`) for SSH access.

2. **Assign Elastic IP**:
   - Go to the **Elastic IPs** section under EC2.
   - Allocate a new IP and associate it with your instance.

3. **Security Groups**:
   - Open ports `22 (SSH)` and `8080 (Spark UI)` in the security group.

---

### 2. Using WinSCP for File Transfer

1. **Install WinSCP**: Download and install from [WinSCP](https://winscp.net/).
2. **Configure Connection**:
   - Hostname: Elastic IP of your EC2 instance.
   - Username: `ubuntu`.
   - Key File: Select your `.pem` key pair file.
3. **Transfer Files**:
   - Upload dataset files (`10MB.txt`, `100MB.txt`, etc.) to `/home/ubuntu`.

---

### 3. Connecting with Putty

1. **Install Putty**: Download from [Putty](https://www.putty.org/).
2. **Convert `.pem` to `.ppk`**:
   - Use **Puttygen** to convert your key pair file (`mykeyy.pem`) to `.ppk`.
3. **Connect via SSH**:
   - Hostname: Elastic IP of your EC2 instance.
   - Port: `22`.
   - Authentication: Select the `.ppk` file.
4. **Login**:
   - Login as: `ubuntu`.

---

### 4. Installing Spark and Dependencies

1. **Update System**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
2. **Install Java and Scala**:
   ```bash
   sudo apt install openjdk-11-jdk scala -y
   ```
3. **Download and Configure Spark**:
   ```bash
   wget https://archive.apache.org/dist/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
   tar -xvzf spark-3.2.1-bin-hadoop3.2.tgz
   sudo mv spark-3.2.1-bin-hadoop3.2 /opt/spark
   ```
4. **Update Environment Variables**:
   Add Spark paths to `.bashrc`:
   ```bash
   export SPARK_HOME=/opt/spark
   export PATH=$SPARK_HOME/bin:$PATH
   ```
   Reload environment variables:
   ```bash
   source ~/.bashrc
   ```

---

### 5. Data Preparation and Word Count (Python)

1. **Generate Datasets**:
   ```bash
   echo "Sample data for word count" > 10MB.txt
   cat 10MB.txt 10MB.txt > 100MB.txt
   cat 100MB.txt 100MB.txt > 1GB.txt
   ```
2. **Word Count Script**:
   Execute a Python script to count words:
   ```python
   with open('10MB.txt', 'r') as file:
       words = file.read().split()
       word_count = {word: words.count(word) for word in set(words)}
   ```
3. **Save Results**:
   Output results to `output.txt`.

---

### 6. EMR Setup with Hadoop Cluster

1. **Create EMR Cluster**:
   - Open **AWS EMR** > **Create Cluster**.
   - Configure:
     - Master Node: 1 (m5.xlarge).
     - Worker Nodes: 2 (m5.xlarge).
   - Software: Include Spark and Hadoop.
2. **SSH into Cluster**:
   - Login as `hadoop` using Putty.
3. **Run Word Count**:
   - Transfer files to `/home/hadoop` using WinSCP.
   - Execute Spark commands for Word Count.
![image](https://github.com/user-attachments/assets/80165ef0-9abe-427e-9bca-9fb6db3021cd)

---

## Results and Analysis

- **EC2 with Python**:
  - Successfully processed small datasets.
  - Higher processing time for larger datasets (1GB and above).
  ![image](https://github.com/user-attachments/assets/6aadc12c-4749-4d15-93bf-4c49e56323c0)

- **EMR with Spark**:
  - Demonstrated scalability and efficiency for big data processing.
  - Optimized processing time using distributed computing.
![image](https://github.com/user-attachments/assets/06426ffd-30e5-4db6-acf4-22a192359ce7)

---

## Error Handling

- **PySpark Error**: `IndexError: Tuple Index Out of Range`.
  - Solution: Check data formatting in `flatMap` and `map` operations.
  - Debugging command:
    ```python
    words = text_file.flatMap(lambda line

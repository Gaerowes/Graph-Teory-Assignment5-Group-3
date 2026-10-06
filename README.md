# Graph-Teory-Assignment5-Group-3

## 1. Identity
**Informatics ITS Graph Theory class Group 3**

* Dzulfiqar Rafi'ussunnah - 5025251011
* Padhang Abiyu Fikri - 5025251014
* Aditya Lingga Mardika - 5025251158
* Muhammad Faris Alfarrel - 5025251002

---

## 2. Project Description

This project implements a simple **Graph Visualizer** based on the concepts of graph matrix representation.

The program allows users to:

1. Input an **Adjacency Matrix** or **Incidence Matrix**.
2. Convert the matrix into an undirected graph.
3. Display the graph visually.
4. Generate the **Fundamental Cycle Matrix**.
5. Display the spanning tree and fundamental cycles.
6. Generate the **Cut-Set Matrix**.
7. Display the fundamental cut-sets.

The project is based on the Graph Theory Week 5 material about graph matrix representation.

---
## 3. Features

### 3.1 Matrix Input

The program supports two types of matrix input:

- Adjacency Matrix
- Incidence Matrix

The user can select the matrix type when running the program.

### 3.2 Graph Visualization

The input matrix is converted into an undirected graph and visualized using Python's graph visualization libraries.

Each vertex represents a node, while each edge represents a connection between two vertices.

### 3.3 Fundamental Cycle Matrix

The program generates the Fundamental Cycle Matrix using a spanning tree.

The process is:

1. Find a spanning tree.
2. Identify edges that are not part of the spanning tree.
3. Add each non-tree edge to the spanning tree.
4. The resulting path forms a fundamental cycle.
5. Represent each cycle in matrix form.

A value of:

- `1` means the edge belongs to the fundamental cycle.
- `0` means the edge does not belong to the fundamental cycle.

### 3.4 Cut-Set Matrix

The program also generates the Fundamental Cut-Set Matrix.

The process is:

1. Start with the spanning tree.
2. Remove one tree edge.
3. The spanning tree is divided into two components.
4. Find all original graph edges connecting the two components.
5. These edges form the fundamental cut-set.

A value of:

- `1` means the edge belongs to the cut-set.
- `0` means the edge does not belong to the cut-set.

---
## 4. Technologies Used

- **Python 3**
- **NetworkX**
- **Matplotlib**

---

## 5. Prerequisites

Make sure the following are installed on your computer:

- Python 3
- pip

The required Python libraries are:

- NetworkX
- Matplotlib

---

## 6. Installation

### Step 1 - Clone the Repository

Clone this repository using Git:

```bash
git clone https://github.com/Gaerowes/Graph-Teory-Assignment5-Group-3.git
```
### Step 2 - Open the Project Directory

```bash
cd Graph-Teory-Assignment5-Group-3
```

### Step 3 - Install Dependencies

```bash
pip install networkx matplotlib
```

---

## 7. How to run

Run the program using:
```bash
python cod3.py
```

The program will ask the user to choose the matrix type:
Choose matrix type:
1. Adjacency
2. Incidence

Enter either:
adjacency or incidence

After selecting the matrix type, enter the number of rows and columns, followed by the matrix values.

---
## 8. Sample input

<img width="887" height="221" alt="image" src="https://github.com/user-attachments/assets/8fc19585-d613-442d-adc3-5cda138ded56" />

---
## 9. Sample Output

```
Incidence Matrix:
1 1 0 0 0 0
1 0 1 1 0 0
0 1 1 0 1 0
0 0 0 1 0 1
0 0 0 0 1 1

Edges:
e1 = (1, 2)
e2 = (1, 3)
e3 = (2, 3)
e4 = (2, 4)
e5 = (3, 5)
e6 = (4, 5)

==============================
FUNDAMENTAL CYCLE MATRIX
==============================
     e 1  e 2  e 3  e 4  e 5  e 6  
C1    1    1    1    0    0    0  
C2    1    1    0    1    1    1  

Spanning Tree:
t1 = (1, 2)
t2 = (1, 3)
t3 = (2, 4)
t4 = (3, 5)

Fundamental Cycles:
C1 = {e1, e2, e3}
C2 = {e4, e1, e2, e5, e6}

==============================
CUT-SET MATRIX
==============================
     e 1  e 2  e 3  e 4  e 5  e 6  
K1    1    0    1    0    0    1  
K2    0    1    1    0    0    1  
K3    0    0    0    1    0    1  
K4    0    0    0    0    1    1  

Fundamental Cut-Sets:
K1 = {e1, e3, e6}
K2 = {e2, e3, e6}
K3 = {e4, e6}
K4 = {e5, e6}

```

<img width="1422" height="860" alt="image" src="https://github.com/user-attachments/assets/6844c053-8927-411b-8466-e37f5dfc3f96" />



# DSA Question Recommender Agent

## SLE-3: Architectural Design

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Project:** DSA Question Recommender Agent  
**Student:** Shivraj Pravin Banne  
**Division:** B  
**Branch:** AIML  
**Semester:** VI  

---

## 1. Project Overview

The DSA Question Recommender Agent is a Python-based recommendation system that suggests Data Structures and Algorithms (DSA) practice questions to learners.

The user selects:

- DSA topic
- Difficulty level
- Number of questions

The system validates the user's input and randomly selects the required number of questions from the available question database.

The project contains **45 curated DSA problems** organized into five topics and three difficulty levels.

### Topics

- Array
- Searching
- Sorting
- Stack
- Queue

### Difficulty Levels

- Easy
- Medium
- Hard

---

## 2. Objectives

The main objectives of the project are:

1. To recommend DSA practice questions according to the user's requirements.
2. To organize questions by topic and difficulty.
3. To randomly select unique questions.
4. To validate user input before processing.
5. To provide clear error messages for invalid input.
6. To demonstrate the architecture of a simple Python-based recommendation agent using the C4 Model.

---

## 3. System Working

The system follows this basic flow:

```text
User
  |
  | Topic + Difficulty + Count
  ↓
DSA Question Recommender Agent
  |
  | Validation
  ↓
Question Database
  |
  | Matching Questions
  ↓
Random Selection
  |
  ↓
Recommended Questions
Level 1 – Context
+-------------+
|    USER     |
+-------------+
       |
       | Topic, Difficulty, Count
       ↓
+----------------------------------+
| DSA Question Recommender Agent   |
+----------------------------------+
       |
       | Recommended Questions
       ↓
+-------------+
|    USER     |
+-------------+
Level 2 – Container
+-------------------+
|  User Input       |
|  Module            |
+-------------------+
          |
          ↓
+-------------------+
| Question Database |
+-------------------+
          |
          ↓
+-------------------+
| Recommendation    |
| Engine            |
+-------------------+
          |
          ↓
+-------------------+
| Output Module     |
+-------------------+
Level 3 – Component
                 +---------------------+
                 |   Input Validator   |
                 +---------------------+
                           |
                           ↓
                 +---------------------+
                 | Question Selector   |
                 +---------------------+
                           |
                           ↓
                 +---------------------+
                 | Output Formatter    |
                 +---------------------+

                 If validation fails
                           |
                           ↓
                 +---------------------+
                 |   Error Handler     |
                 +---------------------+

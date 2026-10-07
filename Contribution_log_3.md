
### Contribution_Log.md

For the **Contribution Log**, I would keep it aligned with the contribution information already present in your SLE-3 report: AI was used for the initial question database, recommendation logic, validation/error handling, and architecture organization, while you reviewed, modified, tested, and documented the system. 1

```markdown
# Contribution Log

## Project: DSA Question Recommender Agent

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Student:** Shivraj Pravin Banne  
**Project:** DSA Question Recommender Agent  
**SLE:** SLE-3 – Architectural Design  

---

## 1. Project Development

The DSA Question Recommender Agent was developed as a Python-based system for recommending Data Structures and Algorithms practice questions.

The project was developed and documented through multiple stages:

1. Creation of the DSA question database.
2. Development of the recommendation function.
3. Addition of input validation.
4. Addition of random question selection.
5. Testing with different inputs.
6. Designing the C4 architecture.
7. Preparing the SLE-3 documentation.

---

## 2. My Contributions

### Question Database

- Created and reviewed the DSA question database.
- Organized questions into five topics:
  - Array
  - Searching
  - Sorting
  - Stack
  - Queue
- Organized questions into:
  - Easy
  - Medium
  - Hard
- Reviewed the question difficulty classifications.

### Recommendation Logic

- Worked on the `recommend_questions()` function.
- Implemented user input for:
  - Topic
  - Difficulty
  - Number of questions
- Implemented random question selection using `random.sample()`.

### Input Validation

- Added validation for invalid topics.
- Added validation for invalid difficulty levels.
- Added validation for invalid question counts.
- Added handling when the requested number of questions exceeds the available questions.

### Testing

The system was tested using different combinations of:

- Topics
- Difficulty levels
- Question counts
- Invalid inputs

The output was checked to ensure that the recommendation logic worked correctly.

---

## 3. C4 Architecture Contribution

I designed and documented the C4 architecture of the DSA Question Recommender Agent.

The architecture was divided into four levels:

### Level 1 – Context

Documented the interaction between:

```text
User → DSA Question Recommender Agent → Recommended Questions

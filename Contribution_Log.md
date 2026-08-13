## Contribution 001

Date: 13 August 2026

File: agent.py

AI Tool: GitHub Copilot

Task:
Create the initial DSA question database organized by topic
and difficulty.

Prompt:
Create a Python dictionary named questions for a DSA question
recommendation agent. Organize it into five topics: Array,
Searching, Sorting, Stack, and Queue. Each topic must contain
three difficulty levels: easy, medium, and hard. For now,
put exactly 3 sample DSA questions under each difficulty.
Do not create any functions, input handling, recommendation
logic, or random selection yet.

AI Contribution:
Generated the initial question database structure with
45 DSA questions.

Accepted:
Yes

Modified:
Yes

Modification:
Reviewed the generated questions and corrected duplicate
questions and some difficulty classifications.

Reason:
To improve the accuracy and organization of the question
database.

## Contribution 002

Date: 13 August 2026

File: agent.py

AI Tool: GitHub Copilot

Task:
Create the recommendation logic for the DSA question
recommendation agent.

Prompt:
Using the existing questions dictionary in agent.py,
create a function called recommend_questions() that asks
the user to enter a DSA topic, difficulty level, and number
of questions. Validate that the topic and difficulty exist
in the dictionary. If the requested number is greater than
the available questions, display an appropriate message.
Use Python's random.sample() to select unique questions.
Display each recommended question's title and description.
Do not modify the existing questions dictionary.

AI Contribution:
Generated the recommend_questions() function including
input handling, validation, random question selection,
and output.

Accepted:
Yes

Modified:
Yes

Modification:
Reviewed the generated function and formatted the output
to display the question title and description on separate
lines.

Reason:
To make the recommended questions easier to read.
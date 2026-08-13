# DSA Question Recommender Agent
questions = {
    "Array": {
        "easy": [
            {
                "title": "Find Maximum Element",
                "description": "Find the largest element in an array."
            },
            {
                "title": "Best Time to Buy and Sell Stock",
                "description": "Find the maximum profit by choosing a single buy and sell day."
            },
            {
                "title": "Contains Duplicate",
                "description": "Check whether the array contains any duplicate elements."
            }
        ],
        "medium": [
            {
                "title": "Maximum Subarray",
                "description": "Find the contiguous subarray with the largest sum."
            },
            {
                "title": "Product of Array Except Self",
                "description": "Return an array where each element is the product of all other elements."
            },
            {
                "title": "3Sum",
                "description": "Find all unique triplets in the array that sum to zero."
            }
        ],
        "hard": [
            {
                "title": "Trapping Rain Water",
                "description": "Compute how much water can be trapped between elevations."
            },
            {
                "title": "Median of Two Sorted Arrays",
                "description": "Find the median of two sorted arrays with O(log n) complexity."
            },
            {
                "title": "Maximum Rectangle in Histogram",
                "description": "Find the largest rectangle area in a histogram."
            }
        ]
    },

    "Searching": {
        "easy": [
            {
                "title": "Linear Search",
                "description": "Find a target element in an unsorted array using linear search."
            },
            {
                "title": "Binary Search",
                "description": "Search for a target value in a sorted array using binary search."
            },
            {
                "title": "Search Insert Position",
                "description": "Find the index where a target should be inserted in a sorted array."
            }
        ],
        "medium": [
            {
                "title": "Find Peak Element",
                "description": "Find an index where the element is greater than its neighbors."
            },
            {
                "title": "Search a 2D Matrix",
                "description": "Search for a target in a row-wise and column-wise sorted matrix."
            },
            {
                "title": "Aggressive Cows",
                "description": "Place cows in stalls to maximize the minimum distance between them."
            }
        ],
        "hard": [
            {
                "title": "Median of Two Sorted Arrays",
                "description": "Find the median of two sorted arrays in logarithmic time."
            },
            {
                "title": "Search in Rotated Sorted Array II",
                "description": "Search for a target in a rotated sorted array that may contain duplicates."
            },
            {
                "title": "Smallest Rectangle Enclosing Black Pixels",
                "description": "Find the minimum area rectangle covering all black pixels."
            }
        ]
    },

    "Sorting": {
        "easy": [
            {
                "title": "Sort Array",
                "description": "Sort the given array in ascending order."
            },
            {
                "title": "Merge Sorted Array",
                "description": "Merge two sorted arrays into one sorted array."
            },
            {
                "title": "Valid Anagram",
                "description": "Check if two strings are anagrams of each other."
            }
        ],
        "medium": [
            {
                "title": "Top K Frequent Elements",
                "description": "Return the k most frequent elements in the array."
            },
            {
                "title": "Meeting Rooms II",
                "description": "Find the minimum number of meeting rooms required."
            },
            {
                "title": "Sort Colors",
                "description": "Sort an array containing 0s, 1s, and 2s in-place."
            }
        ],
        "hard": [
            {
                "title": "Largest Number",
                "description": "Arrange numbers to form the largest possible number."
            },
            {
                "title": "Wiggle Sort II",
                "description": "Rearrange numbers so that the sequence alternates below and above the median."
            },
            {
                "title": "Count of Smaller Numbers After Self",
                "description": "Count how many smaller numbers appear to the right of each element."
            }
        ]
    },

    "Stack": {
        "easy": [
            {
                "title": "Valid Parentheses",
                "description": "Check whether a string contains valid parentheses sequences."
            },
            {
                "title": "Implement Stack Using Array",
                "description": "Implement basic push and pop operations using an array."
            },
            {
                "title": "Reverse a String Using Stack",
                "description": "Reverse a string by using a stack data structure."
            }
        ],
        "medium": [
            {
                "title": "Min Stack",
                "description": "Design a stack that supports push, pop, top, and minimum operations."
            },
            {
                "title": "Daily Temperatures",
                "description": "Find how many days must be waited for a warmer temperature."
            },
            {
                "title": "Next Greater Element I",
                "description": "Find the next greater element for each element in an array."
            }
        ],
        "hard": [
            {
                "title": "Largest Rectangle in Histogram",
                "description": "Compute the largest rectangular area in a histogram."
            },
            {
                "title": "Longest Valid Parentheses",
                "description": "Find the length of the longest valid parentheses substring."
            },
            {
                "title": "Basic Calculator",
                "description": "Evaluate an expression containing numbers, operators, and parentheses."
            }
        ]
    },

    "Queue": {
        "easy": [
            {
                "title": "Implement Queue Using Array",
                "description": "Implement basic enqueue and dequeue operations using an array."
            },
            {
                "title": "Number of Recent Calls",
                "description": "Track the number of recent requests within a fixed time window."
            },
            {
                "title": "Moving Average from Data Stream",
                "description": "Calculate the moving average of values received from a data stream."
            }
        ],
        "medium": [
            {
                "title": "Design Circular Queue",
                "description": "Implement a circular queue with a fixed capacity."
            },
            {
                "title": "Sliding Window Maximum",
                "description": "Find the maximum value in every window of size k."
            },
            {
                "title": "Task Scheduler",
                "description": "Schedule tasks while respecting the required cooldown period."
            }
        ],
        "hard": [
            {
                "title": "Shortest Subarray with Sum at Least K",
                "description": "Find the shortest subarray whose sum is at least K."
            },
            {
                "title": "Design a Front-Middle-Back Queue",
                "description": "Design a queue that supports operations at the front, middle, and back."
            },
            {
                "title": "Sliding Window Median",
                "description": "Find the median of every sliding window in an array."
            }
        ]
    }
}
import random


def recommend_questions():
    topic = input(
        "Enter a DSA topic (Array, Searching, Sorting, Stack, Queue): "
    ).strip().title()

    if topic not in questions:
        print(f"Invalid topic. Available topics: {', '.join(questions.keys())}")
        return

    difficulty = input(
        "Enter difficulty level (easy, medium, hard): "
    ).strip().lower()

    if difficulty not in questions[topic]:
        print(
            f"Invalid difficulty for {topic}. "
            f"Available levels: {', '.join(questions[topic].keys())}"
        )
        return

    try:
        count = int(input("Enter the number of questions: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    if count <= 0:
        print("Number of questions must be greater than 0.")
        return

    available_questions = questions[topic][difficulty]

    if count > len(available_questions):
        print(
            f"Only {len(available_questions)} question(s) are available "
            f"for {topic} - {difficulty}."
        )
        return

    selected_questions = random.sample(available_questions, count)

    print(f"\nRecommended {topic} questions ({difficulty}):")

    for question in selected_questions:
        print(f"- {question['title']}")
        print(f"  {question['description']}")


if __name__ == "__main__":
    recommend_questions()
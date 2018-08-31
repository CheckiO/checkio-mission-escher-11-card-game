"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input":[5, [2, 0, 1, 2]],
            "answer": False
        },
        {
            "input":[10, [9, 9, 6, 6]],
            "answer": True
        }
    ],
    "Extra": [
        {
            "input":[25, [17, 11, 16, 12, 5, 12, 11]],
            "answer": False
        },
        {
            "input":[51, [29, 36, 30, 42]],
            "answer": True
        },
        {
            "input":[100, [95, 11, 29, 64, 94, 96, 13, 96, 88, 95]],
            "answer": False
        },
        {
            "input":[99, [2, 3, 5, 8, 13, 21, 114]],
            "answer": False
        }

    ]
}

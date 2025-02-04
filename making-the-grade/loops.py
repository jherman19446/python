"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    whole_grades = [round(score) for score in student_scores]
    return whole_grades
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """



def count_failed_students(student_scores):
    index = 0
    count = 0
    while index < len(student_scores):
        if student_scores[index] <= 40:
            count += 1
        index += 1
    return count
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """


def above_threshold(student_scores, threshold):
    index = 0
    good_scores = []
    for score in student_scores:
        if student_scores[index] >= threshold:
            good_scores.append(score)
        index += 1
    return good_scores

    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """


def letter_grades(highest):
    step = int((highest - 40)/4)
    return [41 + step*i for i in range(4)]
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """


def student_ranking(student_scores, student_names):
    rankings = []
    for index, score in enumerate(student_scores, start=1):
        rankings.append(f'{index}. {student_names[index-1]}: {score}')
    return sorted(rankings)
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """


def perfect_score(student_info):
    perfect_scores = []
    for student in student_info:
        if student[1] == 100:  # Check if the student's score is 100
            return student
    return perfect_scores     
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

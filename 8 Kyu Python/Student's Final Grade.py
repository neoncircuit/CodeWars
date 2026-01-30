def final_grade(exam: int, projects: int) -> int:
    # final grade
    return 100 if (exam > 90 or projects > 10) \
        else 90 if (exam > 75 and projects >= 5) \
        else 75 if (exam > 50 and projects >= 2) \
        else 0
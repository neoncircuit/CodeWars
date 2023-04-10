def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    match human_years:
        case 1:
            cat_years = dog_years = 15
        case 2:
            cat_years = dog_years = 15 + 9
        case _:
            cat_years = 15 + 9 + 4 * (human_years - 2)
            dog_years = 15 + 9 + 5 * (human_years - 2)
    return [human_years, cat_years, dog_years]

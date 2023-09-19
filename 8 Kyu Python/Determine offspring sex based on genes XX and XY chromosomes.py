def chromosome_check(chromosome):
    match chromosome:
        case 'XX':
            return "Congratulations! You're going to have a daughter."
        case 'XY':
            return "Congratulations! You're going to have a son."

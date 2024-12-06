def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    # Your code here.
    while blue_pulled < blue_start and red_pulled < red_start:
        return (blue_start - blue_pulled)/(blue_start - blue_pulled + red_start - red_pulled)
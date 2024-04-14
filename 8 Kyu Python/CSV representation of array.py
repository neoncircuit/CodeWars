def to_csv_text(array):
    formatted_rows = []

    for row in array:
        formatted_row = ','.join(map(str, row))
        formatted_rows.append(formatted_row)

    return '\n'.join(formatted_rows)

import csv
from io import StringIO


def create_csv(history):

    output = StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "ID",
        "Operation",
        "Number1",
        "Number2",
        "Result",
        "Created At"
    ])

    for item in history:

        writer.writerow([
            item.id,
            item.operation,
            item.number1,
            item.number2,
            item.result,
            item.created_at
        ])

    output.seek(0)

    return output
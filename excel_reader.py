import os
import random
import csv
import json


class Question:
    def __init__(self, type_id, first_mixed_number, first_numerator, first_denominator, operator, second_mixed_number, second_numerator, second_denominator, answer_mixed_number, answer_numerator, answer_denominator, options):
        self.type_id = type_id
        self.first_mixed_number = first_mixed_number
        self.first_numerator = first_numerator
        self.first_denominator = first_denominator
        self.operator = operator
        self.second_mixed_number = second_mixed_number
        self.second_numerator = second_numerator
        self.second_denominator = second_denominator
        self.answer_mixed_number = answer_mixed_number
        self.answer_numerator = answer_numerator
        self.answer_denominator = answer_denominator
        self.options = options


class Option:
    def __init__(self, numerator, denominator, mixed_number=None) -> None:
        self.mixed_number = mixed_number
        self.numerator = numerator
        self.denominator = denominator


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Question, Option)):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


prefix = "./init_data"
files = [f'{prefix}/improper_fractions.csv', f'{prefix}/mixed_fractions.csv']


def transfer_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


def process_improper_fractions(list_of_fractions):
    result = []

    for question in list_of_fractions:
        first_fraction = question[0]
        first_numerator = first_fraction.split("/")[0]
        first_denominator = first_fraction.split("/")[1]
        operator = question[1]
        second_fraction = question[2]
        second_numerator = second_fraction.split("/")[0]
        second_denominator = second_fraction.split("/")[1]
        answer_fraction = question[3]
        answer_numerator = answer_fraction.split("/")[0]
        answer_denominator = answer_fraction.split("/")[1]
        option1 = Option(int(first_numerator), int(first_denominator))
        option2 = Option(int(first_numerator) +
                         int(second_numerator), int(first_denominator))
        option3 = Option(int(first_numerator) -
                         int(second_numerator), int(first_denominator))
        options = [option1, option2, option3]
        random.shuffle(options)
        question = Question(2, None, int(first_numerator), int(first_denominator), operator, None, int(second_numerator), int(
            second_denominator), None, int(answer_numerator), int(answer_denominator), options)
        result.append(question)

    return result


def process_mixed_fractions(list_of_fractions):
    result = []

    for question in list_of_fractions:
        first_fraction = question[0]
        operator = question[1]
        second_fraction = question[2]
        answer_fraction = question[3]
        first_numerator_and_mixed_number = first_fraction.split("/")[0]
        first_mixed_number = first_numerator_and_mixed_number.split(" ")[0]
        first_numerator = first_numerator_and_mixed_number.split(" ")[1]
        first_denominator = first_fraction.split("/")[1]

        second_numerator_and_mixed_number = second_fraction.split("/")[0]
        second_mixed_number = second_numerator_and_mixed_number.split(" ")[0]
        second_numerator = second_numerator_and_mixed_number.split(" ")[1]
        second_denominator = second_fraction.split("/")[1]

        if "/" in answer_fraction:
            answer_numerator_and_mixed_number = answer_fraction.split("/")[0]
            answer_mixed_number = answer_numerator_and_mixed_number.split(" ")[
                0]
            answer_numerator = answer_numerator_and_mixed_number.split(" ")[1]
            answer_denominator = answer_fraction.split("/")[1]
        else:
            answer_mixed_number = answer_fraction
            answer_numerator = None
            answer_denominator = None

        answer_numerator = int(
            answer_numerator) if answer_numerator != None else None
        answer_denominator = int(
            answer_denominator) if answer_denominator != None else None

        option1 = Option(int(first_numerator), int(
            first_denominator), int(first_mixed_number))
        option2 = Option(int(first_numerator) + int(second_numerator),
                         int(first_denominator), int(first_mixed_number))
        option3 = Option(answer_numerator, answer_denominator,
                         int(answer_mixed_number))
        options = [option1, option2, option3]
        random.shuffle(options)
        question = Question(type_id=3,
                            first_mixed_number=int(first_mixed_number),
                            first_numerator=int(
                                first_numerator) if first_numerator != None else first_numerator,
                            first_denominator=int(
                                first_denominator) if first_denominator != None else first_denominator,
                            operator=operator,
                            second_mixed_number=int(second_mixed_number),
                            second_numerator=int(second_numerator),
                            second_denominator=int(second_denominator),
                            answer_mixed_number=int(answer_mixed_number),
                            answer_numerator=answer_numerator,
                            answer_denominator=answer_denominator,
                            options=options)
        result.append(question)
    return result


def dump_result(result_list, output_name):
    with open(output_name, 'w') as f:
        data = {
            "questions": result_list
        }
        json_string = json.dumps(data, cls=CustomEncoder)
        f.write(json_string)

        print(f"JSON 字串已成功匯出到 {output_name} 文件中。")


if __name__ == '__main__':
    # improper_fractions = transfer_to_list(files[0])
    # improper_fractions_result = process_improper_fractions(improper_fractions)
    # dump_result(improper_fractions_result, 'improper_fractions.json')
    mixed_fractions = transfer_to_list(files[1])
    mixed_fractions_result = process_mixed_fractions(mixed_fractions)
    dump_result(mixed_fractions_result, 'mixed_fractions.json')

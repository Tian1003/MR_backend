import random
import json
import os
from PyPDF2 import PdfReader


class Question:
    def __init__(self, first_numerator, first_denominator, operator, second_numerator, second_denominator, answer_numerator, answer_denominator, options):
        self.type_id = 1
        self.first_mixed_number = None
        self.first_numerator = first_numerator
        self.first_denominator = first_denominator
        self.operator = operator
        self.second_mixed_number = None
        self.second_numerator = second_numerator
        self.second_denominator = second_denominator
        self.answer_mixed_number = None
        self.answer_numerator = answer_numerator
        self.answer_denominator = answer_denominator
        self.options = options


class Option:
    def __init__(self, numerator, denominator) -> None:
        self.mixed_number = None
        self.numerator = numerator
        self.denominator = denominator


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Question, Option)):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


init_data_path = os.path.join('.', "questions")
files = os.listdir(init_data_path)

for file_name in files:
    if file_name.endswith('.pdf'):
        output_name = f"question{file_name[-6:-4]}.json"
        reader = PdfReader(f"./questions/{file_name}")
        result = []
        all_pages = reader.pages
        for page in all_pages:
            text = page.extract_text()
            questions = text.split(".")[1:]
            for item in questions:
                item = item.replace("\n", "").replace(" ", "").split("=")[0]

                operator = "+" if "+" in item else "-"
                first_fraction = item.split(operator)[0].strip()
                first_numerator = first_fraction[-1] if len(first_fraction) <= 3 else first_fraction[-2:]
                first_denominator = first_fraction[0:len(first_fraction)-1] if len(first_fraction) <= 3 else first_fraction[0:len(first_fraction)-2]
                second_fraction = item.split(operator)[1].strip()
                second_numerator = second_fraction[-1] if len(second_fraction) <= 3 else second_fraction[-2:]
                second_denominator = second_fraction[0:len(second_fraction)-1] if len(second_fraction) <= 3 else second_fraction[0:len(second_fraction)-2]
                answer_numerator = int(first_numerator) + int(
                    second_numerator) if operator == "+" else int(first_numerator) - int(second_numerator)
                answer_denominator = first_denominator if first_denominator == second_denominator else None
                option1 = Option(int(first_numerator), int(first_denominator))
                option2 = Option(int(first_numerator) +
                                int(second_numerator), int(first_denominator))
                option3 = Option(int(first_numerator) -
                                int(second_numerator), int(first_denominator))
                options = [option1, option2, option3]
                random.shuffle(options)

                question = Question(int(first_numerator), int(first_denominator), operator, int(second_numerator), int(
                    second_denominator), int(answer_numerator), int(answer_denominator), options)
                result.append(question)

        with open(output_name, 'w') as f:
            data = {
                "questions": result
            }
            json_string = json.dumps(data, cls=CustomEncoder)
            f.write(json_string)

            print(f"JSON 字串已成功匯出到 {output_name} 文件中。")

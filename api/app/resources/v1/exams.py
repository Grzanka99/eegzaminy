from ..base import BaseResource
from app.models import (ExamModel, 
                    QuestionModel, 
                    ExamsSchema, 
                    ExamSchema, 
                    QuestionsSchema, 
                    QuestionSchema)

# namesDict = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}


# Return list of exams
class ExamsList(BaseResource):
    def get(self):
        data = ExamModel.query.all()
        data = ExamsSchema.dump(data).data

        return self.response(data)


# Return requested exam
class Exam(BaseResource):
    def get(self, name=None):
        # if name == 'favicon.ico':
        #     return {'message': 'Ni chuja'}, 404

        # examList = fn.getExamsList()
        # if name in examList and name != 'egzamin':
        #     data = {
        #         'title': name,
        #         'questions': fn.getQuestions(name),
        #         'name': namesDict
        #     }
        #     return data, 200
        # else:
        #     return 'Exam {} not found'.format(name), 404

        data = ExamModel.query.filter_by(name=name).first()
        data = ExamsSchema.dump(data).data

        if data:
            return self.response(data)
        else:
            return self.response({'msg': 'Not found!'}, 404)

# TODO: Create verification resource using model and schema.
# class Verification(Resource):
#     def post(self):
#         data = request.form.to_dict()
#         try:
#             questionsInTest = data['list'].split(';')
#             questions = {}
#             percent: float = 0
#             for nr in questionsInTest:
#                 if nr == '':
#                     continue
#                 inr = int(nr)
#                 qObj = fn.getOneQuestion(nr=inr, egz=data['egz_name'])
#                 questions[inr] = {
#                     'q': qObj,
#                     # 'valid': qObj['answer'],
#                     'user': None
#                 }
#                 if nr in data:
#                     questions[inr]['user'] = data[nr]
#                     if questions[inr]['valid'] == data[nr]:
#                         percent += 1

#             percent = (percent / (len(questionsInTest) - 1)) * 100

#             out = {
#                 'userData': data,
#                 'questions': questions,
#                 'percent': percent,
#                 'name': namesDict
#             }
#             return out, 200

#         except MissingDataException:
#             return {'err': 'No data'}, 400
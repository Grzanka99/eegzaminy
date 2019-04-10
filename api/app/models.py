from app.extensions import db, ma

# TODO: Designing the database.

class ExamModel(db.Model):
    __tablename__ = 'exam'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(30), unique=True)
    question = db.relationship('QuestionModel')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "<Exam (id={}, Name={})>".format(self.id, self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()

class QuestionModel(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(100), unique=True)
    exam_name = db.Column(db.VARCHAR(30), db.ForeignKey('ExamModel.name'))
    answer = db.Column(db.Text(1))
    answer_a = db.Column(db.VARCHAR(50))
    answer_b = db.Column(db.VARCHAR(50))
    answer_c = db.Column(db.VARCHAR(50))
    answer_d = db.Column(db.VARCHAR(50))

    def __init__(self, title=None, answer=None, 
                answer_a=None, answer_b=None, answer_c=None,
                answer_d=None):

            self.title = title
            self.answer = answer
            self.answer_a = answer_a
            self.answer_b = answer_b
            self.answer_c = answer_c
            self.answer_d = answer_d

    def __repr__(self):
        return "<Question (id={}, title={})>".format(self.id, self.title)

# Json Schems
class ExamSchema(ma.Schema):
    class Meta:
        model = ExamModel

class QuestionSchema(ma.Schema):
    class Meta:
        model = QuestionModel

ExamsSchema = ExamSchema(many=True)
QuestionsSchema = QuestionSchema(many=True)
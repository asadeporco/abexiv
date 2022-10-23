from answer.models import Answer


class AnswerService:

    def __init__(self):
        pass

    def create_answer(self, question_id, data, user):
        answer = Answer()
        answer.description = data.get("description")
        answer.user = user
        answer.question_id = question_id

        answer.save()

        return answer

    def update_answer(self, answer_id, data):
        answer = Answer.objects.filter(id=answer_id).first()
        answer.description = data.get("description")
        answer.save()

        return answer
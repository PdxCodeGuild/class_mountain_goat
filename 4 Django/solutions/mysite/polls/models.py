from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # https://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django
    # the related_name allows you to customize the name of the set of all the related objects
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):

        # question = Question.objects.get(id=self.question_id)
        # return question.question_text + ' ' + self.choice_text

        return self.question.question_text + ' ' + self.choice_text + ' (' + str(self.votes) + ')'




class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        r = self.name
        if self.city:
            r += ' lives in ' + self.city.name + ' ' + self.city.state
        else:
            r += ' lives nowhere'
        return r







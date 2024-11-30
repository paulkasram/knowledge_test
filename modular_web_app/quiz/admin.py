from django.contrib import admin
from .models import Topic, Question, QuizSession

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'question_text', 'option1', 'option2', 'option3', 'option4', 'correct_answer')
    list_filter = ('topic',)
    search_fields = ('question_text',)

@admin.register(QuizSession)
class QuizSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'topic', 'score', 'date_taken')
    list_filter = ('topic', 'date_taken')
    search_fields = ('user__username', 'topic__name')

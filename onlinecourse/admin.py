from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
from django.contrib import admin

from .models import (

    Question,

    Choice,

    Submission,

    Lesson,

    Course,

    Enrollment,

    UserProfile

)

# Inline for Choice inside Question

class ChoiceInline(admin.TabularInline):

    model = Choice

    extra = 2

# Inline for Question inside Lesson

class QuestionInline(admin.TabularInline):

    model = Question

    extra = 1

# Question Admin

class QuestionAdmin(admin.ModelAdmin):

    list_display = ('text', 'created_at')

    inlines = [ChoiceInline]

# Lesson Admin

class LessonAdmin(admin.ModelAdmin):

    list_display = ('title',)

    inlines = [QuestionInline]

# Register models

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

admin.site.register(Submission)

admin.site.register(Lesson, LessonAdmin)

admin.site.register(Course)

admin.site.register(Enrollment)

admin.site.register(UserProfile)

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)

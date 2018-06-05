from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CourseCategory)  # 课程大类, e.g 前端  后端...
admin.site.register(CourseSubCategory)  # 课程子类, e.g python linux
admin.site.register(DegreeCourse)  # 学位课程
admin.site.register(Teacher)  # 讲师、导师表
admin.site.register(Scholarship)  # 学位课程奖学金
admin.site.register(Course)  # 专题课程 OR 学位课模块
admin.site.register(CourseDetail)  # 课程详情页内容
admin.site.register(OftenAskedQuestion)  # 常见问题
admin.site.register(CourseOutline)  # 课程大纲
admin.site.register(CourseChapter)  # 课程章节
admin.site.register(CourseSection)  # 课时目录
admin.site.register(Homework)  # 章节作业
admin.site.register(PricePolicy)  # 价格与有课程效期表
admin.site.register(ArticleSource)  # 文章来源表
admin.site.register(Article)  # 文章资讯
admin.site.register(Collection)  # 收藏
admin.site.register(Comment)  # 通用的评论表
admin.site.register(Account)  # 用户表
admin.site.register(UserAuthToken)  # 用户Token表

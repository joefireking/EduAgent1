# from pydantic import BaseModel
#
# class Student(BaseModel):
#     name: str          # 字符串
#     age: int           # 整数
#
# # 用关键字参数创建实例
# # s = Student(name="小明", age=18)
# # print(s.name)          # 小明
# # print(s.age)           # 18
# # print(s)               # name='小明' age=18
# #
# # print(f'*'*80)
# # class Student1():
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# # s1 = Student1(name="张三", age = "09")
# # print(s1.name)
# # print(s1)

# s = Student(name="小红", age="18")   # age 传的是字符串
# print(s.age, type(s.age))            # 18 <class 'int'>  → 自动转成了 int
# from pydantic import BaseModel, ValidationError
#
# class Student(BaseModel):
#     name: str
#     age: int
#
# try:
#     Student(name="小刚", age="十八")   # "十八" 无法转成整数
# except ValidationError as e:
#     print(e)


# from pydantic import BaseModel, Field
#
# class UserProfile(BaseModel):
#     name:  str = Field(description="用户姓名")            # 必填：没有默认值
#     phone: str = Field(default="", description="手机号")  # 可选：有默认值 ""
#     age:   int = Field(default=18, description="年龄")    # 可选：默认 18
#     hobbys: list = Field(default_factory=list, description="爱好")
#     # hobbys: list = Field(default=[], description="爱好") # 不建议
#
#
# up = UserProfile(name="张三", phone="123456")
# print(up.name)
# print(up.phone)
# print(up.age)
# print(up.hobbys)


# from pydantic import BaseModel, Field
#
# class EducationItem(BaseModel):
#     school: str = Field(description="学校名称")
#     major:  str = Field(description="专业名称")
#
# class Resume(BaseModel):
#     name:      str                = Field(description="姓名")
#     education: list[EducationItem] = Field(default_factory=list)  # 教育经历列表
# #
# # # 创建时，嵌套部分可以直接用字典，Pydantic 会自动转成对应的子模型
# # resume = Resume(
# #     name="小明",
# #     education=[
# #         {"school": "清华大学", "major": "计算机"},
# #         {"school": "北京大学", "major": "软件工程"},
# #     ],
# # )
#
# resume = Resume(
#     name="小明",
#     education=[EducationItem(school="清华大学",major="计算机"),
#                EducationItem(school="北京大学",major="软件工程"),]
# )
#
# # a = resume.dict()
# a = resume.model_dump()
# print(a)
# print(resume.name)                    # 小明
# print(resume.education[0].school)     # 清华大学  ← 注意：已经是 EducationItem 对象了
# print(type(resume.education[0]))      # <class '__main__.EducationItem'>





from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(description="姓名")
    age:  int = Field(default=18, description="年龄")

# s = Student(name="小明", age=20)
#
# d = s.model_dump()       # 模型 → 字典
# print(d)                 # {'name': '小明', 'age': 20}
# print(type(d))           # <class 'dict'>
# data = {"name": "小红", "age": 22}
# s2 = Student(**data)     # 字典 → 模型
# print(f's2-->{s2}')
# print(s2.name)           # 小红

# def fun(**kwargs):
#     print(kwargs)
#
# # fun(a=1, b=2)
#
# dict1 = {"a":1, "b":2, "c":3}
# fun(**dict1)


from enum import Enum

class InterviewStage(str, Enum):       # 继承 str，取值就是字符串
    WARMUP    = "warmup"
    TECH_BASE = "tech_base"
    PROJECT   = "project"
    CLOSING   = "closing"
    FINISHED  = "finished"

print(InterviewStage.WARMUP)           # InterviewStage.WARMUP
print(InterviewStage.WARMUP.value)     # warmup

# if InterviewStage.WARMUP.value == "warmup":
#     print('你好')
#
# if InterviewStage.WARMUP == "warmup":
#     print('你好')
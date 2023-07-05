import re
from baidu import get_suggestion_words
from chart import generate_line_chart
from score import get_average_score, get_sentiment_score



occupations = ["建筑工程师", "程序员"]
ages = [26, 28, 30, 35, 40, 45, 50]
prompt = '帮我分析如下语句的情感指数，-10代表极端负面， +10代表极端正面， 0代表中性，通过培训考证等方式入行算作正面，转行、寻找出路算负面。请仅仅返回数值数组，数值在-10到10之间。'
occ_scores = []
for occupation in occupations:
    scores = []
    for age in ages:
        keyword = f"{occupation} {age}岁"
        suggestions = get_suggestion_words(keyword)
        if suggestions:
            score = get_sentiment_score(prompt + suggestions)
            print(f"'{keyword}'的评分：")
            print(suggestions)
            print(score)
            scores.append(get_average_score(score))

    occ_scores.append(scores)

generate_line_chart(ages, occ_scores, "年龄", "指数", occupations, "职业与年龄的焦虑指数")


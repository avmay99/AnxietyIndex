import matplotlib.pyplot as plt

def generate_line_chart(x, y_list, x_label, y_label, line_labels, title):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 绘制折线图
    for i, y in enumerate(y_list):
        plt.plot(x, y, label=line_labels[i])

    # 设置图表标题和坐标轴标签
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # 添加图例
    plt.legend()

    # 显示网格线
    plt.grid(True)

    # 显示图表
    plt.show()
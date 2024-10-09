import matplotlib.pyplot as plt
import networkx as nx

# 定义层级依赖
layer_dependencies = [
    [-1], [0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],
    [11, 6], [12], [13], [14], [15, 4], [16], [17], [18, 14],
    [19], [20], [21, 10], [22], [17, 20, 23]
]

# 创建一个有向图
G = nx.DiGraph()

# 添加节点和边
for layer, dependencies in enumerate(layer_dependencies):
    for dep in dependencies:
        if dep != -1:  # 排除没有依赖的层
            G.add_edge(dep, layer)

# 绘制图形
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # 节点位置布局
nx.draw(G, pos, with_labels=True, arrows=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
plt.title("YOLOv5 Layer Dependency DAG")
plt.show()

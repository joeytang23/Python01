import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.mpl_axes import Axes

# ==================== 配置区域 ====================
plt.rcParams['font.sans-serif'] = ['SimHei']  # 展示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


# ==================== 数据加载与清洗 ====================
def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """
    加载电影数据并进行基础清洗

    Args:
        filepath: CSV文件路径

    Returns:
        清洗后的DataFrame
    """
    data = pd.read_csv(
        filepath,
        usecols=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言'],
        dtype={'年份': 'Int64'}
    )

    # 处理年份缺失值：从上映时间字符串中提取前4位
    data['年份'] = data['年份'].fillna(
        data['上映时间'].str[0:4].astype('Int64')
    )

    return data


# ==================== 需求1：每年上映电影数量变化（折线图） ====================
def prepare_year_data(data: pd.DataFrame) -> tuple[list, list]:
    """
    准备年份统计数据

    Returns:
        (年份列表, 对应数量列表)
    """
    year_count = data.groupby('年份')['年份'].count()

    min_year = int(year_count.index.min())
    max_year = int(year_count.index.max()) + 1  # +1 确保包含最后一年

    x = list(range(min_year, max_year))
    y = [year_count.get(i, 0) for i in x]

    return x, y


def plot_year_trend(axes: Axes, data: pd.DataFrame) -> None:
    """绘制每年上映电影数量变化折线图"""
    x, y = prepare_year_data(data)

    axes.plot(x, y, color='#2E86AB', linewidth=2, marker='o', markersize=3)
    axes.set_title('每年上映电影数量变化', fontsize=14, fontweight='bold')
    axes.set_xlabel('年份', fontsize=12)
    axes.set_ylabel('电影数量', fontsize=12)
    axes.set_xticks(x[::10])
    axes.set_yticks(range(0, 31))
    axes.grid(linestyle='--', alpha=0.5)


# ==================== 需求2：不同语言电影数量对比（柱状图） ====================
def prepare_language_data(data: pd.DataFrame) -> tuple[list, list]:
    """
    准备语言统计数据

    Returns:
        (语言列表, 对应数量列表)
    """
    language_count = data.groupby('语言')['语言'].count().sort_values(ascending=False)
    x_language = language_count.index.tolist()
    y_language = language_count.values.tolist()
    return x_language, y_language


def plot_language_comparison(axes: Axes, data: pd.DataFrame) -> None:
    """绘制不同语言电影数量对比柱状图"""
    x_language, y_language = prepare_language_data(data)

    axes.bar(x_language, y_language, width=0.7, color='#A23B72')
    axes.set_title("不同语言电影数量对比", fontsize=14, fontweight='bold')
    axes.set_xlabel('语言', fontsize=12)
    axes.set_ylabel('电影数量', fontsize=12)
    axes.grid(linestyle='--', alpha=0.5)
    axes.tick_params(axis='x', rotation=45)


# ==================== 需求3：不同类型电影数量对比（柱状图） ====================
def prepare_type_data(data: pd.DataFrame) -> tuple[list, list]:
    """
    准备类型统计数据（处理多类型逗号分隔的情况）

    Returns:
        (类型列表, 对应数量列表)
    """
    type_count = {}
    for types in data['类型'].str.split(','):
        for t in types:
            t = t.strip()  # 去除首尾空格
            type_count[t] = type_count.get(t, 0) + 1

    # 按数量降序排列
    sorted_types = sorted(type_count.items(), key=lambda item: item[1], reverse=True)
    x_type = [item[0] for item in sorted_types]
    y_type = [item[1] for item in sorted_types]

    return x_type, y_type


def plot_type_comparison(axes: Axes, data: pd.DataFrame) -> None:
    """绘制不同类型电影数量对比柱状图"""
    x_type, y_type = prepare_type_data(data)

    axes.bar(x_type, y_type, width=0.7, color='#F18F01')
    axes.set_title("不同类型电影数量对比", fontsize=14, fontweight='bold')
    axes.set_xlabel('类型', fontsize=12)
    axes.set_ylabel('电影数量', fontsize=12)
    axes.grid(linestyle='--', alpha=0.5)
    axes.tick_params(axis='x', rotation=45)


# ==================== 需求4：各个评分电影占比（饼状图） ====================
def prepare_score_data(data: pd.DataFrame) -> tuple[list, list]:
    """
    准备评分统计数据，合并占比小于2%的数据为"其他"

    Returns:
        (评分标签列表, 对应数量列表)
    """
    score_count = data.groupby('评分')['评分'].count()
    total = score_count.sum()

    # 分离大数据和小数据
    large_scores = score_count[score_count >= total * 0.02].copy()
    small_scores = score_count[score_count < total * 0.02]

    # 合并小数据
    if small_scores.shape[0] > 0:
        large_scores.loc['其他'] = small_scores.sum()

    scores = large_scores.index.tolist()
    score_values = large_scores.values.tolist()

    return scores, score_values


def plot_score_distribution(axes: Axes, data: pd.DataFrame) -> None:
    """绘制各个评分电影占比饼状图"""
    scores, score_values = prepare_score_data(data)

    axes.set_title('各个评分电影占比', y=1.05, fontsize=14, fontweight='bold')
    axes.pie(
        score_values,
        labels=scores,
        autopct='%1.1f%%',
        shadow=False,
        startangle=0,
        radius=1.2,
        colors=plt.cm.Set3.colors
    )
    axes.legend(loc='lower left', bbox_to_anchor=(0.5, -0.2), ncol=4)


# ==================== 主程序 ====================
def create_figure() -> tuple:
    """创建画布和子图"""
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.suptitle('TMDB-TOP300电影数据统计', fontsize=23, x=0.5, y=0.95)
    fig.subplots_adjust(hspace=0.4, wspace=0.2)
    return fig, ax


def main() -> None:
    """主函数：执行完整的数据分析与可视化流程"""
    # 1. 加载数据
    data = load_and_clean_data('data/movies.csv')

    # 2. 创建画布
    fig, ax = create_figure()

    axes1: Axes = ax[0][0]
    axes2: Axes = ax[0][1]
    axes3: Axes = ax[1][0]
    axes4: Axes = ax[1][1]

    # 3. 绘制四个子图
    plot_year_trend(axes1, data)
    plot_language_comparison(axes2, data)
    plot_type_comparison(axes3, data)
    plot_score_distribution(axes4, data)

    # 4. 保存并展示
    plt.savefig('data/TMDB-TOP300.png', bbox_inches='tight')
    plt.show()
    print("图表已保存至 data/TMDB-TOP300.png")


if __name__ == '__main__':
    main()
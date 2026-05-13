from common import BASE_DIR, TODAY, ensure_dirs
from competitor_collector import run as run_competitors
from hot_topics_collector import run as run_hot_topics
from viral_analyzer import run as run_viral_analyzer


def main() -> None:
    ensure_dirs()
    hot_topics_path = run_hot_topics()
    competitors_path = run_competitors()
    viral_analysis_path = run_viral_analyzer()
    print("AI 自媒体增长操作系统第二阶段基础模块已完成。")
    print(f"日期：{TODAY}")
    print(f"热点采集输出：{hot_topics_path}")
    print(f"竞品采集输出：{competitors_path}")
    print(f"爆款拆解输出：{viral_analysis_path}")
    print(f"项目根目录：{BASE_DIR}")


if __name__ == "__main__":
    main()

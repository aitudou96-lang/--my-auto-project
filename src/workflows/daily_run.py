from common import BASE_DIR, TODAY, ensure_dirs
from competitor_collector import run as run_competitors
from daily_content_generator import run as run_daily_content
from hot_topics_collector import run as run_hot_topics
from knowledge_updater import run as run_knowledge_update
from topic_scorer import run as run_topic_scorer
from viral_analyzer import run as run_viral_analyzer
from weekly_review_generator import run as run_weekly_review


def main() -> None:
    ensure_dirs()
    hot_topics_path = run_hot_topics()
    competitors_path = run_competitors()
    viral_analysis_path = run_viral_analyzer()
    scoring_result = run_topic_scorer()
    content_result = run_daily_content()
    knowledge_path = run_knowledge_update()
    weekly_review_path = run_weekly_review()
    print("AI 自媒体增长操作系统全流程已完成。")
    print(f"日期：{TODAY}")
    print(f"热点采集输出：{hot_topics_path}")
    print(f"竞品采集输出：{competitors_path}")
    print(f"爆款拆解输出：{viral_analysis_path}")
    print(f"每日选题输出：{scoring_result['daily_plan']}")
    print(f"每日素材输出：{scoring_result['daily_materials']}")
    print(f"每日脚本输出：{content_result['daily_scripts']}")
    print(f"待办清单输出：{content_result['daily_todo']}")
    print(f"知识库回写：{knowledge_path}")
    print(f"周复盘输出：{weekly_review_path}")
    print(f"项目根目录：{BASE_DIR}")


if __name__ == "__main__":
    main()

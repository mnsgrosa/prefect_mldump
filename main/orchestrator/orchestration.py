from orchestration_tools import scrape_flow, post_flow
from prefect.client.schemas.schedules import CronSchedule, IntervalSchedule

if __name__ == '__main__':
    sumarization = scrape_flow.from_source(
        source = '.',
        entrypoint = './orchestrator/orchestration_tools.py:scrape_flow',
    ).deploy(
        name = 'scrape-cron-deployment',
        work_pool_name = 'my-docker-pool',
        schedule = CronSchedule(
            cron = '0 */2 * * *'
        ),
        build = False
    )

    post_flow.from_source(
        source = '.',
        entrypoint = './orchestrator/orchestration_tools.py:post_flow',
    ).deploy(
        name = 'post-flow',
        work_pool_name = 'my-docker-pool',
        schedule = CronSchedule(
            cron = '10 */2 * * *'
        ),
        build = False
    )
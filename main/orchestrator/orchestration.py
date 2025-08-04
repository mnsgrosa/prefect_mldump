from orchestration_tools import full_flow

if __name__ == '__main__':
    full_flow.from_source(
        source = '.',
        entrypoint = './orchestrator/orchestration_tools.py:full_flow'
    ).deploy(
        name='parent-scrape-post-deployment',
        work_pool_name='my-docker-pool',
        schedule={
            "cron": "0 */2 * * *"
        },
        build=False
    )
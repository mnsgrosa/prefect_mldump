from orchestration_tools import scrape_flow, post_flow

if __name__ == '__main__':
    sumarization = scrape_flow.deploy(
        name = 'scraper-flow',
        work_pool_name = 'my-docker-pool',
        cron = '0 */2 * * *'
    )
    
    post_flow.deploy(
        name = 'post-flow',
        work_pool_name = 'my-docker-pool',
        parameters = {'sumarization': sumarization},
        cron = '0 */2 * * *'
    )
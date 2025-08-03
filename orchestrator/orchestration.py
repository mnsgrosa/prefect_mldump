from orchestration_tools import scrape_flow, post_flow

if __name__ == '__main__':
    sumarization = scrape_flow.serve(
        name = 'scraper-flow',
        cron = '0 */2 * * *'
    )
    
    post_flow.serve(
        name = 'post-flow',
        parameters = {'sumarization': sumarization},
        cron = '0 */2 * * *'
    )
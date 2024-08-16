import requests
from lxml import html

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"
response = requests.get(url)
tree = html.fromstring(response.content)



xp_1 = '/html/body/app-root/app-global-layout/div/div/app-header/header'
xp_2 = '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]'
xp_3 = '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/a'
xp_4 = '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/a'
xp_5 = '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/button[1]'
xp_6 = '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/button[2]'
xp_7 = "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[1]"
xp_8 = '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]'
xp_9 = '/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/h1'
xp_10 = '/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/p'
xp_11 = '/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/button'
xp_12 = '//*[@id="movie_player"]/div[4]/div'
xp_13 = '/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section'
xp_14 = '//*[@id="aboutSection"]'
xp_15 = '//*[@id="aboutSection"]/div/div/div[1]/div/div'
xp_16 = '//*[@id="aboutSection"]/div/div/div[2]/div/div'
xp_17 = '//*[@id="aboutSection"]/div/div/div[1]/div/p[1]'
xp_18 = '//*[@id="aboutSection"]/div/div/div[1]/div/p[2]'
xp_19 = '//*[@id="aboutSection"]/div/div/div[2]/div/p[1]'
xp_20 = '//*[@id="aboutSection"]/div/div/div[2]/div/p[2]'
xp_21 = '//*[@id="contactsSection"]'
xp_22 = '//*[@id="contactsSection"]/div/div/div[1]/h2'
xp_23 = '//*[@id="contactsSection"]/div/div/div[1]/div/a[1]'
xp_24 = '//*[@id="contactsSection"]/div/div/div[1]/div/a[2]'
xp_25 =  '//*[@id="contactsSection"]/div/div/div[1]/div/a[3]'

css_1 = 'body > app-root > app-global-layout > div > div > app-header'
css_2 = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > a'
css_3 = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > a'
css_4 = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > button:nth-child(2)'
css_5 = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > button:nth-child(3)'
css_6 = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_right.d-flex.align-items-center > button.header-link.-guest'
css_7 = 'body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_right.d-flex.align-items-center > button.btn.btn-outline-white.header_signin'
css_8 = 'body > app-root > app-global-layout > div > div > div > app-guest-layout > div > app-home > section'
css_9 = 'body > app-root > app-global-layout > div > div > div > app-guest-layout > div > app-home > section > div > div > div.col-12.col-lg-4 > div'
css_10 = 'body > app-root > app-global-layout > div > div > div > app-guest-layout > div > app-home > section > div > div > div.col-12.col-lg-4 > div > h1'
css_11 = 'body > app-root > app-global-layout > div > div > div > app-guest-layout > div > app-home > section > div > div > div.col-12.col-lg-4 > div > p'
css_12 = 'body > app-root > app-global-layout > div > div > div > app-guest-layout > div > app-home > section > div > div > div.col-12.col-lg-4 > div > button'
css_13 = 'body > app-root > app-global-layout > div > div > div > app-guest-layout > div > app-home > section > div > div > div.col-12.col-lg-8 > div'
css_14 = '#aboutSection'
css_15 = '#aboutSection > div > div > div:nth-child(1) > div > div'
css_16 = '#aboutSection > div > div > div:nth-child(1) > div > p.about-block_title.h2'
css_17 = '#aboutSection > div > div > div:nth-child(1) > div > p.about-block_descr.lead'
css_18 = '#aboutSection > div > div > div.col-12.col-lg-6.mt-lg-0.mt-md-5.mt-sm-4.mt-3 > div > div'
css_19 = '#aboutSection > div > div > div.col-12.col-lg-6.mt-lg-0.mt-md-5.mt-sm-4.mt-3 > div > p.about-block_title.h2'
css_20 = '#aboutSection > div > div > div.col-12.col-lg-6.mt-lg-0.mt-md-5.mt-sm-4.mt-3 > div > p.about-block_descr.lead'
css_21 = '#contactsSection'
css_22 = '#contactsSection > div > div > div.col-md-6.d-flex.flex-column.align-items-center.align-items-md-start > div > a:nth-child(1)'
css_23 = '#contactsSection > div > div > div.col-md-6.d-flex.flex-column.align-items-center.align-items-md-start > div > a:nth-child(2)'
css_24 = '#contactsSection > div > div > div.col-md-6.d-flex.flex-column.align-items-center.align-items-md-start > div > a:nth-child(3)'
css_25 = '#contactsSection > div > div > div.col-md-6.d-flex.flex-column.align-items-center.align-items-md-start > div > a:nth-child(4)'
from hp_rera_code_file import HP_RERA
import pandas as pd


if __name__ == '__main__':
    url = 'https://hprera.nic.in/PublicDashboard'
    driver_path = r"C:\Program Files (x86)\chromedriver.exe"

    with HP_RERA(url, driver_path) as scraper:
        print('main.py k under scraper')
        print(scraper)
        if all([scraper]):
            print('Scraper Present')
            df = pd.DataFrame(scraper)
            df.to_csv(r'C:\Users\user01\Desktop\HP_RERA.csv', index=False)


import main
import bot

def run():
    products = main.collect_data()
    print(f'[INFO] Total found {len(products)} items!')
    bot.post_to_telegram(products)

if __name__ == '__main__':
    run()
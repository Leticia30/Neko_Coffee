class Menu:
    def __init__(self):
        self.coffees = [('エスプレッソ', 350), ('ミルクコーヒー', 400), ('カプチーノ', 450), ('モカ', 500), ('ラテ', 450), ('アメリカーノ', 300), ('アイスコーヒー', 400), ('チョコレートコーヒー', 450), ('クリームコーヒー', 400), ('シナモンコーヒー', 350), ('バニラコーヒー', 400), ('キャラメルコーヒー', 450)]
        self.breads = [('フランスパン', 100), ('チーズパン', 150), ('クロワッサン', 200), ('ベーグル', 250)]
        self.sides = [('バター', 50), ('ジャム', 50), ('クリームチーズ', 100), ('レケジョンチーズスプレッド', 100)]
        self.payments = ['現金','カード']
        self.order = []

    def choose_option(self, options):
        for i, option in enumerate(options):
            if isinstance(option, tuple):
                name, price = option
                print(f'{i + 1} - {name} (¥ {price:.2f})')
            else:
                print(f'{i + 1} - {option}')
        choice = int(input('メニューの番号を選択してください: '))
        return options[choice - 1]

    def show_menu(self):
        print('いらしゃいませ！\n猫のコーヒーをご利用いただきありがとうございます。')
        print('指示に従って正しく注文してください。 \n 注文を一つずつしてください。')
        if input('コーヒーを選択しますか？ (はい/いいえ) ') == 'はい':
            coffee_choice, coffee_price = self.choose_option(self.coffees)
            self.order.append((coffee_choice, coffee_price))

        if input('パンを選択しますか？ (はい/いいえ) ') == 'はい':
            bread_choice, bread_price = self.choose_option(self.breads)
            self.order.append((bread_choice, bread_price))

        if input('サイドメニューを選択しますか？ (はい/いいえ) ') == 'はい':
            side_choice, side_price = self.choose_option(self.sides)
            self.order.append((side_choice, side_price))

        payment_choice = self.choose_option(self.payments)

        total = sum(price for _, price in self.order)

        print('\nお客様の注文:')
        for item, price in self.order:
            print(f'{item} (¥ {price:.2f})')
        print(f'合計: ¥ {total:.2f}')
        print(f'支払方法: {payment_choice}')

menu = Menu()
menu.show_menu()
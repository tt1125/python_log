import xlsxwriter


def test_excel():
    # xlsxwriterでブックを作成
    optbook = xlsxwriter.Workbook("test.xlsx")
    # xlsxwriterでシートを追加
    optsheet = optbook.add_worksheet()
    # 書式を定義
    red = optbook.add_format({"color": "red"})
    # リッチテキストで書き込み
    blue = optbook.add_format({"color": "blue"})
    optsheet.write_rich_string(
        "A1",
        blue,
        "Hello ",
        red,
        "World",
        "!",
    )
    optbook.close()


if __name__ == "__main__":
    test_excel()

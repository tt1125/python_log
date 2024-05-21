import xlsxwriter


def create_format():
    black = "#000000"
    gray = "a5a5a5"
    white = "#ffffff"
    sky = "ccecff"
    deep_bule = "#2e75b5"
    deep_green = "#548135"
    pink = "ffccff"
    orange = "ffc000"
    book = xlsxwriter.Workbook("test.xlsx")
    sheet = book.add_worksheet()

    # セルのフォーマット
    GREEN_CELL = book.add_format(
        {
            "text_wrap": True,
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "color": white,
            "fg_color": deep_green,
        }
    )
    BLUE_CELL = book.add_format(
        {
            "text_wrap": True,
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "color": white,
            "fg_color": deep_bule,
        }
    )
    GRAY_CELL = book.add_format(
        {
            "text_wrap": True,
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "color": white,
            "fg_color": gray,
        }
    )
    SKY_CELL = book.add_format(
        {
            "text_wrap": True,
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "color": black,
            "fg_color": sky,
        }
    )
    ORANGE_CELL = book.add_format(
        {
            "text_wrap": True,
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "color": black,
            "fg_color": orange,
        }
    )

    # セルの大きさを指定
    for i in range(0, 3):
        sheet.set_row(i, 0)
    sheet.set_row(4, 30)
    sheet.set_row(5, 20)
    sheet.set_row(6, 20)
    sheet.set_row(7, 40)

    sheet.set_column("A:A", 0)
    sheet.set_column("B:B", 5)
    sheet.set_column("L:M", 50)
    sheet.set_column("N:N", 20)
    sheet.set_column("U:U", 20)
    sheet.set_column("V:V", 40)
    sheet.set_column("AB:AB", 20)

    # 4行目

    ROW4_FORMAT = [
        ["C4:R4", "規制の洗い出し", GRAY_CELL],
        ["S4:T4", "規制の洗い出し", BLUE_CELL],
        ["U4:AB4", "規制の洗い出し", GREEN_CELL],
    ]

    for cell, value, format in ROW4_FORMAT:
        sheet.merge_range(cell, value, format)

    # 5行目

    ROW5_FORMAT = [
        ["B5:B7", "No.", SKY_CELL],
        ["C5:C7", "所管課", GREEN_CELL],
        ["D5:D7", "担当者", GREEN_CELL],
        ["E5:E7", "連絡先", GREEN_CELL],
        ["F5:F7", "規制区分", BLUE_CELL],
        ["G5:G7", "【非表示】例規集登載順", GRAY_CELL],
        ["H5:H7", "【非表示】リンク設定用", GRAY_CELL],
        ["I5:I7", "例規名", BLUE_CELL],
        ["J5:J7", "制定年番号", BLUE_CELL],
        ["K5:K7", "条項／\n掲載場所", BLUE_CELL],
    ]

    for cell, value, format in ROW5_FORMAT:
        sheet.merge_range(cell, value, format)

    # 作成
    book.close()


if __name__ == "__main__":
    create_format()

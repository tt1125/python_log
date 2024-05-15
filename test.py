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
    for i in range(0, 4):
        sheet.set_row(i, 0)

    for i in range(3, 7):
        sheet.set_row(i, 40)
    sheet.set_row(8, 20)
    sheet.set_column("A:A", 0)
    sheet.set_column("R:S", 50)

    # 4行目

    ROW4_FORMAT = [
        ["D4", " ", GREEN_CELL],
        ["E4", " ", GREEN_CELL],
        ["F4", " ", GREEN_CELL],
        ["G4", " ", BLUE_CELL],
        ["H4", "★", GRAY_CELL],
        ["I4", "★", GRAY_CELL],
        ["J4", " ", GRAY_CELL],
        ["K4", " ", GRAY_CELL],
        ["L4", " ", BLUE_CELL],
        ["M4", " ", BLUE_CELL],
        ["N4", "★", GRAY_CELL],
        ["O4", "★", GRAY_CELL],
        ["P4", "★", GRAY_CELL],
        ["Q4", " ", BLUE_CELL],
        ["R4", "規制の洗い出し", BLUE_CELL],
        ["S4", " ", BLUE_CELL],
    ]

    for cell, value, format in ROW4_FORMAT:
        sheet.write(cell, value, format)

    # 5行目

    ROW5_FORMAT = [
        ["B5:B7", "No.", SKY_CELL],
        ["C5:C7", "ぎょうせい作業用", GRAY_CELL],
        ["D5:D7", "所管課", GREEN_CELL],
        ["E5:E7", "担当者", GREEN_CELL],
        ["F5:F7", "連絡先", GREEN_CELL],
        ["G5:G7", "規制区分", ORANGE_CELL],
        ["H5:H7", "No.", GRAY_CELL],
        ["I5:I7", "ヒットKW\n※一部", GRAY_CELL],
        ["J5:J7", "【非表示】例規集登載順", GRAY_CELL],
        ["K5:K7", "【非表示】リンク設定用", GRAY_CELL],
        ["L5:L7", "例規名", BLUE_CELL],
        ["M5:M7", "制定年番号", BLUE_CELL],
        ["N5:N7", "条等", GRAY_CELL],
        ["O5:O7", "乗番号", GRAY_CELL],
        ["P5:P7", "位置", GRAY_CELL],
        ["Q5:Q7", "条／\n掲載場所", BLUE_CELL],
        ["R5:R7", "規制の洗い出し", SKY_CELL],
        ["S5:S7", "留意事項", SKY_CELL],
    ]

    for cell, value, format in ROW5_FORMAT:
        sheet.merge_range(cell, value, format)

    # 作成
    book.close()


if __name__ == "__main__":
    create_format()

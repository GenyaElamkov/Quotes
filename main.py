import csv


def reads_and_writes_file(read_file: str, finish_file: str) -> None:

    with open(read_file, "r", encoding="utf_8") as start_file, \
            open(finish_file, "w", encoding="utf_8") as final_file:
        content = csv.DictReader(start_file)
        for row in content:
            quote = "Цитата:"
            comment = "Комментарий:"

            if not row['content']:
                quote = ''
            if not row['comment']:
                comment = ''

            print(
                f"{quote}\n{row['content']}\n\n{comment}\n{row['comment']}\n",
                file=final_file)


def main() -> None:
    cvf_file = input("Введите название файла: ")
    text_file = cvf_file.split('.')[0]+'.txt'

    reads_and_writes_file(read_file=cvf_file, finish_file=text_file)


if __name__ == "__main__":
    main()

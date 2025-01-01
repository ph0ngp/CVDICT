import pandas as pd
import unicodedata

def read_cedict(path):
    # Read the file line by line
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Filter out lines that do not match our expected format (lines starting with '#' are likely comments)
    actual_data_lines = [
        line for line in lines if line.strip() and not line.startswith("#")
    ]

    df = get_df_from_lines(actual_data_lines)

    return df, actual_data_lines

def get_df_from_lines(lines):
    traditional_chars = []
    simplified_chars = []
    pinyins = []
    meanings = []

    for line in lines:
        parts = line.split(maxsplit=2)
        traditional_chars.append(parts[0])
        simplified_chars.append(parts[1])

        # this part already asserts the definition format is /.../
        parts2 = parts[2].split("] /", maxsplit=1)
        pinyins.append(parts2[0][1:])
        if parts2[1][-2:] != "/\n":
            raise ValueError(f"Definition format is incorrect: {parts2[1]}")
        definition = parts2[1][:-2]
        if not definition or definition.isspace():
            raise ValueError(f"Definition is empty: {definition}")
        meanings.append(definition)

    df = pd.DataFrame(
        {
            "trad": traditional_chars,
            "simp": simplified_chars,
            "pinyin": pinyins,
            "meaning": meanings,
        }
    )

    return df

def write_vdict():
    file_path = "CVDICT2.u8"
    with open(file_path, 'w') as f:
        f.write('''# Từ điển Hán Việt CVDICT - Chinese-Vietnamese dictionary CVDICT
# https://github.com/ph0ngp/CVDICT
#
# Tác giả: Phong Phan - Published by Phong Phan
#
# Giấy phép - License:
# Creative Commons Attribution-ShareAlike 4.0 International License
# https://creativecommons.org/licenses/by-sa/4.0/
#
# Dự án này dựa trên - This project is based on:
# CC-CEDICT: https://www.mdbg.net/chinese/dictionary?page=cc-cedict
# CEDICT - Copyright (C) 1997, 1998 Paul Andrew Denisowski
#
# Ý kiến đóng góp xin gửi về - For contributions please send to:
# https://github.com/ph0ngp/CVDICT (issue, pull request)
#
#
#
#
#
#
#! version=1.0.1
#! subversion=0
#! format=ts
#! charset=UTF-8
#! entries=122591
#! publisher=Phong Phan
#! license=https://creativecommons.org/licenses/by-sa/4.0/
#! date=2024-12-02T17:46:19Z
#! time=1733161579
''')
    write_df_to_file(vdict, file_path, 'a')

def write_df_to_file(df, path, mode = 'w'):
    with open(path, mode) as f:
        for _, row in df.iterrows():
            f.write(f"{row['trad']} {row['simp']} [{row['pinyin']}] /{row['meaning']}/\n")

vdict, vdict_lines = read_cedict("CVDICT.u8")

vdict['meaning'] = vdict['meaning'].apply(lambda x: unicodedata.normalize('NFC', x))

write_vdict()
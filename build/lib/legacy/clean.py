from pathlib import Path
import sys
import os
import shutil
import file_parser as parser
from normalize import normalize


def hand_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder/normalize(filename.name))


def hand_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder/normalize(filename.name))


def hand_archiv(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_file = target_folder / \
        normalize(filename.name.replace(filename.suffix, ''))
    folder_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_file.resolve()))
    except shutil.ReadError:
        folder_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path) -> None:
    try:
        folder.rmdir()
    except OSError:
        print(f'Sorry, we can not delete the folder: {folder}')


def main(folder: Path) -> None:
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        hand_media(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        hand_media(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        hand_media(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        hand_media(file, folder / 'images' / 'SVG')
    for file in parser.AVI_VIDEO:
        hand_media(file, folder / 'video' / 'AVI')
    for file in parser.MP4_VIDEO:
        hand_media(file, folder / 'video' / 'MP4')
    for file in parser.MOV_VIDEO:
        hand_media(file, folder / 'video' / 'MOV')
    for file in parser.MKV_VIDEO:
        hand_media(file, folder / 'video' / 'MKV')
    for file in parser.DOC_DOCUMENTS:
        hand_media(file, folder / 'video' / 'DOC')
    for file in parser.TXT_DOCUMENTS:
        hand_media(file, folder / 'video' / 'TXT')
    for file in parser.PDF_DOCUMENTS:
        hand_media(file, folder / 'video' / 'PDF')
    for file in parser.XLSX_DOCUMENTS:
        hand_media(file, folder / 'video' / 'XLSX')
    for file in parser.PPTX_DOCUMENTS:
        hand_media(file, folder / 'video' / 'PPTX')
    for file in parser.MP3_AUDIO:
        hand_media(file, folder / 'audio' / 'MP3')
    for file in parser.OGG_AUDIO:
        hand_media(file, folder / 'audio' / 'OGG')
    for file in parser.WAV_AUDIO:
        hand_media(file, folder / 'audio' / 'WAV')
    for file in parser.AMR_AUDIO:
        hand_media(file, folder / 'audio' / 'AMR')

    for file in parser.OTHER:
        hand_media(file, folder / 'OTHER')
    for file in parser.ZIP_ARCHIVES:
        hand_media(file, folder / 'archives' / 'ZIP')
    for file in parser.GZ_ARCHIVES:
        hand_media(file, folder / 'archives' / 'GZ')
    for file in parser.TAR_ARCHIVES:
        hand_media(file, folder / 'archives' / 'TAR')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


if __name__ == '__main__':
    folder_for_scan = Path(sys.argv[1])
    main(folder_for_scan.resolve())

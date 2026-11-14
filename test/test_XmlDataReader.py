# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XmlDataReader import XmlDataReader


class TestXmlDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = """<?xml version="1.0" encoding="UTF-8" ?>
        <root>
            <Иванов_Иван_Иванович>
                <математика>91</математика>
                <русский_язык>100</русский_язык>
                <химия>100</химия>
            </Иванов_Иван_Иванович>
        </root>"""
        data = {
            "Иванов_Иван_Иванович": [("математика", 91),
                                     ("русский_язык", 100), ("химия", 100)]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content,
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("xmldatadir").join("data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data) -> None:
        file_content = XmlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

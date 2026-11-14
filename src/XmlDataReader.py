# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from src.Types import DataType
from src.DataReader import DataReader

class XmlDataReader(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()
        for student_elem in root:
            student_name = student_elem.tag.strip()
            self.students[student_name] = []            
            for subject_elem in student_elem:
                subject_name = subject_elem.tag.strip()
                score = int(subject_elem.text.strip())
                self.students[student_name].append((subject_name, score))
        return self.students
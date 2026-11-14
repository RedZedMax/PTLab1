# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.QuartileAnalysis import QuartileAnalysis


class TestQuartileAnalysis:

    @pytest.fixture()
    def sample_data(self) -> DataType:
        return {
            "Студент 1": [("математика", 100)],
            "Студент 2": [("математика", 80)],
            "Студент 3": [("математика", 60)],
            "Студент 4": [("математика", 40)],
            "Студент 5": [("математика", 20)],
        }

    def test_get_first_quartile_students(self, sample_data: DataType) -> None:
        analyzer = QuartileAnalysis(sample_data)
        result = analyzer.get_first_quartile_students()
        assert "Студент 4" in result
        assert "Студент 5" in result
        assert len(result) == 2

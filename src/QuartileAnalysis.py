# -*- coding: utf-8 -*-
import statistics
from src.CalcRating import CalcRating
from src.Types import DataType

RatingType = dict[str, float]


class QuartileAnalysis:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def get_first_quartile_students(self) -> list[str]:
        self.rating = CalcRating(self.data).calc()

        if not self.rating:
            return []

        scores = list(self.rating.values())

        if len(scores) < 2:
            return list(self.rating.keys())

        q1_threshold = statistics.quantiles(scores, n=4)[0]

        return [
            student for student, score in self.rating.items()
            if score <= q1_threshold
        ]

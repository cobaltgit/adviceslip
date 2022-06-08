import datetime
from typing import Iterable, Iterator, Optional, Tuple


class Slip:
    """Slip object returned by the API. Contains the slip ID, advice and an optional date attribute"""

    __slots__: Tuple[str] = ("id", "advice", "date")

    def __init__(self, *, id: int, advice: str, date: Optional[datetime.date] = None) -> None:
        self.id: int = id
        self.advice: str = advice
        self.date: Optional[datetime.date] = date

    def __str__(self) -> str:
        """Returns the advice in the slip"""
        return self.advice

    def __repr__(self) -> str:
        """Returns a clean representation of the slip object"""
        return f"<Search id={self.id} advice={self.advice!r}>"


class Search:
    """Search object returned by the API. Contains the amount of results, the query itself and an iterable of slip objects"""

    __slots__: Tuple[str] = ("total_results", "query", "slips")

    def __init__(self, *, total_results: int, query: str, slips: Iterable[Slip]) -> None:
        self.total_results: int = total_results
        self.query: str = query
        self.slips: Iterable[Slip] = slips

    def __repr__(self) -> str:
        """Returns a clean representation of the search object"""
        return f"<Search total_results={self.total_results} query={self.query!r}>"

    def __iter__(self) -> Iterator[Slip]:
        """Returns an iterator over the search results"""
        return iter(self.slips)

from .MPI import Intracomm
from typing import Optional
from typing import Sequence
from typing import List, Tuple

def helloworld(comm: Intracomm, args: Optional[Sequence[str]] = None, verbose: bool = True) -> str: ...
def ringtest(comm: Intracomm, args: Optional[Sequence[str]] = None, verbose: bool = True) -> float: ...
def pingpong(comm: Intracomm, args: Optional[Sequence[str]] = None, verbose: bool = True) -> List[Tuple[int, float, float]]: ...
def futures(comm: Intracomm, args: Optional[Sequence[str]] = None, verbose: bool = True) -> List[Tuple[int, float, float]]: ...
def main(args: Optional[Sequence[str]] = ...) -> None: ...

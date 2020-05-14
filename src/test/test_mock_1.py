import pytest
from src.main.Journey import Journey


@pytest.mark.parametrize("n_passatgers", "desti_1", "desti_2", "desti_3", "desti_4", "vol_1", "vol_2", "vol_3",
                         "vol_4", "vol_5"[

                         ])

def test_prova(n_passatgers: int, desti_1: str, desti_2: str):


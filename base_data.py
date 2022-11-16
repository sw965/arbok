import os
import boa
import path

ALL_POKE_NAMES = boa.readlines_txt(path.ALL_POKE_NAMES, True)
ALL_MOVE_NAMES = boa.readlines_txt(path.ALL_MOVE_NAMES, True)
HALF_HEAL_MOVE_NAMES = boa.readlines_txt(path.HALF_HEAL_MOVE_NAMES, True)
assert set(HALF_HEAL_MOVE_NAMES).issubset(ALL_MOVE_NAMES)
ONE_HIT_KO_MOVE_NAMES = boa.readlines_txt(path.ONE_HIT_KO_MOVE_NAMES, True)
assert set(ONE_HIT_KO_MOVE_NAMES).issubset(ALL_MOVE_NAMES)
TWO_ATTACK_MOVE_NAMES = boa.readlines_txt(path.TWO_ATTACK_MOVE_NAMES, True)
assert set(TWO_ATTACK_MOVE_NAMES).issubset(ALL_MOVE_NAMES)
MIN_TWO_MAX_FIVE_ATTACK_MOVE_NAMES = boa.readlines_txt(path.MIN_TWO_MAX_FIVE_ATTACK_MOVE_NAMES, True)
assert set(MIN_TWO_MAX_FIVE_ATTACK_MOVE_NAMES).issubset(ALL_MOVE_NAMES)
MAX_THREE_ATTACK_MOVE_NAMES = boa.readlines_txt(path.MAX_THREE_ATTACK_MOVE_NAMES, True)
assert set(MAX_THREE_ATTACK_MOVE_NAMES).issubset(ALL_MOVE_NAMES)

ALL_NATURES = boa.readlines_txt(path.ALL_NATURES, True)
ALL_ITEMS = boa.readlines_txt(path.ALL_ITEMS, True)
ALL_TYPES = boa.readlines_txt(path.ALL_TYPES, True)
assert len(ALL_TYPES) == 18

POKEDEX = {poke_name:boa.load_json(path.POKEDEX + poke_name + ".json") for poke_name in ALL_POKE_NAMES}
assert set(POKEDEX.keys()) == set(ALL_POKE_NAMES)
MOVEDEX = {move_name:boa.load_json(path.MOVEDEX + move_name + ".json") for move_name in ALL_MOVE_NAMES}
assert set(MOVEDEX.keys()) == set(ALL_MOVE_NAMES)
NATUREDEX = boa.load_json(path.NATUREDEX)
assert set(NATUREDEX.keys()) == set(ALL_NATURES)

TYPEDEX = boa.load_json(path.TYPEDEX)
assert set(TYPEDEX.keys()) == set(ALL_TYPES)
assert all([set(v.keys()) == set(ALL_TYPES) for v in TYPEDEX.values()])

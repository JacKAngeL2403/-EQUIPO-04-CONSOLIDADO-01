"""Excepciones personalizadas del dominio de Pixel-Quest."""


class PixelQuestError(Exception):
    """Excepción base de todo el juego."""


class InvalidNameError(PixelQuestError):
    """El nombre está vacío o supera el largo permitido."""


class InvalidStatError(PixelQuestError):
    """Una estadística (HP, ataque, valor...) tiene un valor inválido."""


class InventoryFullError(PixelQuestError):
    """El inventario alcanzó su capacidad máxima."""


class ItemNotFoundError(PixelQuestError):
    """No existe un objeto en la posición indicada."""


class InvalidItemError(PixelQuestError):
    """El objeto no se puede usar/equipar de esa forma."""


class NotEnoughGoldError(PixelQuestError):
    """El héroe no tiene oro suficiente."""


class CombatError(PixelQuestError):
    """Acción de combate no permitida."""


class HeroNotFoundError(PixelQuestError):
    """No existe un héroe guardado con ese nombre."""


class DuplicateHeroError(PixelQuestError):
    """Ya existe un héroe con ese nombre."""


class SaveDataError(PixelQuestError):
    """El archivo de guardado está dañado o no se pudo leer/escribir."""


class PartyError(PixelQuestError):
    """Operación de grupo no válida (compañero repetido, índice inexistente...)."""


class PartyFullError(PartyError):
    """El grupo ya tiene el máximo de compañeros."""

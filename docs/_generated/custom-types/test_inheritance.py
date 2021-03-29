from platonic.sqs.queue import SQSReceiver, SQSSender


class Spell:
    """Magical spell."""

    def __init__(self, text: str) -> None:
        """Initialize."""
        self.text = text


class SpellSender(SQSSender[Spell]):
    """Spell sender."""

    def serialize_value(self, spell: Spell) -> str:
        """Serialize a spell."""
        return spell.text


class SpellReceiver(SQSReceiver[Spell]):
    """Spell receiver."""

    def deserialize_value(self, raw_value: str) -> Spell:
        """Deserialize a spell."""
        return Spell(text=raw_value)


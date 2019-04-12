from app.parser import clear_spaces

def test_parser_can_clean_spaces():
    result = clear_spaces("   Bonjour tout le monde")
    assert result == "Bonjourtoutlemonde"

from doc_ocr.pipeline import character_error_rate, word_error_rate, edit_distance

def test_exact_match_has_zero_error():
    assert character_error_rate("hello world", "hello world") == 0
    assert word_error_rate("hello world", "hello world") == 0

def test_whitespace_is_normalised():
    assert character_error_rate("hello\nworld", "hello   world") == 0

def test_edit_distance():
    assert edit_distance("kitten", "sitting") == 3

def test_error_is_positive_for_mismatch():
    assert character_error_rate("invoice", "inv0ice") > 0

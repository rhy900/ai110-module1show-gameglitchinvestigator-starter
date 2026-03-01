from logic_utils import check_guess

# def test_winning_guess():
#     # If the secret is 50 and guess is 50, it should be a win
#     result = check_guess(50, 50)
#     assert result == "Win"

# def test_guess_too_high():
#     # If secret is 50 and guess is 60, hint should be "Too High"
#     result = check_guess(60, 50)
#     assert result == "Too High"

# def test_guess_too_low():
#     # If secret is 50 and guess is 40, hint should be "Too Low"
#     result = check_guess(40, 50)
#     assert result == "Too Low"


# --- Fixed versions of the tests above --- using claude code 
# check_guess returns a tuple (outcome, message), not just a string.
# The original tests above compare the whole tuple to a string, which always fails.

def test_winning_guess_fixed():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high_fixed():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low_fixed():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- New tests covering the bugs that were fixed ---

# Bug 1: hints were swapped — when guess is too high, the message should say LOWER
def test_too_high_message_says_lower():
    # Reproduces the user's exact experience: secret=29, guess=70
    outcome, message = check_guess(70, 29)
    assert outcome == "Too High"
    assert "LOWER" in message

# Bug 1: when guess is too low, the message should say HIGHER
def test_too_low_message_says_higher():
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

# Bug 2: both inputs are ints — numerical comparison, not alphabetical string comparison
def test_numerical_comparison_not_alphabetical():
    # "9" > "10" alphabetically, but 9 < 10 numerically.
    # With string comparison (the bug), check_guess(9, 10) would wrongly return "Too High".
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low"

# Winning still works correctly
def test_win_message_content():
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"
    assert "Correct" in message

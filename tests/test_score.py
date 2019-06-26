from app.tennis import Tennis


def test_should_return_0_0_when_no_player_has_scored():
    # Given
    tennis = Tennis()

    # When
    score = tennis.get_score()

    # Then
    assert score == "0-0"


def test_should_return_15_0_when_player_1_scored_once():
    # Given
    tennis = Tennis()

    # When
    tennis.add_point_player_1()
    score = tennis.get_score()

    # Then
    assert score == "15-0"


def test_should_return_30_0_when_player_1_scored_twice():
    # Given
    tennis = Tennis()

    # When
    tennis.add_point_player_1()
    tennis.add_point_player_1()
    score = tennis.get_score()

    # Then
    assert score == "30-0"


def test_should_return_40_0_when_player_1_scored_three_times():
    # Given
    tennis = Tennis()

    # When
    tennis.add_point_player_1()
    tennis.add_point_player_1()
    tennis.add_point_player_1()
    score = tennis.get_score()

    # Then
    assert score == "40-0"


def test_should_return_0_15_when_player_2_scored_once():
    # Given
    tennis = Tennis()

    # When
    tennis.add_point_player_2()
    score = tennis.get_score()

    # Then
    assert score == "0-15"


def test_should_return_0_30_when_player_2_scored_twice():
    # Given
    tennis = Tennis()

    # When
    tennis.add_point_player_2()
    tennis.add_point_player_2()
    score = tennis.get_score()

    # Then
    assert score == "0-30"


def test_should_return_0_40_when_player_2_scored_three_times():
    # Given
    tennis = Tennis()

    # When
    tennis.add_point_player_2()
    tennis.add_point_player_2()
    tennis.add_point_player_2()
    score = tennis.get_score()

    # Then
    assert score == "0-40"


def test_should_return_egalite_when_both_scored_three_times():
    # Given
    tennis = Tennis()

    # When
    tennis.add_point_player_1()
    tennis.add_point_player_1()
    tennis.add_point_player_1()
    tennis.add_point_player_2()
    tennis.add_point_player_2()
    tennis.add_point_player_2()
    score = tennis.get_score()

    # Then
    assert score == "Egalité"


def test_should_return_egalite_when_both_scored_four_times():
    # Given
    tennis = Tennis()

    # When
    tennis.add_point_player_1()
    tennis.add_point_player_1()
    tennis.add_point_player_1()
    tennis.add_point_player_2()
    tennis.add_point_player_2()
    tennis.add_point_player_2()
    tennis.add_point_player_1()
    tennis.add_point_player_2()
    score = tennis.get_score()

    # Then
    assert score == "Egalité"

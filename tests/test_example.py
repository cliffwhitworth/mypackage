def test_example_returns_string(example_test):
    # Given
    # When
    # Then
    assert example_test == 'hello world!'

def test_example_returns_version():
    # Given
    from pathlib import Path
    import mypackage

    PACKAGE_ROOT = Path(mypackage.__file__).resolve().parent

    # When
    with open(PACKAGE_ROOT / 'VERSION') as f:
        __version__ = f.read().strip()

    # Then
    assert mypackage.__version__ == __version__
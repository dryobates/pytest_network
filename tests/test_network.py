import pytest


def test_disable_network_fixture_raiese_exception(testdir):
    testdir.makepyfile(
        """
        import urllib.request

        import pytest


        def test_hello_default(disable_network):
            with pytest.raises(Exception):
                urllib.request.urlopen('http://httpbin.org/robots.txt')
        """
    )

    result = testdir.runpytest('--verbose')

    assert result.parseoutcomes() == {'passed': 1}


@pytest.mark.usefixtures('disable_network_addopt')
def test_disable_network_addopt_raises_exception(testdir):
    testdir.makepyfile(
        """
        import urllib.request
        
        import pytest


        def test_hello_default():
            with pytest.raises(Exception):
                urllib.request.urlopen('http://httpbin.org/robots.txt')
        """
    )

    result = testdir.runpytest('--verbose')

    assert result.parseoutcomes() == {'passed': 1}


@pytest.mark.usefixtures('disable_network_addopt')
def test_enable_network_fixture_enables_connect(testdir):
    testdir.makepyfile(
        """
        import urllib.request

        import pytest


        def test_hello_default(enable_network):
            response = urllib.request.urlopen('http://httpbin.org/robots.txt')

            assert response.status == 200
        """
    )

    result = testdir.runpytest('--verbose')

    assert result.parseoutcomes() == {'passed': 1}

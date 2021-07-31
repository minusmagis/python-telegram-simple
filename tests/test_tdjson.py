from unittest.mock import Mock, patch

from telegram_simple.tdjson import _get_tdjson_lib_path


class TestGetTdjsonTdlibPath:
    def test_for_darwin(self):
        mocked_system = Mock(return_value='Darwin')
        mocked_resource = Mock()

        with patch('telegram_simple.tdjson.platform.system', mocked_system):
            with patch(
                'telegram_simple.tdjson.pkg_resources.resource_filename', mocked_resource
            ):
                _get_tdjson_lib_path()

        mocked_resource.assert_called_once_with(
            'telegram_simple', 'lib/darwin/libtdjson.dylib'
        )

    def test_for_linux(self):
        mocked_system = Mock(return_value='Linux')
        mocked_resource = Mock(return_value='/tmp/')

        with patch('telegram_simple.tdjson.platform.system', mocked_system):
            with patch(
                'telegram_simple.tdjson.pkg_resources.resource_filename', mocked_resource
            ):
                _get_tdjson_lib_path()

        mocked_resource.assert_called_once_with('telegram_simple', 'lib/linux/libtdjson.so')

    def test_for_windows(self):
        mocked_system = Mock(return_value='Windows')
        mocked_resource = Mock(return_value='/tmp/')

        with patch('telegram_simple.tdjson.platform.system', mocked_system):
            with patch(
                'telegram_simple.tdjson.pkg_resources.resource_filename', mocked_resource
            ):
                _get_tdjson_lib_path()

        mocked_resource.assert_called_once_with('telegram_simple', 'lib/linux/libtdjson.so')

    def test_unknown(self):
        mocked_system = Mock(return_value='Unknown')
        mocked_resource = Mock(return_value='/tmp/')

        with patch('telegram_simple.tdjson.platform.system', mocked_system):
            with patch(
                'telegram_simple.tdjson.pkg_resources.resource_filename', mocked_resource
            ):
                _get_tdjson_lib_path()

        mocked_resource.assert_called_once_with('telegram_simple', 'lib/linux/libtdjson.so')

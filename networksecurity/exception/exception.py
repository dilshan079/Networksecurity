import sys
from networksecurity.logging import logger


def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename

    return (
        f"Error occurred in Python script: {file_name} "
        f"at line {exc_tb.tb_lineno}: {error}"
    )


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(
            error_message,
            error_detail
        )
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

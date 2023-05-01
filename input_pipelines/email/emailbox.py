from input_pipelines.input_pipeline import InputPipeline, OnMessageReceive
from input_pipelines.email.login_details import mail_address, mail_host, password
from imaplib import IMAP4
from datetime import datetime
from input_pipelines.message import Message
from typing import List, Union
from email.header import decode_header
from email import message_from_bytes


# TODO(Ido): decide between two possible options - always delete the mail, or hold last open

class EmailBox(InputPipeline):
    text_destination = mail_address
    _MIN_FETCH_INBOX_TIME = 50
    __slots__ = ["__connection", "__last_time_email_checked", "__num_emails", "__inbox_fetch_time"]

    def __init__(self, on_email_receive: OnMessageReceive=None, last_time_emails_checked: Union[datetime, None] = None):
        super().__init__(on_email_receive)
        self.__connection = self.__connect_to_email_server()
        self.__last_time_email_checked = last_time_emails_checked
        self.__fetch_emails()

    @staticmethod
    def __connect_to_email_server() -> IMAP4:
        mail_connection = IMAP4(host=mail_host)
        mail_connection.login(user=mail_address, password=password)
        return mail_connection

    def __fetch_emails(self):
        if (datetime.now() - self.__inbox_fetch_time).seconds < self._MIN_FETCH_INBOX_TIME:
            return
        status, emails_data = self.__connection.select("INBOX")
        self.__num_emails = int(emails_data[0], 0)
        # TODO(Ido): implement status check
        self.__inbox_fetch_time = datetime.now()

    def __get_messages_in_window(self, start_of_window: datetime, end_of_window: datetime) -> List[Message]:
        self.__fetch_emails()
        messages = []
        for i in range(self.__num_emails, 0, -1):
            res, message = self.__connection.fetch(str(i), "(RFC822)")
            for response in message:
                if type(response) is tuple:
                    msg = message_from_bytes(response[1])
                    date = decode_header(msg["Date"])[0][0]
                    print(date)

    def get_new_messages(self, client_id:str) -> List[Message]:
        return self.__get_messages_in_window(self.__last_time_email_checked, datetime.now())

from django.core.mail.backends.smtp import EmailBackend

class PatchedEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def open(self):
        """
        Open a network connection. Override to avoid passing keyfile/certfile to starttls().
        """
        if self.connection:
            return False

        connection_params = {
            'host': self.host,
            'port': self.port,
            'timeout': self.timeout,
        }

        # ✅ Safely handle missing local_hostname
        if hasattr(self, 'local_hostname'):
            connection_params['local_hostname'] = self.local_hostname

        self.connection = self.connection_class(**connection_params)

        if self.use_tls:
            self.connection.ehlo()
            self.connection.starttls()
            self.connection.ehlo()

        if self.username and self.password:
            self.connection.login(self.username, self.password)

        return True

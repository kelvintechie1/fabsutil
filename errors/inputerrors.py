class InvalidTemplateException(Exception):
    def __init__(self, fileName):
        self.message = f"Syntax error in template {fileName}"
        super().__init__(self.message)
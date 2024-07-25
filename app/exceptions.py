from rest_framework.exceptions import APIException


class ChallengeTransactionException(APIException):
    status_code = 400

    def __init__(self, detail="You can do a challenge just once"):
        self.default_code = "challenge_transaction_exception"
        super().__init__(detail, self.default_code)
        self.default_detail = detail


class ChallengeTransactionInvalidData(APIException):
    status_code = 400

    def __init__(self, detail="challenge item ids are missing"):
        self.default_code = "challenge_transaction_exception"
        super().__init__(detail, self.default_code)
        self.default_detail = detail

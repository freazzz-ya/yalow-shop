class Constants:
    CHARFIELD = 256
    TEXTFIELD = 1000
    INT_FIELD_MAX_VALUE = 1000000000
    INT_FIELD_MIN_VALUE = 0


class HelpText:
    CATEGORIES_TITLE = 'WRITE A UNIQUE CATEGORIES' \
                       ' MAX lenght 256 symm'
    CATEGORIES_DESCRIPTION = 'Something information about' \
                             ' category'


class UserModelConstant(Constants):
    """Константы для модели User."""

    DEFAULT_TEXT_FOR_DESCRIPTION = "Данный пользователь ничего "\
                                   "о себе не написал, " \
                                   "но мы уверены, что это очень "\
                                   "хороший и позитивный человек, " \
                                   "который скоро добьется финансовых успехов."
    DEFAULT_TEXT_FOR_COMMENT = "Дефолтное описание для комментария"

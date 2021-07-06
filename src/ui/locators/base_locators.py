class BaseLocators:

    @classmethod
    def upd_loc(cls, locator: list, replacements: list):
        for value in replacements:
            locator[1] = locator[1].replace('%s', value)
        return locator

class BaseLocators:

    @classmethod
    def upd_loc(cls, locator: list, replacement: str):
        locator[1] = locator[1].replace('%s', replacement)
        return locator

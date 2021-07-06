class BaseLocators:

    @classmethod
    def upd_loc(cls, locator: list, replacements: list):
        loc = locator.copy()
        for value in replacements:
            loc[1] = loc[1].replace('%s', value, 1)
        return loc

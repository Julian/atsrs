import attr


class Loader:
    def one_from_string(self, string):
        return attr.make_class("Alert", attrs={"error": attr.ib()})

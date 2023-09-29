from pathlib import Path

from tree_sitter import Language, Parser
import attr


_PARENT = Path(__file__).parent
SO_PATH = _PARENT / "build/atsree-sitter.so"
TS_PATH = _PARENT.parent / "vendor/tree-sitter-typescript/typescript"


def _parser():
    Language.build_library(str(SO_PATH), [str(TS_PATH)])
    parser = Parser()
    parser.set_language(Language(str(SO_PATH), "typescript"))
    return parser


@attr.define()
class Loader:

    _parser = attr.field(factory=_parser)

    def one_from_bytes(self, string):
        tree = self._parser.parse(string)
        import pudb; pu.db
        return attr.make_class("Alert", attrs={"error": attr.ib()})

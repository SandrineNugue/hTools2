# [h] interpolate selected glyphs

import hTools2
reload(hTools2)

if hTools2.DEBUG:
    import hTools2.dialogs
    reload(hTools2.dialogs)

from hTools2.dialogs import interpolateGlyphsDialog

interpolateGlyphsDialog()

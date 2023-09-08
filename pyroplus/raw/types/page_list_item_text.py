#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyroplus.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyroplus.raw.core import TLObject
from pyroplus import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class PageListItemText(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyroplus.raw.base.PageListItem`.

    Details:
        - Layer: ``158``
        - ID: ``B92FB6CD``

    Parameters:
        text (:obj:`RichText <pyroplus.raw.base.RichText>`):
            N/A

    """

    __slots__: List[str] = ["text"]

    ID = 0xb92fb6cd
    QUALNAME = "types.PageListItemText"

    def __init__(self, *, text: "raw.base.RichText") -> None:
        self.text = text  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageListItemText":
        # No flags
        
        text = TLObject.read(b)
        
        return PageListItemText(text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        return b.getvalue()
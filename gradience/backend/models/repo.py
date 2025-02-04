# repo.py
#
# Change the look of Adwaita, with ease
# Copyright (C) 2022 Gradience Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os

from gradience.backend.utils.common import to_slug_case
from gradience.backend.globals import presets_dir
from gradience.backend.models.preset import Preset


class Repo:
    presets = {}

    def __init__(self, name):
        self.name = to_slug_case(name)
        self.path = os.path.join(presets_dir, name)
        self.presets = self.get_presets()

    def get_presets(self):
        presets = {}
        for preset in os.listdir(self.path):
            if preset.endswith(".json"):
                preset_path = os.path.join(self.path, preset)
                presets[preset[:-5]] = Preset().new_from_path(preset_path)
        return presets

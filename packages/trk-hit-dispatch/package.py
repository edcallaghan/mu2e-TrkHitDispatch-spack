# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from pathlib import Path
from spack.package import *


class TrkHitDispatch(CMakePackage):
    homepage = "https://mu2e.fnal.gov"
    git = "https://github.com/edcallaghan/mu2e-TrkHitDispatch"

    maintainers("edcallaghan")

    license("Apache-2.0")

    #version("main", branch="main", get_full_repo=True)
    version("main", branch="main")

    variant(
        "cxxstd",
        default="20",
        values=("14", "17", "20"),
        multi=False,
        sticky=True,
        description="Use the specified C++ standard when building.",
    )

    # Direct dependencies
    depends_on("Offline")

    def cmake_args(self):
        args = [self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd")]
        args += ['-DCMAKE_BUILD_TYPE=Debug']
        return args

    def setup_run_environment(self, env):
        prefix = self.prefix
        env.set("EN_DIR", prefix)
        env.prepend_path("CET_PLUGIN_PATH", prefix.lib)

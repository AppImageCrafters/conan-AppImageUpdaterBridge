#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    remotes = [("https://api.bintray.com/conan/bincrafters/public-conan", "yes", "bincrafters"),
               ("https://api.bintray.com/conan/conan-community/conan", "yes", "conan-community")]

    builder = ConanMultiPackager(build_policy="outdated", remotes=remotes, build_types=["Release"], archs=["x86_64"])
    builder.add_common_builds(shared_option_name="AppImageUpdaterBridge:shared")
    builder.run()

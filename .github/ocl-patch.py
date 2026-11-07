import sys
p = sys.argv[1] + "/src/metal/adapter.rs"
s = open(p).read()
anchor = "        Self {\n            msl_version,\n"
assert s.count(anchor) == 1, "anchor"
cap = ("        // A GPU without the Metal 3 family on macOS 15+ only happens on Macs run with OpenCore\n"
       "        // Legacy Patcher, whose older Metal compiler rejects the OS's newest MSL standard\n"
       "        // (\"invalid value 'metal3.2'\"). MSL 2.4 is what that hardware last shipped with.\n"
       "        let msl_version = if os_type == super::OsType::Macos\n"
       "            && !metal3\n"
       "            && msl_version > MTLLanguageVersion::Version2_4\n"
       "        {\n"
       "            MTLLanguageVersion::Version2_4\n"
       "        } else {\n"
       "            msl_version\n"
       "        };\n\n")
open(p, "w").write(s.replace(anchor, cap + anchor))
print("patched", p)

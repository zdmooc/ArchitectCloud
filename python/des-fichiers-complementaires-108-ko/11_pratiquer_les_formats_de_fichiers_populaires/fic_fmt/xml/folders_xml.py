import xmltodict

mon_dict = { "solution": { 
            "folders": { 
                "folder": [
                {
                    "Dossier" : "FINAN",
                    "Version" : "R090.013",
                    "Release" : "90",
                    "Patch"   : "13",
                    "Update"  : "17/10/2019"
                },
                {
                    "Dossier" : "SEED",
                    "Version" : "R090.013",
                    "Release" : "90",
                    "Patch"   : "13",
                    "Update"  : "17/10/2019"
                },
                {
                    "Dossier" : "X3",
                    "Version" : "R090.013",
                    "Release" : "90",
                    "Patch"   : "13",
                    "Update"  : "17/10/2019"
                }
            ]
        }
    }
}

print( xmltodict.unparse(mon_dict, pretty=True) )

import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\LPA\Projects\FrameworkProject\FrameworkProject.gdb"
countryName = arcpy.GetParameterAsText(0)
arcpy.analysis.Select(r"C:\LPA\Data\ne_10m_admin_0_countries.shp",
                      r"C:\LPA\Projects\FrameworkProject\FrameworkProject.gdb\SelCountry",
                      f"NAME = '{countryName}'")
arcpy.analysis.Buffer("SelCountry",
                      "SelCountry_Buffer",
                      "200 Kilometers",
                      "FULL",
                      "ROUND",
                      "NONE",
                      None,
                      "PLANAR")
arcpy.analysis.Clip(r"C:\LPA\Data\ne_10m_populated_places.shp",
                    "SelCountry_Buffer",
                    "Places_Clip",
                    None)
arcpy.AddMessage(f"There are {arcpy.management.GetCount('Places_Clip')} populated places in or within 200km of {countryName}")



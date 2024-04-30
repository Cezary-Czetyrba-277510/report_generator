import sys, os
sys.path.append("/report_generator/report_3")
import Generator.Generator
print(os.path.join("report_generator/report_3/data/test/", "rura.csv"))
rura_data = Generator.Generator("report_3/data/test/", "rura.csv") # type: ignore
print(rura_data.data_set)

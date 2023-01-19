# Import the main class for creating a kerykeion instance:
from kerykeion import print_all_data, KrInstance, MakeSvgInstance

# Create a kerykeion instance:
# Args: Name, year, month, day, hour, minuts, city, nation(optional)

people=[
		("Ivo (m)", 1987, 6, 10, 15, 30, "Buenos Aires, Argentina"),
		("Adams Patch (m)", 1945, 5, 28, 20, 15, "Washington, DC (US)"),
		("Solar Xul (m)", 1887, 12, 14, 11, 20, "San Fernando, Buenos Aires, Argentina"),
		("leo", 1966, 1, 21, 6, 30, "General Roca, Rio Negro, Argentina")
	]

for aPerson in people:
	print(aPerson)
	chart = KrInstance(aPerson[0], aPerson[1], aPerson[2], aPerson[3], aPerson[4], aPerson[5], aPerson[6])
	print_all_data(chart)
	print(chart.sun)
	print(chart.first_house)
	print(chart.moon.get("element",1))
	name = MakeSvgInstance(chart, chart_type="Natal",  lang= "ES")
	name.set_output_directory(".")
	name.makeSVG()
	print(len(name.aspects_list))


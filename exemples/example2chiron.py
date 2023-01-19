from kerykeion import KrInstance, MakeSvgInstance

first = KrInstance("Jack", 1990, 6, 15, 15, 15, "Roma")
second = KrInstance("Jane", 1991, 10, 25, 21, 00, "Roma")

# Set the type, it can be Natal, Composite or Transit

name = MakeSvgInstance(first, chart_type="Composite", second_obj=second, lang= "ES")
name.set_output_directory(".")
name.makeSVG()
print(len(name.aspects_list))


leo = KrInstance("Leo", 1966, 1, 21, 6, 30, "General Roca, Rio Negro")


# Set the type, it can be Natal, Composite or Transit
# Literal['Natal', 'Composite', 'Transit'] = 'Natal',
name = MakeSvgInstance(leo, chart_type="Natal",  lang= "ES")
name.set_output_directory(".")
name.makeSVG()
print(len(name.aspects_list))


#> Generating kerykeion object for Jack...
#> Generating kerykeion object for Jane...
#> Jack birth location: Roma, 41.89193, 12.51133
#> SVG Generated Correctly
#> 38



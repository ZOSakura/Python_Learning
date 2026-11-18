import Ciricle_Funtion
s_radius = 10
m_radius = 15
l_radius = 20
small_area = Ciricle_Funtion.circle_area(s_radius)
medium_area = Ciricle_Funtion.circle_area(m_radius)
large_area = Ciricle_Funtion.circle_area(l_radius)
small_cost = small_area * 0.05
medium_cost = medium_area * 0.05
large_cost = large_area * 0.05
print(small_area, small_cost)
print(medium_area, medium_cost)
print(large_area, large_cost)
print("\n")

import My_Function
print(__name__)
print(My_Function.PI)
print(My_Function.NAME)
My_Function.log_separator1()
My_Function.log_separator2()
My_Function.log_separator3()
My_Function.log_separator4()
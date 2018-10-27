# -*- coding: utf-8 -*-

import io

def loadFile(fileName):
	with open(fileName, "r") as file:
		lines = file.readlines()

	names = []
	data = {}

	for line in lines:
		words = line.split()

		if len(words) > 0:
			if len(names) == 0:
				if words[0] == "alpha":
					names = words
					for n in names:
						data[n] = []
			else:
				for i, v in enumerate(map(float, words)):
					data[names[i]].append(v)				

	return data

base = loadFile(u"polars/base_T1-30_0 m_s-VLM2-34_9kg-x0_0mm-TG.txt")
baseBeta = loadFile(u"polars/base_T5-a0_0°-30_0m_s-VLM2-34_9kg-x0_0mm-TG.txt")
elevatorMinus10 = loadFile(u"polars/elevator -10_T1-30_0 m_s-VLM2-34_9kg-x0_0mm-TG.txt")
elevatorPlus10 = loadFile(u"polars/elevator 10_T1-30_0 m_s-VLM2-34_9kg-x0_0mm-TG.txt")
flaps15 = loadFile(u"polars/flaps 15_T1-30_0 m_s-VLM2-34_9kg-x0_0mm-TG.txt")
flaps30 = loadFile(u"polars/flaps 30_T1-30_0 m_s-VLM2-34_9kg-x0_0mm-TG.txt")
leftAileronMinus12 = loadFile(u"polars/left aileron -12_T1-30_0 m_s-VLM2-34_9kg-x0_0mm-TG.txt")
leftAileronMinus5 = loadFile(u"polars/left aileron -5_T1-30_0 m_s-VLM2-34_9kg-x0_0mm-TG.txt")
leftAileronPlus10 = loadFile(u"polars/left aileron 10_T1-30_0 m_s-VLM2-34_9kg-x0_0mm-TG.txt")
leftAileronPlus5 = loadFile(u"polars/left aileron 5_T1-30_0 m_s-VLM2-34_9kg-x0_0mm-TG.txt")
rudder10 = loadFile(u"polars/rudder 10_T1-30_0 m_s-VLM2-34_9kg-x0_0mm-TG.txt")

print('<?xml version="1.0"?>')
print('<aerodynamics>\n')

print('	<axis name="LIFT">\n')	# ------- LIFT ----------------------------

print('		<function name="aero/force/lift-due-to-alpha-and-flaps">')
print('			<description>lift due to alpha and flaps</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/flap-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d" % (0, 15, 30))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], base["CL"][i], flaps15["CL"][i], flaps30["CL"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')		

print('		<function name="aero/force/lift-due-to-the-left-aileron-deflection">')
print('			<description>lift due to the left aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/left-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			leftAileronMinus12["CL"][i] - base["CL"][i], 
			leftAileronMinus5["CL"][i] - base["CL"][i], 
			0,
			leftAileronPlus5["CL"][i] - base["CL"][i], 
			leftAileronPlus10["CL"][i] - base["CL"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/force/lift-due-to-the-right-aileron-deflection">')
print('			<description>lift due to the right aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/right-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			leftAileronMinus12["CL"][i] - base["CL"][i], 
			leftAileronMinus5["CL"][i] - base["CL"][i], 
			0,
			leftAileronPlus5["CL"][i] - base["CL"][i], 
			leftAileronPlus10["CL"][i] - base["CL"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/force/lift-due-to-the-elevator-deflection">')
print('			<description>lift due to the elevator deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/elevator-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d" % (-10, 0, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			elevatorMinus10["CL"][i] - base["CL"][i], 
			0,
			elevatorPlus10["CL"][i] - base["CL"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('	</axis>\n')

print('	<axis name="DRAG">\n')	# ------- DRAG ----------------------------

print('		<function name="aero/force/drag-due-to-alpha-and-flaps">')
print('			<description>drag due to alpha and flaps</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<sum>')
print('					<value>0.05</value> <!-- added manualy to take body and gear into account -->')
print('					<table>')
print('						<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('						<independentVar lookup="column">fcs/flap-pos-deg</independentVar>')
print('						<tableData>')

print("      %10d %10d %10d" % (0, 15, 30))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], base["CD"][i], flaps15["CD"][i], flaps30["CD"][i]))

print('						</tableData>')
print('					</table>')
print('				</sum>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/force/drag-due-to-the-left-aileron-deflection">')
print('			<description>drag due to the left aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/left-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			leftAileronMinus12["CD"][i] - base["CD"][i], 
			leftAileronMinus5["CD"][i] - base["CD"][i], 
			0,
			leftAileronPlus5["CD"][i] - base["CD"][i], 
			leftAileronPlus10["CD"][i] - base["CD"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/force/drag-due-to-the-right-aileron-deflection">')
print('			<description>drag due to the right aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/right-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			leftAileronMinus12["CD"][i] - base["CD"][i], 
			leftAileronMinus5["CD"][i] - base["CD"][i], 
			0,
			leftAileronPlus5["CD"][i] - base["CD"][i], 
			leftAileronPlus10["CD"][i] - base["CD"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/force/drag-due-to-the-elevator-deflection">')
print('			<description>drag due to the elevator deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/elevator-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d" % (-10, 0, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			elevatorMinus10["CD"][i] - base["CD"][i], 
			0,
			elevatorPlus10["CD"][i] - base["CD"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/force/drag-due-to-the-rudder-deflection">')
print('			<description>drag due to the rudder deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/rudder-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d" % (-10, 0, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			rudder10["CD"][i] - base["CD"][i], 
			0,
			rudder10["CD"][i] - base["CD"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('	</axis>\n')

print('	<axis name="SIDE">\n')	# ------- SIDE ----------------------------

print('		<function name="aero/force/side-force-due-to-beta">')
print('			<description>side force due to beta</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/beta-deg</independentVar>')
print('					<tableData>')

for i in range(len(baseBeta["Beta"])):
	print("%5.1f %10.6f" % 
		(baseBeta["Beta"][i], baseBeta["CY"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/force/side-force-due-to-the-rudder-deflection">')
print('			<description>side force due to the rudder deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/rudder-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d" % (-10, 0, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			rudder10["CY"][i], 
			0,
			-rudder10["CY"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/force/side-force-due-to-the-left-aileron-deflection">')
print('			<description>side force due to the left aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/left-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			leftAileronMinus12["CY"][i], 
			leftAileronMinus5["CY"][i], 
			0,
			leftAileronPlus5["CY"][i], 
			leftAileronPlus10["CY"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/force/side-force-due-to-the-right-aileron-deflection">')
print('			<description>side force due to the right aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/right-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			-leftAileronMinus12["CY"][i], 
			-leftAileronMinus5["CY"][i], 
			0,
			-leftAileronPlus5["CY"][i], 
			-leftAileronPlus10["CY"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('	</axis>\n')

print('	<axis name="PITCH">\n')	# ------- PITCH ----------------------------

print('		<function name="aero/moment/pitchdamp">')
print('			<description>pitch due to pitch rate</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<property>aero/bi2vel</property>')
print('				<property>velocities/p-aero-rad_sec</property>')
print('				<value>-0.1</value>')
print('			</product>')
print('		</function>')

print('		<function name="aero/moment/pitch-due-to-alpha-and-flaps">')
print('			<description>pitch due to alpha and flaps</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/flap-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d" % (0, 15, 30))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], base["Cm"][i], flaps15["Cm"][i], flaps30["Cm"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/moment/pitch-due-to-the-left-aileron-deflection">')
print('			<description>pitch due to the left aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/left-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			leftAileronMinus12["Cm"][i] - base["Cm"][i], 
			leftAileronMinus5["Cm"][i] - base["Cm"][i], 
			0,
			leftAileronPlus5["Cm"][i] - base["Cm"][i], 
			leftAileronPlus10["Cm"][i] - base["Cm"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/moment/pitch-due-to-the-right-aileron-deflection">')
print('			<description>pitch due to the right aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/right-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			leftAileronMinus12["Cm"][i] - base["Cm"][i], 
			leftAileronMinus5["Cm"][i] - base["Cm"][i], 
			0,
			leftAileronPlus5["Cm"][i] - base["Cm"][i], 
			leftAileronPlus10["Cm"][i] - base["Cm"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/moment/pitch-due-to-the-elevator-deflection">')
print('			<description>pitch due to the elevator deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/elevator-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d" % (-10, 0, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			elevatorMinus10["Cm"][i] - base["Cm"][i], 
			0,
			elevatorPlus10["Cm"][i] - base["Cm"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('	</axis>\n')

print('	<axis name="ROLL">\n')	# ------- ROLL ----------------------------

print('		<function name="aero/moment/rolldamp">')
print('			<description>roll due to roll rate</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<property>aero/bi2vel</property>')
print('				<property>velocities/p-aero-rad_sec</property>')
print('				<value>-0.1</value>')
print('			</product>')
print('		</function>')

print('		<function name="aero/moment/roll-due-to-beta">')
print('			<description>roll due to beta</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/beta-deg</independentVar>')
print('					<tableData>')

for i in range(len(baseBeta["Beta"])):
	print("%5.1f %10.6f" % 
		(baseBeta["Beta"][i], baseBeta["Cl"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/moment/roll-due-to-the-left-aileron-deflection">')
print('			<description>roll due to the left aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/left-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			leftAileronMinus12["Cl"][i], 
			leftAileronMinus5["Cl"][i], 
			0,
			leftAileronPlus5["Cl"][i], 
			leftAileronPlus10["Cl"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/moment/roll-due-to-the-right-aileron-deflection">')
print('			<description>roll due to the right aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/right-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			-leftAileronMinus12["Cl"][i], 
			-leftAileronMinus5["Cl"][i], 
			0,
			-leftAileronPlus5["Cl"][i], 
			-leftAileronPlus10["Cl"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/moment/roll-due-to-the-rudder-deflection">')
print('			<description>roll due to the rudder deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/rudder-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d" % (-10, 0, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			rudder10["Cl"][i], 
			0,
			-rudder10["Cl"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('	</axis>\n')

print('	<axis name="YAW">\n')	# ------- YAW ----------------------------

print('		<function name="aero/moment/yawdamp">')
print('			<description>yaw due to yaw rate</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<property>aero/bi2vel</property>')
print('				<property>velocities/r-aero-rad_sec</property>')
print('				<value>-0.01</value>')
print('			</product>')
print('		</function>')

print('		<function name="aero/moment/yaw-due-to-beta">')
print('			<description>yaw due to beta</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/beta-deg</independentVar>')
print('					<tableData>')

for i in range(len(baseBeta["Beta"])):
	print("%5.1f %10.6f" % 
		(baseBeta["Beta"][i], baseBeta["Cn"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/moment/yaw-due-to-the-rudder-deflection">')
print('			<description>yaw due to the rudder deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/rudder-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d" % (-10, 0, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			rudder10["Cn"][i], 
			0,
			-rudder10["Cn"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/moment/yaw-due-to-the-left-aileron-deflection">')
print('			<description>yaw due to the left aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/left-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			leftAileronMinus12["Cn"][i], 
			leftAileronMinus5["Cn"][i], 
			0,
			leftAileronPlus5["Cn"][i], 
			leftAileronPlus10["Cn"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('		<function name="aero/moment/yaw-due-to-the-right-aileron-deflection">')
print('			<description>right due to the left aileron deflection</description>')
print('			<product>')
print('				<property>aero/qbar-psf</property>')
print('				<property>metrics/Sw-sqft</property>')
print('				<property>metrics/bw-ft</property>')
print('				<table>')
print('					<independentVar lookup="row">aero/alpha-deg</independentVar>')
print('					<independentVar lookup="column">fcs/right-aileron-pos-deg</independentVar>')
print('					<tableData>')

print("      %10d %10d %10d %10d %10d" % (-12, -5, 0, 5, 10))
for i in range(len(base["alpha"])):
	print("%5.1f %10.6f %10.6f %10.6f %10.6f %10.6f" % 
		(base["alpha"][i], 
			-leftAileronMinus12["Cn"][i], 
			-leftAileronMinus5["Cn"][i], 
			0,
			-leftAileronPlus5["Cn"][i], 
			-leftAileronPlus10["Cn"][i]))

print('					</tableData>')
print('				</table>')
print('			</product>')
print('		</function>\n')

print('	</axis>\n')

print('</aerodynamics>')

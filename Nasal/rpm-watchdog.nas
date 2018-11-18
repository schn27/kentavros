var rpmwdg = func {
	if (getprop("/fdm/jsbsim/propulsion/engine/propeller-rpm") < 50) {
	   	setprop("/controls/engines/engine/throttle", 0.0001);
	}

	if (getprop("/fdm/jsbsim/propulsion/engine[1]/propeller-rpm") < 50) {
	   	setprop("/controls/engines/engine[1]/throttle", 0.0001);
	}

	if (getprop("/fdm/jsbsim/propulsion/engine[2]/propeller-rpm") < 50) {
	   	setprop("/controls/engines/engine[2]/throttle", 0.0001);
	}

	if (getprop("/fdm/jsbsim/propulsion/engine[3]/propeller-rpm") < 50) {
	   	setprop("/controls/engines/engine[3]/throttle", 0.0001);
	}

	settimer(rpmwdg, 1.0);
}

settimer(rpmwdg, 1.0);


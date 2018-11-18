# set the tower position by CTRL+LeftMouseButton

var KbdCtrl = props.globals.getNode("/devices/status/keyboard/ctrl");
var MtoFT  = 3.2808399;

setlistener("/sim/signals/click", func {         
    if (KbdCtrl.getBoolValue()) {
        var click_pos = geo.click_position();
        var tower = "/sim/tower";
        setprop(tower ~ "/latitude-deg", click_pos.lat());
        setprop(tower ~ "/longitude-deg", click_pos.lon());
        setprop(tower ~ "/altitude-ft", 4 + MtoFT * click_pos.alt());
    }
});

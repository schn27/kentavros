var inputPath = "/controls/nacelles/nacelle";
var outputPath = "/fdm/jsbsim/fcs/nacelle";

var getIndexedPath = func(path, index) {
	if (index == 0) {
		return path;
	}

	return path ~ "[" ~ index ~ "]";
}

setprop(getIndexedPath(inputPath, 0), 0);
setprop(getIndexedPath(outputPath, 0), 0);

setlistener(getIndexedPath(inputPath, 0), func(o) {
   	setprop(getIndexedPath(outputPath, 0), o.getValue());
});

setprop(getIndexedPath(inputPath, 1), 0);
setprop(getIndexedPath(outputPath, 1), 0);

setlistener(getIndexedPath(inputPath, 1), func(o) {
   	setprop(getIndexedPath(outputPath, 1), o.getValue());
});

setprop(getIndexedPath(inputPath, 2), 0);
setprop(getIndexedPath(outputPath, 2), 0);

setlistener(getIndexedPath(inputPath, 2), func(o) {
   	setprop(getIndexedPath(outputPath, 2), o.getValue());
});

setprop(getIndexedPath(inputPath, 3), 0);
setprop(getIndexedPath(outputPath, 3), 0);

setlistener(getIndexedPath(inputPath, 3), func(o) {
   	setprop(getIndexedPath(outputPath, 3), o.getValue());
});

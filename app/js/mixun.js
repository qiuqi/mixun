var mixun = {};
mixun.baseUrl = "https://www.han2011.com/"

mixun.register1 = function() {
	$.ajax({
		type: "GET",
		url: mixun.baseUrl + "register1/call.xml",
		dataType: "xml",
		success: mixun.register1.onSuccess,
		error: mixun.register1.onError
	});
};
mixun.register1.onSuccess = function(data, status) {
	alert($(data).text());
	alert($(data).find("b").text());
	alert($(data).find("b>skey").text());
};
mixun.register1.onError = function(data, status) {
	alert(data);
};

mixun.gettime = function() {
	$.ajax({
		type: "GET",
		url: mixun.baseUrl + "gettime/call.xml",
		dataType: "xml",
		success: mixun.gettime.onSuccess,
		error: mixun.gettime.onError
	});
};
mixun.gettime.onSuccess = function(data, status) {
	alert($(data).find("b>r").text());
	alert($(data).find("b>time").text());
};
mixun.gettime.onError = function(data, status) {
	alert(data);
};

mixun.test = function() {
	$.ajax({
		type: "GET",
		url: mixun.baseUrl + "test/1/2/0",
		dataType: "xml",
		success: mixun.test.onSuccess,
		error: mixun.test.onError
	});
};
mixun.test.onSuccess = function(data, status) {
	alert($(data).find("b>r").text());
};
mixun.test.onError = function(data, status) {
	alert(data);
};
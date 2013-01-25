$(document).ready(function() {
	$("#m_register1").on("click", function(event, ui) {
		mixun.register1();
	});
	$("#m_gettime").on("click", function(event, ui) {
		mixun.gettime();
	});
	$("#m_test").on("click", function(event, ui){
		mixun.test();
	});
	(function poll(){
		$.ajax({
			url:"https://www.han2011.com/test/1/2/1",
			success: function(data, status){
				console.log(data);
			},
			complete:poll,
			timeout:30000
		});
	})();
});
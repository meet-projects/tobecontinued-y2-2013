$(document).ready(function () {
    $('#username').hover(
	function() { 
		$(this).css('color', 'red'); 
	},
	function() {
		$(this).css('color', 'white');
	});
});

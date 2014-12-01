
function getLabel(s) {
	return s.split(/#/)[1];
}
$vg( document ).ready(function() {
var legends = $vg('.legends');
var children = legends.children('g');
var currSeries = getLabel($vg(children[0]).find('text').text());
var currColor = 0;
for (i = 1; i < children.length; i++) {
	var label = getLabel($vg(children[i]).find('text').text());
	if (label == currSeries) {
		$vg('.color-' + i).addClass('color-' + currColor).removeClass('color-' + i)
		$vg('.serie-' + i).removeClass('serie-' + i).addClass('serie-' + currColor);
		$vg('.activate-serie-' + i).removeClass('activate-serie-' + i).addClass('activate-serie-' + currColor);
		$vg('#activate-serie-' + i).attr('id', 'activate-serie-' + currColor);
	} else {
		currSeries = label;
		currColor = i;
	}
}
$vg(function () {
	$vg('.activate-serie').hover(function() {
		var match = this.id.match(/activate-serie-(\d+)/);
		if (match.length > 1) {
			var id = parseInt(match[1], 10);
			$vg('.plot .series').css('opacity', 0);
			$vg('.plot .serie-' + id).css('opacity', 1);
		}
	}, function() {
		$vg('.plot .series').css('opacity', 1);
		$vg('.text-overlay .series').css('opacity', 0);
	});

});

});

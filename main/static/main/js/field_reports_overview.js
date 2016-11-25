function getLatest(length){
	$('#days').html(length);
	$.ajax({url: "data/latest/"+length,
		dataType:'json',
		success: function(results){
			var html ='';
			countries = [];
			var frs;
        	results.forEach(function(fr,i){
        		if(i==0){
        			frs=fr
        		} else {
        			for(key in frs){
        				frs[key] +=parseInt(fr[key]);
        			}
        		}
        		html+=genFieldReportOverview(fr,true);
        		countries.push(fr.countryid);
        	});
        	console.log(frs);
        	if(frs){
        		$('#keyfiguresoverview').html(genFieldReportOverview(frs,false));
        	} else {
        		$('#keyfiguresoverview').html();
        	}
        	$('#latest').html(html);
        	updateMap(countries);
    	}
    });
}

function genFieldReportOverview(fr,all){
	var html = '';
	var cls="col-sm-2 col-xs-4 keyfiguretitle";
	if(all){
		html+='<div class="fieldreportoverview"></div><h4><a href="">'+fr.summary+'</a></h4>';
	    html+='<p><a href="">'+fr.countryname+'</a> - '+fr.disastertype+'</p></div>';
	}
    html+='<div class="row">';
    html+='<div class="'+cls+'"><p>Injured</p><p class="keyfigure">'+fr.injured+'</p></div><div class="'+cls+'"><p>Casualties</p><p class="keyfigure">'+fr.casualties+'</p></div><div class="'+cls+'"><p>Affected</p><p class="keyfigure">'+fr.affected+'</p></div><div class="'+cls+'"><p>Displaced</p><p class="keyfigure">'+fr.displaced+'</p></div><div class="'+cls+'"><p>Missing</p><p class="keyfigure">'+fr.missing+'</p></div>';
    html+='</div><div class="row"><div class="col-md-12"><p>Response</p></div></div><div class="row">';
    html+='<div class="'+cls+'"><p>Staff</p><p class="keyfigure">'+fr.staff+'</p></div><div class="'+cls+'"><p>Volunteers</p><p class="keyfigure">'+fr.volunteers+'</p></div><div class="'+cls+'"><p>Assisted</p><p class="keyfigure">'+fr.assisted+'</p></div><div class="'+cls+'"><p>Delegates</p><p class="keyfigure">'+fr.delegates+'</p></div>';
    html+='</div></div>';
    return html;
}
/*
function initMap(geom){
    var baselayer = L.tileLayer('https://data.hdx.rwlabs.org/mapbox-base-tiles/{z}/{x}/{y}.png', {});
    var baselayer2 = L.tileLayer('https://data.hdx.rwlabs.org/mapbox-layer-tiles/{z}/{x}/{y}.png', {minZoom:4});

	map = L.map('mapfroverview',{
				center: [0,0],
		        zoom: 2,
		        layers: [baselayer,baselayer2]
			});

	var style = function(feature) {
        return {
                'color': '#aaaaaa',
                'fillcolor': '#aaaaaa',
                'weight': 1,
                'opacity': 0.7,
                'fillOpacity':0,
                'className':'country'
            };
        }

	map.overlay = L.geoJson(geom,{
		style: style,
		onEachFeature: function (feature, layer) {
                feature.properties.bounds_calculated=layer.getBounds();
            }
    }).addTo(map);

	return map;
}
*/

function initMap(geom){
	console.log(geom);
	var width = $('#mapfroverview').width(),
    height =  $('#mapfroverview').height();

	var svg = d3.select("#mapfroverview").append("svg")
	    .attr("width", width)
	    .attr("height", height);

	var projection = d3.geo.mercator()
	    .center([0, 0])
	    .scale(width/6.2)
	    .translate([width / 2, height / 2]);    

	svg.selectAll("path")
      .data(geom.features)
      .enter().append("path")
      .attr("d", d3.geo.path().projection(projection))
      .attr('class','country')
      .attr('id',function(d){
      	return 'country'+d.properties.ISO_A3;
      });
}
function updateMap(countries){
	$('.country').removeClass('selected');

	countries.forEach(function(d){
		console.log('#country'+d);
		$('#country'+d).addClass('selected');
	});
}


$('#last7').on('click',function(){
	getLatest(7);
});

$('#last30').on('click',function(){
	getLatest(30);
});

var map;

$.ajax({url: geomurl,
		dataType:'json',
		success: function(result){
			var geom = topojson.feature(result,result.objects.geom);
			map = initMap(geom);
			getLatest(7);
    	}
    });

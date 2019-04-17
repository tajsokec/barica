window.onload=function(){
	
	$('body').append( '<div class="barica" id="div_barica"><video 200="width" height="375" id="barica"><source src="video_barica.mp4" type="video/mp4"></video></div>' );
	$( '.step' ).css( right );
	$( '.header' ).css( right );
	$( '.footer' ).css( right );
	$( '.footer' ).css({
		'position': 'absolute',
		'bottom': '0'
	})
	
	var promise = document.querySelector('video').play();

	if (promise !== undefined) {
		promise.then(_ => {
			promise[0].play();
		}).catch(error => {
			$('body').append('<div id="btn_play" onclick="clickPlayVideo()"></div>')
			$("#btn_play").css("background-image","url(http://image.flaticon.com/icons/svg/10/10430.svg)");
		});
	}
	
	$( '#barica' )[0].ontimeupdate = function(){
		var barica = $( '#barica' )[0];
		var the_time = barica.currentTime;
		console.log( the_time );
		if( the_time >= END )
		{
			barica.pause();
			play_part( 'TISINA' );
		}
	}
	$( '#barica' )[0].loadedmetadata = function(){
		play_part( 'TISINA' );
	}

}

function clickPlayVideo(){
		
	if( $("video").prop('muted') ) {
          $("video").prop('muted', false);
    }
		
	//var barica = $( '#barica' )[0];
	//barica.play();
	play_part( 'TISINA' );
	
	$('#btn_play').hide();
	
}

function connect() {
	var ws = new WebSocket('ws://localhost:8009');
	ws.onopen = function() {
		// subscribe to some channels
		ws.send( 'connect' );
		toggleMute();
 	};

	ws.onmessage = function( msg ) {
		console.log( msg.data );
		var message_split = msg.data.toString().split(" ");
		if( msg.data.toString() == 'IZVOLI' )
		{
			play_part( 'IZVOLI' );
		}
		else if( msg.data.toString() == 'FOI' )
		{
			play_part( 'FOI' );
		}
		else if( msg.data.toString() == 'KOJA_DVORANA' )
		{
			play_part( 'KOJA_DVORANA' );
		}
		else if( msg.data.toString() == 'KOJI_PROFESOR' )
		{
			play_part( 'KOJI_PROFESOR' );
		}
		else if( msg.data.toString() == 'KOJA_VRSTA_STUDIJA' )
		{
			play_part( 'KOJA_VRSTA_STUDIJA' );
		}
		else if( msg.data.toString() == 'KOJA_GODINA' )
		{
			play_part( 'KOJA_GODINA' );
		}
		else if( msg.data.toString() == 'RASPORED_NE_POSTOJI' )
		{
			play_part( 'RASPORED_NE_POSTOJI' );
		}
		else if( message_split[0] == 'PROFESOR' )
		{
			if($('#podatci-o-profesoru').next().is('#theImg')){
				$( '#theImg' ).replaceWith('<img id="theImg" style="width: 130%; height: 130%" src="images\\professors\\' 
			+ message_split[1] + '.png" />');
			}else{
				$('#podatci-o-profesoru').after('<img id="theImg" style="width: 130%; height: 130%" src="images\\professors\\' 
			+ message_split[1] + '.png" />');
			}
			play_part( 'PROFESOR' );
		}
		else if(message_split[0] == 'GROUPS')
		{
			if($('#grupa').next().is('blockquote')){
				$('blockquote').replaceWith(message_split[1]);
			}else{
				$('#grupa').after(message_split[1]);
			}
			play_part( 'KOJA_GRUPA' );
		}
		else if( message_split[0] == 'DVORANA' )
		{
			play_part( message_split[1] );
		}
		else if( msg.data.toString() == 'RASPORED' )
		{
			play_part( 'RASPORED' );
		}
		else if( msg.data.toString() == 'PONOVI' )
		{
			play_part( 'PONOVI' );
		}
	};

	ws.onclose = function(e) {
		console.log( 'Socket is closed. Reconnect will be attempted in 1 second.', e.reason );
		setTimeout(function() {
			connect();
		}, 1000);
	};

	ws.onerror = function(err) {
		console.error( 'Socket encountered error: ', err.message, 'Closing socket' );
		ws.close();
	};
}

connect();

right = { 
	'text-align': 'right',
	'width': '1000px',
	'margin-right': '-400px auto'
};

CUR_PART = 'TISINA';
END = 71;

function play_part( part )
{
	CUR_PART = part;
	var barica = $( '#barica' )[ 0 ];
	var end = 0;
	barica.play()
	switch( part )
	{
		case 'IZVOLI':
			barica.currentTime = 7;
			end = 7.8;
			break;
		case 'FOI':
			barica.currentTime = 8;
			end = 31.8;
			break;
		case 'KOJA_DVORANA':
			barica.currentTime = 32.3;
			end = 33.3;
			break;
		case 'KOJI_PROFESOR':
			barica.currentTime = 33.5;
			end = 34.7;
			break;
		case 'KOJA_VRSTA_STUDIJA':
			barica.currentTime = 35;
			end = 37.8;
			break;
		case 'KOJA_GODINA':
			barica.currentTime = 159.5;
			end = 162.5;
			break;
		case 'KOJA_GRUPA':
			barica.currentTime = 162.7;
			end = 165;
			break;
		case 'RASPORED_NE_POSTOJI':
			barica.currentTime = 165.2;
			end = 169;
			break;
		case 'RASPORED_NEDOSTUPAN':
			barica.currentTime = 169;
			end = 171.5;
			break;
		case 'PROFESOR':
			barica.currentTime = 171.5;
			end = 173.7;
			break;
		case 'RASPORED':
			barica.currentTime = 173.9;
			end = 175.5;
			break;
		case 'PONOVI':
			barica.currentTime = 175.5;
			end = 177;
			break;
		case 'TISINA':
			barica.currentTime = 0;
			end = 5;
			break;
		case 'd9':
			barica.currentTime = 38;
			end = 42.3;
			break;
		case 'info':
			barica.currentTime = 42.5;
			end = 47.3;
			break;
		case 'knjiznica':
			barica.currentTime = 47.6;
			end = 51.7;
			break;
		case 'd10':
			barica.currentTime = 51.7;
			end = 56.3;
			break;
		case 'referada':
			barica.currentTime = 56.5;
			end = 60.9;
			break;
		case 'lab5':
			barica.currentTime = 60.9;
			end = 65.8;
			break;
		case 'skriptarnica':
			barica.currentTime = 65.8;
			end = 70.4;
			break;
		case 'foto':
			barica.currentTime = 70.6;
			end = 75.5;
			break;
		case 'd6':
			barica.currentTime = 75.5;
			end = 79.8;
			break;
		case 'd7':
			barica.currentTime = 84.5;
			end = 89;
			break;
		case 'lab12':
			barica.currentTime = 89.2;
			end = 94.1;
			break;
		case 'lab13':
			barica.currentTime = 94.1;
			end = 99;
			break;
		case 'lab14':
			barica.currentTime = 99;
			end = 104.1;
			break;
		case 'lab15':
			barica.currentTime = 104.3;
			end = 109.1;
			break;
		case 'dekanat':
			barica.currentTime = 109.3;
			end = 114.5;
			break;
		case 'CPSRK':
			barica.currentTime = 114.5;
			end = 122;
			break;
		case 'racunovodstvo':
			barica.currentTime = 122;
			end = 126.5;
			break;
		case 'd4':
			barica.currentTime = 127.2;
			end = 133;
			break;
		case 'd11':
			barica.currentTime = 133.4;
			end = 138.1;
			break;
		case 'd1':
			barica.currentTime = 138.4;
			end = 143.7;
			break;
		case 'd2':
			barica.currentTime = 143.7;
			end = 148.5;
			break;
		case 'd8':
			barica.currentTime = 148.7;
			end = 154.7;
			break;
		case 'd3':
			barica.currentTime = 155;
			end = 159.4;
			break;
		
	}
	END = end;
}

function toggleMute() {

  var video=document.getElementById("barica");

  if(video.muted){
    video.muted = false;
  } else {
    video.muted = true;
  }

}









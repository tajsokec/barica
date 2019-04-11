
function connect() {
	var ws = new WebSocket('ws://localhost:8009');
	ws.onopen = function() {
		// subscribe to some channels
		ws.send( 'connect' );
 	};

	ws.onmessage = function( msg ) {
		console.log( msg.data );
		var message_split = msg.data.toString().split(" ");
		if( message_split[0] == 'PROFESOR' )
		{
			console.log( 'message: PROFESOR' );
			if($('#podatci-o-profesoru').next().is('#theImg')){
				$( '#theImg' ).replaceWith('<img id="theImg" style="width: 130%; height: 130%" src="images\\professors\\' 
			+ message_split[1] + '.png" />');
			}else{
				$('#podatci-o-profesoru').after('<img id="theImg" style="width: 130%; height: 130%" src="images\\professors\\' 
			+ message_split[1] + '.png" />');
			}
		}
		if(message_split[0] == 'GROUPS')
		{
			console.log('message: GROUPS');
			if($('#grupa').next().is('blockquote')){
				$('blockquote').replaceWith(message_split[1]);
			}else{
				$('#grupa').after(message_split[1]);
			}
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







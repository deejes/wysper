$(document).ready(function(){
  // gets list of previous messages and displays them
  $.ajax({
    type: 'GET',
    url: '/messages/'+receiver_id,
    success: function(messages){
      $.each(messages, function(i,message){
	if (message.sender == receiver_id){
	  $('#msg-list').append('<li class="text-left list-group-item">' + message.body  + '</li>');}
	else {	  $('#msg-list').append('<li class="text-right list-group-item">' + message.body  + '</li>');};
      });
    }
    });

  // intercepts the send button,adds message to model, and then sends across the websocket.
  $( "#send" ).click(function(e) {
  e.preventDefault();
    $.when(create_post()).then(send_message());
  });

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function pairing(a,b){
	var a = parseInt(a);
	var b = parseInt(b);
  return ((a**b)+(b**a))
  //return ((1/2)*(a+b)*(a+b+1)+b);
};

  //creates new websocket
  socket = new WebSocket("ws://" + window.location.host + "/chat/" + pairing(user_id,receiver_id));

  // sets behaviour when a message comes across the socket
  socket.onmessage= function(e){
    if (JSON.parse(e.data).sender != user_id){
      $('#msg-list').append('<li class="text-left list-group-item">' + (JSON.parse(e.data)).msg  + '</li>')};
  };

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        }
    }
  });
});



  //creates a record in the message model
function create_post() {

  $.ajax({
        url : "/messages/"+receiver_id, // the endpoint
        type : "POST", // http method
        data : { msgbox : $('#chat-msg').val() },

        success : function(json) {
   	  $('#msg-list').append('<li class="text-right list-group-item">' +  $('#chat-msg').val()  + '</li>');
	  $('#chat-msg').val('');
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
  });

};

// sends a Json message across the socket
function send_message(){
  socket.send(JSON.stringify({"msg": $('#chat-msg').val(),"sender":user_id}));
}

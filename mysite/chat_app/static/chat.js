$(document).ready(function(){
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
  return ((1/2)*(a+b)*(a+b+1)+b);
};

  socket = new WebSocket("ws://" + window.location.host + "/chat/123");
  socket.onmessage= function(e){
    if ((JSON.parse(JSON.parse(e.data))).sender != user_id){
      $('#msg-list').append('<li class="text-left list-group-item">' + JSON.parse(JSON.parse(e.data)).msg  + '</li>')};
  };

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        }
    }



});




//   $("body").bind("ajaxSend", function(elm, xhr, s){
//    if (s.type == "POST") {
//       xhr.setRequestHeader('X-CSRF-Token', getCSRFTokenValue());
//    }
// });

});




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


function send_message(){

  socket.send(JSON.stringify(JSON.stringify({"msg": $('#chat-msg').val(),"sender":user_id})));
}

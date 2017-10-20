$(document).ready(function(){

  $.ajax({
    type: 'GET',
    url: '/messages/'+receiver_id,
    success: function(messages){
      $.each(messages, function(i,message){
	if (message.sender == receiver_id){
	  $('#msg-list').append('<li class="text-left list-group-item">' + message.body + '</li>');}
	else {
	  $('#msg-list').append('<li class="text-right list-group-item">' + message.body + '</li>');
	}
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

  socket = new WebSocket("ws://" + window.location.host + "/chat/"+ user_id*receiver_id);

  socket.onmessage= function(e){
    var message = JSON.parse(e.data);
    if (message.sender != user_id) {
      $('#msg-list').append('<li class="text-left list-group-item">' + message +'</li>');
    }
  };
  
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        }
    }
 
});
  
function create_post() {
  $.ajax({
        url : "/messages/"+receiver_id, // the endpoint
        type : "POST", // http method
        data : { msgbox : $('#chat-msg').val() },
        success : function(json) {
   	  $('#msg-list').append('<li class="text-right list-group-item">' + $('#chat-msg').val() + '</li>');
	  $('#chat-msg').val('');
        },
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // more details about error
        }
  });

};

function send_message(){
  socket.send(JSON.stringify({"msg": $('#chat-msg').val(),"sender":user_id}));
}
  
// $('#chat').on('submit', function(event){
//     event.preventDefault();
// }
	      
//     $.ajax({
//         url : '/post/',
//         type : 'POST',
//         data : { msgbox : $('#chat-msg').val() },

//         success : function(json){
//             $('#chat-msg').val('');
//             $('#msg-list').append('<li ass="text-right list-group-item">' + json.msg + '</li>');
//             var chatlist = document.getElementById('msg-list-div');
//             chatlist.scrollTop = chatlist.scrollHeight;
//         }
//     });
// });

// function getMessages(){
//     if (!scrolling) {
//         $.get('/messages/', function(messages){
//             $('#msg-list').html(messages);
//             var chatlist = document.getElementById('msg-list-div');
//             chatlist.scrollTop = chatlist.scrollHeight;
//         });
//     }
//     scrolling = false;
// }

// var scrolling = false;
// $(function(){
//     $('#msg-list-div').on('scroll', function(){
//         scrolling = true;
//     });
//     refreshTimer = setInterval(getMessages, 500);
// });

// $(document).ready(function() {
//      $('#send').attr('disabled','disabled');
//      $('#chat-msg').keyup(function() {
//         if($(this).val() != '') {
//            $('#send').removeAttr('disabled');
//         }
//         else {
//         $('#send').attr('disabled','disabled');
//         }
//      });
//  });

// // using jQuery
// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie != '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// var csrftoken = getCookie('csrftoken');

// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }
// $.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });

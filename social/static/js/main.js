var modalConfirm = function(callback, action, param){
  var action = null
  $(".action").on("click", function(){
      action = $(this)
      $("#msg-confirm").text(action.attr('data-msg'))
    $("#mi-modal").modal('show');
  });

  $("#modal-btn-sim").on("click", function(){
    callback(action.attr('positive'), action.attr('param'));
    $("#mi-modal").modal('hide');
  });

  $("#modal-btn-nao").on("click", function(){
    callback(action.attr('negative'), action.attr('param'));
    $("#mi-modal").modal('hide');
  });
};

modalConfirm(function(action, param){
   window[action](param);
});
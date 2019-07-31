//
// $(document).ready(function(){
//
//  $('.preview-article').click(function(){
//
//    // AJAX request
//    $.ajax({
//     url: $(this).attr("data-url"),
//     type: 'post',
//     success: function(response){
//       // Add response in Modal body
//       $('.modal-body').html(response);
//
//       // Display Modal
//       $('formModalCenter').modal('show');
//     }
//   });
//  });
// });

$(document).ready(function(){

 $('.preview-article').click(function(e){

  e.preventDefault();

  var form_data = $('#articleForm').serialize();
  console.log(form_data)

  $('#dynamic-content').hide(); // hide dive for loader
  $('#modal-loader').show();  // load ajax loader

  $.ajax({
      headers: { "X-CSRFToken": $.cookie("csrftoken") },
      url: $(this).attr("data-url"),
      type: 'POST',
  })
  .done(function(data){
      console.log(data);
      $('#dynamic-content').hide(); // hide dynamic div
      $('#dynamic-content').show(); // show dynamic div
      $('#txt_fname').html(data.first_name);
      $('#modal-loader').hide();    // hide ajax loader
  })
  .fail(function(){
      $('.modal-body').html('<i class="fas fa-info-circle"></i> Something went wrong, Please try again...');
  });

 });

});
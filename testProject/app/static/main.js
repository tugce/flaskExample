$(document).ready(function() {
  console.log("ready!");

  // on form submission ...
  $('form').on('submit', function() {

    console.log("the form has beeen submitted");

    // grab values
    valueOne = $('input[name="url"]').val();
    valueTwo = $('input[name="email"]').val();
    console.log(valueOne, valueTwo)

    $.ajax({
      type: "POST",
      url: "/",
      data : { 'first': valueOne, 'second': valueTwo },
      success: function(results) {
        if (results.items.length > 0) {
          $('input').hide();
        } else {
          $('#results').html('Something went terribly wrong! Please try again.')
        }
      },
      error: function(error) {
        console.log(error)
      }
    });

  });

  });

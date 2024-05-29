$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
        // Add optional callback code here if needed
      });
    }
  });

  // Clear message input field and paragraph text on window load
  window.onload = function () {
    document.getElementById('msg').value = '';
    var response = "{{ response }}" === "True";  // Convert response to boolean
  // Convert response to boolean
    if (response) {
      document.querySelector('h4').textContent = '';
    }
  };
});

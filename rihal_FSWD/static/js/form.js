// static/js/form.js

// Add event listener to submit button to show loading spinner
document.querySelector('form button[type="submit"]').addEventListener('click', function() {
    this.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';
  });
  
// Get the toggle button and body element from the HTML
const toggle = document.getElementById('toggleDark');
const body = document.querySelector('body');

// Add a click event listener to the toggle button
toggle.addEventListener('click', function(){

   // Toggle the moon icon on and off
  this.classList.toggle('bi-moon');
  // Toggle the brightness icon on and off and check if it's toggled on
  if(this.classList.toggle('bi-brightness-high-fill')){
     // Set the background color to white, text color to black, and transition time to 2 seconds
      body.style.background = 'white';
      body.style.color = 'black';
      body.style.transition = '2s';

  }else{
    // Set the background color to black, text color to white, and transition time to 2 seconds
      body.style.background = 'black';
      body.style.color = 'white';
      body.style.transition = '2s';


  }
});

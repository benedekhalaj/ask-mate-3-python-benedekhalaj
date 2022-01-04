document.getElementById('submit').hidden = true;
let check = function() {
  if (document.getElementById('password').value ==
    document.getElementById('password_confirmation').value &&
      document.getElementById('password').value !== '')  {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'matching';
    document.getElementById('submit').hidden = false;
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'not matching';
    document.getElementById('submit').hidden = true;
  }
}
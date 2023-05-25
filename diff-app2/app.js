document.getElementById('numberForm').addEventListener('submit', function(e) {
  e.preventDefault(); // Prevent form submission

  // Get input values
  var e = parseFloat(document.getElementById('e').value);
  var v = parseFloat(document.getElementById('v').value);
  var p = parseFloat(document.getElementById('p').value);

  // Perform computation
  var r = 1-(p/100);
  var result = Math.round((e*v-v*r*e)/(v*r));
  var preis = (result + e)/100 

  // Display result
  document.getElementById('result').innerHTML = '<p style="font-weight: bold">Wenn Super&nbsp;E5 nicht mehr als <span style="color: red;">' + preis + '&nbsp;&#8364;</span> kostet, dann lohnt es sich eventuell, Super&nbsp;E5 zu tanken.</span></p>';
});

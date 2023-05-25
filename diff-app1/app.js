document.getElementById('numberForm').addEventListener('submit', function(e) {
  e.preventDefault(); // Prevent form submission

  // Get input values
  var e = parseFloat(document.getElementById('e').value);
  var v = parseFloat(document.getElementById('v').value);

  // Perform computation
  var result1 = Math.round((e*v-v*0.98*e)/(v*0.98));
  var result2 = Math.round((e*v-v*0.95*e)/(v*0.95));

  // Display result
  document.getElementById('result').innerHTML = '<p style="font-weight: bold">Wenn Super&nbsp;E5 nicht mehr als <span style="color: red;">' + result1 + '&nbsp;bis&nbsp;' + result2 + '&nbsp;Cent</span> teurer ist als Super&nbsp;E10, dann lohnt es sich eventuell, Super&nbsp;E5 zu tanken.</span></p>';
});

var d  = new Date();
var tt = d.getDate();
var m = ("0" + (d.getMonth() + 1)).slice(-2)
var yy = d.getFullYear();
var h = String(yy) + String(m) + String(tt)


document.writeln("<a href='#" + h + "' class='jumplink pic'>")

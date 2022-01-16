var d  = new Date();
var tt = d.getDate();
var m = ("0" + (d.getMonth() + 1)).slice(-2)
var yy = d.getFullYear();
var h = String(yy) + String(m) + String(tt)

var g = new Date();
var gg = g.setDate(g.getDate() - 1);
var tt_g = g.getDate();
var m_g = ("0" + (g.getMonth() + 1)).slice(-2)
var yy_g = g.getFullYear();
var h_g = String(yy_g) + String(m_g) + String(tt_g)

var mg = new Date();
var gg = mg.setDate(mg.getDate() + 1);
var tt_m = mg.getDate();
var m_m = ("0" + (mg.getMonth() + 1)).slice(-2)
var yy_m = mg.getFullYear();
var h_m = String(yy_m) + String(m_m) + String(tt_m)



//-------------------------------------------

document.writeln("<a href='#" + h_g + "'class='icon solid fa-arrow-circle-left'><span>Gestern</span></a>")
document.writeln("<a href='#" + h   + "'class='icon solid fa-calendar-day'><span>Heute</span></a>")
document.writeln("<a href='#" + h_m + "'class='icon solid fa-arrow-circle-right'><span>Morgen</span></a>")
document.writeln("<a href='#" + h_m + "_w'class='icon solid fa-calendar-week'><span>Woche</span></a>")

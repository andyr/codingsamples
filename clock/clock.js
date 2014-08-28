
// Compute initial state from current time
var now = new Date();

var now_s = now.getSeconds();
var now_m = now.getMinutes();
var now_h = now.getHours() % 12;

var sa = now_s * 6;
var ma = (now_s * 6/60) + now_m * 6;
var ha = (now_s * 30/3600) + (now_m * 30/60) + (now.getHours() % 12)*30;

var s_el = $('.second-hand'),
    m_el = $('.minute-hand'),
    h_el = $('.hour-hand');
var interval = 25;

function rotate(el, angle) {
  el.css({ transform: 'rotate('+angle+'deg)' });
};
  
setInterval(function () { 
  sa += 6/(1000/interval) % 360; // 6deg/s
  ma += 6/(60 * 1000/interval) % 360; // 6deg/min
  ha += 30/(3600 * 1000/interval) % 360; // 30deg/1hr
  
  rotate(s_el, sa);
  rotate(m_el, ma);
  rotate(h_el, ha);

}, interval);




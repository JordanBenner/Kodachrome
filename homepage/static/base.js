function show_p(a, id) {
  var p = document.getElementById(id);
  if (p.style.height == 'auto') {
    p.style.height = '0';
    a.innerHTML = 'Read More';
  } else {
    p.style.height = 'auto';
    a.innerHTML = 'Hide';
  }

  p.scrollIntoView(true);
}

<!-- Quantcast Tag -->
<script type="text/javascript">
var _qevents = _qevents || [];

(function() {
var elem = document.createElement('script');
elem.src = (document.location.protocol == "https:" ? "https://secure" : "http://edge") + ".quantserve.com/quant.js";
elem.async = true;
elem.type = "text/javascript";
var scpt = document.getElementsByTagName('script')[0];
scpt.parentNode.insertBefore(elem, scpt);
})();

_qevents.push({
qacct:"p-tAMkw8d3tEH3z"
});
</script>

<noscript>
<div style="display:none;">
<img src="//pixel.quantserve.com/pixel/p-tAMkw8d3tEH3z.gif" border="0" height="1" width="1" alt="Quantcast"/>
</div>
</noscript>
<!-- End Quantcast tag -->

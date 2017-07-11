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

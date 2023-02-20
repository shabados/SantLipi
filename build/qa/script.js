var slide = document.getElementById('fw')
var slideValue = document.getElementById('fw-value')
var sle = document.getElementsByClassName('large')

function isLocalStorageAvailable() {
  try {
    localStorage.setItem('test', 'test')
    localStorage.removeItem('test')
    return true
  } catch (e) {
    return false
  }
}

function changeFontWeight(weight) {
  if (isLocalStorageAvailable()) {
    localStorage.setItem('fontWeight', weight)
  }
  for (var i = 0; i < sle.length; i++) {
    sle[i].style['font-variation-settings'] = "'wght' " + weight
  }
  slideValue.innerHTML = weight
}

if (isLocalStorageAvailable()) {
  var fontWeight = localStorage.getItem('fontWeight')
  changeFontWeight(fontWeight)
  slide.value = fontWeight
} else {
  changeFontWeight(400)
}

slide.addEventListener('input', function () {
  changeFontWeight(this.value)
})

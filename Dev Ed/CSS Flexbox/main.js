function flexStart() {
  document.getElementById('parent-container').classList.remove('justify-end');
  document.getElementById('parent-container').classList.remove('justify-center');
  document.getElementById('parent-container').classList.add('justify-start');
}

function center() {
  document.getElementById('parent-container').classList.remove('justify-end');
  document.getElementById('parent-container').classList.remove('justify-start');
  document.getElementById('parent-container').classList.add('justify-center');
}

function flexEnd() {
  document.getElementById('parent-container').classList.remove('justify-start');
  document.getElementById('parent-container').classList.remove('justify-center');
  document.getElementById('parent-container').classList.add('justify-end');
}

function spaceBetween() {
  document.getElementById('parent-container').classList.remove('space-evenly');
  document.getElementById('parent-container').classList.add('space-between');
}

function spaceEvenly() {
  document.getElementById('parent-container').classList.remove('space-between');
  document.getElementById('parent-container').classList.add('space-evenly');
}

function alignStart() {
  document.getElementById('parent-container').classList.remove('align-end');
  document.getElementById('parent-container').classList.remove('align-center');
  document.getElementById('parent-container').classList.add('align-start');
}

function alignCenter() {
  document.getElementById('parent-container').classList.remove('align-start');
  document.getElementById('parent-container').classList.remove('align-end');
  document.getElementById('parent-container').classList.add('align-center');
}

function alignEnd() {
  document.getElementById('parent-container').classList.remove('align-start');
  document.getElementById('parent-container').classList.remove('align-center');
  document.getElementById('parent-container').classList.add('align-end');
}

function flexRow() {
  document.getElementById('parent-container').classList.remove('flex-column');
  document.getElementById('parent-container').classList.add('flex-row');
}

function flexColumn() {
  document.getElementById('parent-container').classList.remove('flex-row');
  document.getElementById('parent-container').classList.add('flex-column');
}

document.getElementById('child1').addEventListener('click', () => {
  document.getElementById('child1').classList.toggle('flex-grow');
})

document.getElementById('child2').addEventListener('click', () => {
  document.getElementById('child2').classList.toggle('flex-grow');
})

document.getElementById('child3').addEventListener('click', () => {
  document.getElementById('child3').classList.toggle('flex-grow');
})

document.getElementById('child4').addEventListener('click', () => {
  document.getElementById('child4').classList.toggle('flex-grow');
})
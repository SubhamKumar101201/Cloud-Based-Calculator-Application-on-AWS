// ---------------- calculate & send ----------------
function calculate(op) {
  const a = parseFloat(document.getElementById('input1').value);
  const b = parseFloat(document.getElementById('input2').value);
  const resultBox = document.getElementById('result');

  // basic validation
  if (Number.isNaN(a) || Number.isNaN(b)) {
    resultBox.value = 'Invalid input';
    return;
  }

  let result;
  switch (op) {
    case 'add':       result = a + b; break;
    case 'subtract':  result = a - b; break;
    case 'multiply':  result = a * b; break;
    case 'divide':
      if (b === 0)    { resultBox.value = 'Divide‑by‑zero!'; return; }
      result = a / b;
      break;
    default:
      resultBox.value = 'Unknown op';
      return;
  }

  // show result instantly
  resultBox.value = result;

  // send to backend with fetch (GET for simplicity)
  fetch(`http://127.0.0.1:8000/api/v1/store-result/?sum=${result}`)
    .then(r => r.json())
    .then(data => {
      if (data.status !== 'saved') {
        alert(data.message || 'Server did not confirm save.');
      }
    })
    .catch(err => {
      console.error('Save error:', err);
      alert('Failed to save result.');
    });
}

// ---------------- load history on page load ----------------
function loadResults() {
  fetch('http://127.0.0.1:8000/api/v1/get-results/')
    .then(r => r.json())
    .then(data => {
      const list = document.getElementById('resultList');
      list.innerHTML = '';
      (data.results || []).forEach((val, i) => {
        const li = document.createElement('li');
        li.textContent = `Result ${i + 1}: ${val}`;
        list.appendChild(li);
      });
    })
    .catch(err => console.error('History load error:', err));
}

// fire once per full page load / refresh
document.addEventListener('DOMContentLoaded', loadResults);

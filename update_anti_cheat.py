import sys

# 1. Update class-prep-workplace.html (Anti-cheat)
with open("class-prep-workplace.html", "r", encoding="utf-8") as f:
    html = f.read()

old_start = """  const name = document.getElementById('studentName').value.trim();
  if (!name) {
    alert("Please enter your name in the Warm-Up section before submitting!");
    goTo(0);
    return;
  }"""

anti_cheat_logic = """  const name = document.getElementById('studentName').value.trim();
  if (!name) {
    alert("Please enter your name in the Warm-Up section before submitting!");
    goTo(0);
    return;
  }
  
  // ANTI-TRAMPAS: Verificar que hayan llenado todo y no sea basura
  const w1 = document.getElementById('w1') ? document.getElementById('w1').value.trim() : '';
  const w2 = document.getElementById('w2') ? document.getElementById('w2').value.trim() : '';
  const w3 = document.getElementById('w3') ? document.getElementById('w3').value.trim() : '';
  const w4 = document.getElementById('w4') ? document.getElementById('w4').value.trim() : '';
  const dialogue = document.getElementById('myDialogue') ? document.getElementById('myDialogue').value.trim() : '';
  
  if (!w1 || !w2 || !w3 || !w4 || !dialogue) {
    alert("Hold on! You must complete ALL the Writing Scenarios and the Challenge Dialogue before submitting.");
    return;
  }
  
  if (w1.length < 5 || dialogue.length < 15) {
    alert("Your answers are too short. Please write complete sentences and try again!");
    return;
  }"""

html = html.replace(old_start, anti_cheat_logic)

with open("class-prep-workplace.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. Update admin.html (Add student counter)
with open("admin.html", "r", encoding="utf-8") as f:
    admin = f.read()

admin = admin.replace('<h1>👩‍🏫 Panel de Resultados</h1>', '<h1 id="panelTitle">👩‍🏫 Panel de Resultados</h1>')

old_fetch_logic = """    if (data.length === 0) {
      container.innerHTML = '<p>Aún no hay respuestas de ningún estudiante.</p>';
      return;
    }"""

new_fetch_logic = """    document.getElementById('panelTitle').innerHTML = `👩‍🏫 Panel de Resultados <span style="font-size:18px;color:var(--teal)">(${data.length} entregas)</span>`;
    
    if (data.length === 0) {
      container.innerHTML = '<p>Aún no hay respuestas de ningún estudiante.</p>';
      return;
    }"""

admin = admin.replace(old_fetch_logic, new_fetch_logic)

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(admin)

print("Anti-cheat and admin counter updated.")

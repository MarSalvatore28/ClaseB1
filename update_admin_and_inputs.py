import re

# 1. Update class-prep-workplace.html
with open("class-prep-workplace.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add IDs to Warm-Up inputs
html = html.replace('<input class="task-input" placeholder="I would say: ..." />', '<input class="task-input" id="wu1" placeholder="I would say: ..." />', 1)
html = html.replace('<input class="task-input" placeholder="I would say: ..." />', '<input class="task-input" id="wu2" placeholder="I would say: ..." />', 1)
html = html.replace('<textarea class="task-input" rows="2" style="resize:vertical" placeholder="Because..."></textarea>', '<textarea class="task-input" id="wu3" rows="2" style="resize:vertical" placeholder="Because..."></textarea>', 1)

# Add IDs to Listening inputs
html = html.replace('<input class="task-input" placeholder="She says: ..." />', '<input class="task-input" id="l1" placeholder="She says: ..." />')
html = html.replace('<input class="task-input" placeholder="She rejects the offer of... She says: ... പക" />', '<input class="task-input" id="l2" placeholder="She rejects the offer of... She says: ..." />')
# Fix the above replace if the placeholder text differs slightly
html = re.sub(r'<input class="task-input" placeholder="She rejects the offer of[^>]+>', '<input class="task-input" id="l2" placeholder="She rejects the offer of... She says: ..." />', html)
html = re.sub(r'<textarea class="task-input" rows="2" style="resize:vertical" placeholder="Because..."></textarea>', '<textarea class="task-input" id="l3" rows="2" style="resize:vertical" placeholder="Because..."></textarea>', html)
html = re.sub(r'<input class="task-input" placeholder="The expression is... I think it sounds..." />', '<input class="task-input" id="l4" placeholder="The expression is... I think it sounds..." />', html)

# Update submit logic
old_data_obj = """  const data = {
    name: name,
    quizScore: document.getElementById('scoreNum') ? document.getElementById('scoreNum').innerText.split('/')[0] : '0',
    w1: document.getElementById('w1') ? document.getElementById('w1').value : '',
    w1r: document.getElementById('w1r') ? document.getElementById('w1r').value : '',
    w2: document.getElementById('w2') ? document.getElementById('w2').value : '',
    w3: document.getElementById('w3') ? document.getElementById('w3').value : '',
    w3t: document.getElementById('w3t') ? document.getElementById('w3t').value : '',
    w4: document.getElementById('w4') ? document.getElementById('w4').value : '',
    dialogue: document.getElementById('myDialogue') ? document.getElementById('myDialogue').value : ''
  };"""

new_data_obj = """
  let quizDetails = [];
  document.querySelectorAll('.quiz-item').forEach((item, index) => {
    let isCorrect = item.classList.contains('correct');
    let isWrong = item.classList.contains('wrong');
    let status = isCorrect ? '✅ Correct' : (isWrong ? '❌ Wrong' : '⚪ Blank');
    quizDetails.push(`Q${index+1}: ${status}`);
  });

  const data = {
    name: name,
    wu1: document.getElementById('wu1') ? document.getElementById('wu1').value : '',
    wu2: document.getElementById('wu2') ? document.getElementById('wu2').value : '',
    wu3: document.getElementById('wu3') ? document.getElementById('wu3').value : '',
    l1: document.getElementById('l1') ? document.getElementById('l1').value : '',
    l2: document.getElementById('l2') ? document.getElementById('l2').value : '',
    l3: document.getElementById('l3') ? document.getElementById('l3').value : '',
    l4: document.getElementById('l4') ? document.getElementById('l4').value : '',
    quizScore: document.getElementById('scoreNum') ? document.getElementById('scoreNum').innerText : '0/5',
    quizDetails: quizDetails.join(' | '),
    sortResult: document.getElementById('sortFeedback') ? document.getElementById('sortFeedback').innerText : '',
    w1: document.getElementById('w1') ? document.getElementById('w1').value : '',
    w1r: document.getElementById('w1r') ? document.getElementById('w1r').value : '',
    w2: document.getElementById('w2') ? document.getElementById('w2').value : '',
    w3: document.getElementById('w3') ? document.getElementById('w3').value : '',
    w3t: document.getElementById('w3t') ? document.getElementById('w3t').value : '',
    w4: document.getElementById('w4') ? document.getElementById('w4').value : '',
    dialogue: document.getElementById('myDialogue') ? document.getElementById('myDialogue').value : ''
  };"""

html = html.replace(old_data_obj, new_data_obj)

with open("class-prep-workplace.html", "w", encoding="utf-8") as f:
    f.write(html)


# 2. Update admin.html
with open("admin.html", "r", encoding="utf-8") as f:
    admin = f.read()

# Add the Answer Key button and modal/section
answer_key_html = """
<button class="btn" onclick="toggleAnswers()" style="background:#2C3E50;color:white;margin-bottom:30px;margin-left:10px">📄 Ver Respuestas Correctas</button>

<div id="answerKey" style="display:none;background:var(--white);border:1.5px solid #DDD5C4;border-radius:16px;padding:30px;margin-bottom:30px;">
  <h2 style="font-family:'Syne',sans-serif;color:var(--amber);margin-top:0">✅ Answer Key (Guía para la Profesora)</h2>
  <div class="answer-block">
    <div class="answer-label">WARM-UP</div>
    <div class="answer-text"><strong>Situation A (Manager):</strong> Algo formal como "That would be wonderful, thank you."<br><strong>Situation B (Coworker):</strong> Algo casual como "Sure, thanks!"<br><strong>Why:</strong> Por la diferencia de jerarquía/confianza y la dificultad de la tarea.</div>
  </div>
  <div class="answer-block">
    <div class="answer-label">LISTENING</div>
    <div class="answer-text">
      <strong>Q1:</strong> "That would be wonderful, thank you so much!" & "I'd really appreciate that, thank you."<br>
      <strong>Q2:</strong> Rejects formatting the presentation slides. Says: "No thanks, I'm good!"<br>
      <strong>Q3:</strong> Because getting coffee is a simple task and they are coworkers (informal).<br>
      <strong>Q4:</strong> "Thank you so much, but I think I can manage". Sounds polite but firm/serious.
    </div>
  </div>
  <div class="answer-block">
    <div class="answer-label">QUIZ & SORTING</div>
    <div class="answer-text">El sistema califica automáticamente (5/5). El sorting también debe decir "Perfect!".</div>
  </div>
</div>

<script>
function toggleAnswers() {
  const el = document.getElementById('answerKey');
  el.style.display = el.style.display === 'none' ? 'block' : 'none';
}
</script>
"""

# Insert answer key right after the refresh button
admin = admin.replace('↻ Actualizar Respuestas</button>', '↻ Actualizar Respuestas</button>' + answer_key_html)

# Update the student card rendering
old_student_card = """<div class="answer-label">Quiz Score</div>
            <div class="answer-text"><strong>${student.quizScore || '0'}/5</strong></div>
          </div>"""

new_student_card = """<div class="answer-label">1. WARM-UP</div>
            <div class="answer-text" style="background:#FFF0D0">
              <strong>Sit A:</strong> ${student.wu1 || '<em>No respondió</em>'}<br>
              <strong>Sit B:</strong> ${student.wu2 || '<em>No respondió</em>'}<br>
              <strong>Why:</strong> ${student.wu3 || '<em>No respondió</em>'}
            </div>
          </div>
          
          <div class="answer-block">
            <div class="answer-label">2. LISTENING COMPREHENSION</div>
            <div class="answer-text" style="background:#D4F0EB">
              <strong>Q1:</strong> ${student.l1 || '<em>No respondió</em>'}<br>
              <strong>Q2:</strong> ${student.l2 || '<em>No respondió</em>'}<br>
              <strong>Q3:</strong> ${student.l3 || '<em>No respondió</em>'}<br>
              <strong>Q4:</strong> ${student.l4 || '<em>No respondió</em>'}
            </div>
          </div>

          <div class="answer-block">
            <div class="answer-label">3. QUIZ & SORT IT OUT</div>
            <div class="answer-text">
              <strong>Quiz Score:</strong> ${student.quizScore || '0/5'}<br>
              <small style="color:#7f8c8d">${student.quizDetails || 'Sin detalles'}</small><br><br>
              <strong>Sort Activity:</strong> ${student.sortResult || '<em>El estudiante no presionó "Check my answers"</em>'}
            </div>
          </div>"""

admin = admin.replace(old_student_card, new_student_card)

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(admin)

print("Admin dashboard completely upgraded with answer key and all sections.")

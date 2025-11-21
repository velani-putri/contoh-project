<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Belajar Bahasa Madura Halus</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f0f0f0; }
    #app { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 8px; }
    button { padding: 10px 20px; margin: 5px; border-radius: 6px; border: none; cursor: pointer; }
    .correct { background: #c7f7c1; }
    .wrong { background: #f7c1c1; }
  </style>
</head>
<body>
  <div id="app">
    <h1>Belajar Bahasa Madura Halus</h1>
    <div id="question"></div>
    <div id="answers"></div>
    <button id="nextBtn" style="display:none">Lanjut</button>
  </div>

  <script>
    const levels = [
      {
        level: 1,
        data: [
          {
            q: "Apa bahasa Madura halus untuk 'makan'?",
            options: ["mangan", "napa", "mèngkèr", "nèpèng"],
            correct: 0
          },
          {
            q: "Apa arti kata 'bâ'en'?",
            options: ["Anda", "Kami", "Dia", "Mereka"],
            correct: 0
          }
        ]
      },
      {
        level: 2,
        data: [
          {
            q: "Bahasa Madura halus dari 'tidur'?",
            options: ["tindhur", "tettor", "toju", "soghut"],
            correct: 0
          },
          {
            q: "Arti kalimat 'Mon bâ'en badha takon'?",
            options: ["Jika Anda mau makan", "Jika Anda ingin bertanya", "Jika Anda tidur", "Jika Anda datang"],
            correct: 1
          }
        ]
      }
    ];

    let currentLevel = 0;
    let currentQuestion = 0;

    function loadQuestion() {
      const level = levels[currentLevel];
      const qData = level.data[currentQuestion];

      document.getElementById("question").innerHTML = `<h2>Level ${level.level}</h2><p>${qData.q}</p>`;

      const ansDiv = document.getElementById("answers");
      ansDiv.innerHTML = "";

      qData.options.forEach((opt, index) => {
        const btn = document.createElement("button");
        btn.textContent = opt;
        btn.onclick = () => checkAnswer(index);
        ansDiv.appendChild(btn);
      });
    }

    function checkAnswer(i) {
      const level = levels[currentLevel];
      const qData = level.data[currentQuestion];
      const btns = document.querySelectorAll("#answers button");

      btns.forEach((b, idx) => {
        if (idx === qData.correct) b.classList.add("correct");
        else if (idx === i) b.classList.add("wrong");
        b.disabled = true;
      });

      document.getElementById("nextBtn").style.display = "block";
    }

    document.getElementById("nextBtn").onclick = () => {
      const level = levels[currentLevel];

      currentQuestion++;
      if (currentQuestion >= level.data.length) {
        currentLevel++;
        currentQuestion = 0;
        if (currentLevel >= levels.length) {
          document.getElementById("app").innerHTML = "<h1>Selamat! Anda telah menyelesaikan semua level.</h1>";
          return;
        }
      }

      document.getElementById("nextBtn").style.display = "none";
      loadQuestion();
    };

    loadQuestion();
  </script>
</body>
</html>

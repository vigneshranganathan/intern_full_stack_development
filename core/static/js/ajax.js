document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("question-form");
  const historyDiv = document.getElementById("history");
  const askBtn = document.getElementById("ask-btn");
  const spinner = document.getElementById("spinner");
  const btnText = document.getElementById("btn-text");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const textarea = form.querySelector("textarea");
    const question = textarea.value.trim();
    if (!question) return;

    // show spinner
    spinner.classList.remove("d-none");
    btnText.textContent = "Thinking...";

    const csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;
    try {
      const resp = await fetch("/ask/", {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({ question_text: question }),
      });
      const data = await resp.json();
      if (resp.ok) {
        // prepend new entry
        const card = document.createElement("div");
        card.className = "card mb-2";
        card.innerHTML = `
          <div class="card-body">
            <strong>Q:</strong> ${data.question}<br/>
            <strong>A:</strong> ${data.answer.replace(/\n/g, "<br/>")}<br/>
            <small class="text-muted">Asked: ${data.created_at} via ${data.plugin}</small>
          </div>
        `;
        historyDiv.prepend(card);
        textarea.value = "";
      } else {
        alert(data.error || "Failed to get answer");
      }
    } catch (err) {
      alert("Network error");
    } finally {
      spinner.classList.add("d-none");
      btnText.textContent = "Ask";
    }
  });
});

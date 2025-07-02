document.addEventListener('DOMContentLoaded', function () {
        const resultDiv = document.getElementById('prediction-result');
        const historyList = document.getElementById('history-list');

        if (resultDiv) {
            const sqft = resultDiv.getAttribute('data-sqft');
            const bedrooms = resultDiv.getAttribute('data-bedrooms');
            const bathrooms = resultDiv.getAttribute('data-bathrooms');
            const price = resultDiv.querySelector('h3').innerText;

            const entry = `📐 ${sqft} sq ft | 🛌 ${bedrooms} BR | 🚿 ${bathrooms} Bath → 💰 ${price}`;

            let history = JSON.parse(localStorage.getItem('predictionHistory')) || [];
            history.push(entry);
            localStorage.setItem('predictionHistory', JSON.stringify(history));
        }

        const savedHistory = JSON.parse(localStorage.getItem('predictionHistory')) || [];
        savedHistory.forEach(entry => {
            const li = document.createElement('li');
            li.textContent = entry;
            historyList.appendChild(li);
        });

        setTimeout(() => {
            if (resultDiv) resultDiv.style.display = 'none';
        }, 20000);

        document.getElementById("about-link").addEventListener("click", function (e) {
            e.preventDefault();
            document.getElementById("home-section").style.display = "none";
            document.getElementById("about-section").style.display = "block";
        });

        document.getElementById("home-link").addEventListener("click", function (e) {
            e.preventDefault();
            document.getElementById("home-section").style.display = "flex";
            document.getElementById("about-section").style.display = "none";
        });
    });
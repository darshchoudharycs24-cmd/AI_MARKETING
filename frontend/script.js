async function analyzeCompetitor() {

    const company = document.getElementById("company").value.trim();
    const industry = document.getElementById("industry").value.trim();
    const country = document.getElementById("country").value.trim();

    const button = document.getElementById("analyzeBtn");
    const buttonText = document.getElementById("buttonText");

    const loading = document.getElementById("loading");
    const error = document.getElementById("error");
    const results = document.getElementById("results");


    // Validate input

    if (!company || !industry || !country) {

        showError("Please fill in all three fields.");

        return;
    }


    // Reset UI

    error.classList.add("hidden");
    results.classList.add("hidden");

    loading.classList.remove("hidden");

    button.disabled = true;
    buttonText.textContent = "Analyzing...";


    try {

        const response = await fetch("/competitor-research", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                company: company,
                industry: industry,
                country: country
            })

        });


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail
                    ? JSON.stringify(data.detail)
                    : "Something went wrong."
            );

        }


        displayResults(data);


    } catch (err) {

        console.error(err);

        showError(
            "Unable to complete the analysis. Please check that the FastAPI server is running."
        );

    } finally {

        loading.classList.add("hidden");

        button.disabled = false;

        buttonText.textContent = "Analyze Competitors";
    }
}


/* DISPLAY RESULTS */

function displayResults(data) {

    const results = document.getElementById("results");

    results.classList.remove("hidden");


    // Company

    document.getElementById("resultCompany").textContent =
        data.company || "Company";


    document.getElementById("resultIndustry").textContent =
        data.industry || "";


    // Competitors

    const competitorsContainer =
        document.getElementById("competitors");

    competitorsContainer.innerHTML = "";


    if (data.competitors && data.competitors.length > 0) {

        data.competitors.forEach(competitor => {

            const card = document.createElement("div");

            card.className = "competitor-card";


            const platforms =
                competitor.social_media_strategy?.main_platforms || [];

            const postingFrequency =
                competitor.social_media_strategy?.posting_frequency || "N/A";

            const brandTone =
                competitor.social_media_strategy?.brand_tone || "N/A";


            card.innerHTML = `

                <h4>${escapeHtml(competitor.name || "Unknown")}</h4>

                <p>
                    ${escapeHtml(competitor.description || "")}
                </p>

                <div class="competitor-info">

                    <div>
                        <strong>Industry:</strong>
                        ${escapeHtml(competitor.industry || "N/A")}
                    </div>

                    <div>
                        <strong>Target Audience:</strong>
                        ${escapeHtml(competitor.target_audience || "N/A")}
                    </div>

                    <div>
                        <strong>Platforms:</strong>
                        ${escapeHtml(platforms.join(", ") || "N/A")}
                    </div>

                    <div>
                        <strong>Posting:</strong>
                        ${escapeHtml(postingFrequency)}
                    </div>

                    <div>
                        <strong>Brand Tone:</strong>
                        ${escapeHtml(brandTone)}
                    </div>

                </div>

            `;

            competitorsContainer.appendChild(card);

        });

    } else {

        competitorsContainer.innerHTML =
            "<p>No competitors found.</p>";

    }


    // Strategy

    const strategy = data.marketing_strategy || {};


    populateList(
        "strengths",
        strategy.strengths
    );

    populateList(
        "weaknesses",
        strategy.weaknesses
    );

    populateList(
        "opportunities",
        strategy.opportunities
    );

    populateList(
        "contentGaps",
        strategy.content_gaps
    );


    // Suggestions

    const suggestions =
        document.getElementById("suggestions");

    suggestions.innerHTML = "";


    if (strategy.suggestions) {

        strategy.suggestions.forEach(item => {

            const div = document.createElement("div");

            div.className = "suggestion";

            div.textContent = item;

            suggestions.appendChild(div);

        });

    }


    // Summary

    document.getElementById("summaryText").textContent =
        data.summary || "No summary available.";


    // Scroll to results

    results.scrollIntoView({
        behavior: "smooth"
    });
}


/* LIST HELPER */

function populateList(elementId, items) {

    const list = document.getElementById(elementId);

    list.innerHTML = "";


    if (!items || items.length === 0) {

        const li = document.createElement("li");

        li.textContent = "No information available.";

        list.appendChild(li);

        return;
    }


    items.forEach(item => {

        const li = document.createElement("li");

        li.textContent = item;

        list.appendChild(li);

    });
}


/* ERROR */

function showError(message) {

    const error = document.getElementById("error");

    error.textContent = message;

    error.classList.remove("hidden");

    error.scrollIntoView({
        behavior: "smooth"
    });
}


/* BASIC HTML ESCAPING */

function escapeHtml(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}
async function analyzeCompetitor() {

    const company = document.getElementById("company").value.trim();
    const industry = document.getElementById("industry").value.trim();
    const country = document.getElementById("country").value.trim();

    const button = document.getElementById("analyzeBtn");
    const buttonText = document.getElementById("buttonText");

    const loading = document.getElementById("loading");
    const error = document.getElementById("error");
    const results = document.getElementById("results");


    if (!company || !industry || !country) {

        showError("Please fill in all three fields.");

        return;
    }


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


/* ================================= */
/* DISPLAY COMPETITOR RESULTS */
/* ================================= */

function displayResults(data) {

    const results = document.getElementById("results");

    results.classList.remove("hidden");


    document.getElementById("resultCompany").textContent =
        data.company || "Company";


    document.getElementById("resultIndustry").textContent =
        data.industry || "";


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
                        ${escapeHtml(
                            competitor.target_audience || "N/A"
                        )}
                    </div>

                    <div>
                        <strong>Platforms:</strong>
                        ${escapeHtml(
                            platforms.join(", ") || "N/A"
                        )}
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


    document.getElementById("summaryText").textContent =
        data.summary || "No summary available.";


    results.scrollIntoView({
        behavior: "smooth"
    });
}


/* ================================= */
/* GENERATE SOCIAL MEDIA POST */
/* ================================= */

async function generatePost() {

    const company =
        document.getElementById("company").value.trim();

    const industry =
        document.getElementById("industry").value.trim();

    const country =
        document.getElementById("country").value.trim();

    const platform =
        document.getElementById("platform").value;


    const button =
        document.getElementById("generatePostBtn");

    const buttonText =
        document.getElementById("generatePostButtonText");

    const loading =
        document.getElementById("postLoading");

    const error =
        document.getElementById("postError");

    const results =
        document.getElementById("postResults");


    /* Validate */

    if (!company || !industry || !country) {

        error.textContent =
            "Please enter Company Name, Industry, and Country first.";

        error.classList.remove("hidden");

        error.scrollIntoView({
            behavior: "smooth"
        });

        return;
    }


    /* Reset */

    error.classList.add("hidden");

    results.classList.add("hidden");

    loading.classList.remove("hidden");

    button.disabled = true;

    buttonText.textContent = "Generating...";


    try {

        const response = await fetch(
            "/api/posts/generate",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    company: company,
                    industry: industry,
                    country: country,
                    platform: platform
                })
            }
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail
                    ? JSON.stringify(data.detail)
                    : "Post generation failed."
            );

        }


        displayPost(data);


    } catch (err) {

        console.error(err);

        error.textContent =
            "Unable to generate the post. " +
            "Please try again.";

        error.classList.remove("hidden");

        error.scrollIntoView({
            behavior: "smooth"
        });

    } finally {

        loading.classList.add("hidden");

        button.disabled = false;

        buttonText.textContent = "Generate Post";

    }
}


/* ================================= */
/* DISPLAY GENERATED POST */
/* ================================= */

function displayPost(data) {

    const results =
        document.getElementById("postResults");

    results.classList.remove("hidden");


    /* Platform */

    document.getElementById("postPlatform").textContent =
        data.platform || "Social Media Post";


    /* Post text */

    document.getElementById("postText").textContent =
        data.post_text ||
        data.content ||
        data.text ||
        "No post content available.";


    /* Caption */

    document.getElementById("postCaption").textContent =
        data.caption ||
        "No caption available.";


    /* Image prompt */

    document.getElementById("imagePrompt").textContent =
        data.image_prompt ||
        data.imagePrompt ||
        "No image concept available.";


    /* Hashtags */

    const hashtagsContainer =
        document.getElementById("postHashtags");

    hashtagsContainer.innerHTML = "";


    const hashtags = data.hashtags || [];


    if (Array.isArray(hashtags)) {

        hashtags.forEach(tag => {

            const span =
                document.createElement("span");

            span.className = "hashtag";

            span.textContent =
                tag.startsWith("#")
                    ? tag
                    : "#" + tag;

            hashtagsContainer.appendChild(span);

        });

    }


    /* Image */

    if (data.image_url) {

        const image =
            document.getElementById("generatedImage");

        let imageUrl = data.image_url;


        /*
         * If backend returns a relative URL,
         * attach it to the current server.
         */

        if (imageUrl.startsWith("/")) {

            imageUrl =
                window.location.origin + imageUrl;

        }


        image.src = imageUrl;


        /* Download */

        const download =
            document.getElementById("downloadImage");

        download.href = imageUrl;

        download.download =
            "ai-marketing-post.png";

        download.style.display =
            "inline-block";

    }


    results.scrollIntoView({
        behavior: "smooth"
    });
}


/* ================================= */
/* LIST HELPER */
/* ================================= */

function populateList(elementId, items) {

    const list =
        document.getElementById(elementId);

    list.innerHTML = "";


    if (!items || items.length === 0) {

        const li =
            document.createElement("li");

        li.textContent =
            "No information available.";

        list.appendChild(li);

        return;
    }


    items.forEach(item => {

        const li =
            document.createElement("li");

        li.textContent = item;

        list.appendChild(li);

    });
}


/* ================================= */
/* COMPETITOR ERROR */
/* ================================= */

function showError(message) {

    const error =
        document.getElementById("error");

    error.textContent = message;

    error.classList.remove("hidden");

    error.scrollIntoView({
        behavior: "smooth"
    });
}


/* ================================= */
/* HTML ESCAPING */
/* ================================= */

function escapeHtml(text) {

    const div =
        document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}
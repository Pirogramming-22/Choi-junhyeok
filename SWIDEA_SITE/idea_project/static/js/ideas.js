function toggleStar(ideaId) {
    fetch(`/ideas/${ideaId}/star/`)
        .then(response => response.json())
        .then(data => {
            const starIcon = document.getElementById(`star-${ideaId}`);
            starIcon.textContent = data.is_starred ? '★' : '☆';
        });
}

function updateInterest(ideaId, change) {
    fetch(`/ideas/${ideaId}/interest/?change=${change}`)
        .then(response => response.json())
        .then(data => {
            const interestCount = document.getElementById(`interest-${ideaId}`);
            interestCount.textContent = data.interest;
        });
}
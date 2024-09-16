var isLoading = false;
var page = 1;

function fetchCinemaSessions() {
    if (isLoading) return;

    isLoading = true;
    var loadingContainer = document.getElementById('loading-container');
    loadingContainer.innerHTML = '<img src="{{ url_for("static", filename="loading.gif") }}" alt="Loading...">';

    fetch('/?page=' + page)
        .then(function(response) {
            return response.text();
        })
        .then(function(html) {
            var cinemaContainer = document.getElementById('cinema-container');
            cinemaContainer.insertAdjacentHTML('beforeend', html);
            isLoading = false;
            page += 1;
        })
        .catch(function() {
            isLoading = false;
        });
}

window.addEventListener('scroll', function() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100 && !isLoading) {
        fetchCinemaSessions();
    }
});

fetchCinemaSessions();

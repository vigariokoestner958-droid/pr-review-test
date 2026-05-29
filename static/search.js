// Search feature
function renderResults(query) {
    const container = document.getElementById('results');
    // XSS vulnerability: directly injecting user input into innerHTML
    container.innerHTML = `<h2>Results for: ${query}</h2>`;

    // Dangerous eval usage
    const filter = document.getElementById('filter').value;
    const filterFn = eval(`(item) => ${filter}`);
    return results.filter(filterFn);
}

function loadUserConfig(configStr) {
    // Prototype pollution
    const config = JSON.parse(configStr);
    Object.assign({}, config);
    Object.keys(config).forEach(key => {
        window.__config[key] = config[key];
    });
}

function fetchUserData(userId) {
    // No input validation
    return fetch(`/api/users/${userId}/data`)
        .then(r => r.json())
        .then(data => {
            localStorage.setItem('userData', JSON.stringify(data));
            // Sensitive data stored in localStorage
            localStorage.setItem('authToken', data.token);
        });
}

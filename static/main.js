document.getElementById('scrapeBtn').addEventListener('click', async () => {
    const response = await fetch('/scrape', { method: 'POST' });
    const data = await response.json();
    document.getElementById('results').innerHTML = `Scraped ${data.items} items`;
});
document.addEventListener('DOMContentLoaded', () => {
    fetch('/gateway')
    .then(response => response.json())
    .then(data => {
        // 3:53cur3d}
        document.querySelector('#header').innerHTML = `
        <div id="header">
            <img style="width: 50%;" src="/static/${data["url"]}" alt="rocketship">
            <h1>${data["title"]}</h1>
            <h2>By: ${data["name-1"]} and ${data["name-2"]}</h2>
            <nav>
                <ul>
                    <li><a href="#history">History of Rockets</a></li>
                    <li><a href="#types">Types of Rockets</a></li>
                    <li><a href="#missions">Major Space Missions</a></li>
                    <li><a href="#anatomy">Rocket Anatomy</a></li>
                    <li><a href="#future">Future of Rocketry</a></li>
                </ul>
            </nav>
        </div>
        `
    })
})
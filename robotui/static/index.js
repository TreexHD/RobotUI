document.addEventListener('DOMContentLoaded', () => {
    CPUFunc();
    RAMFunc();
    StatusFunc();
});

function CPUFunc(data){
    // Set CPU usage dynamically
    let cpuPercentage = data; // Example value
    document.querySelector('.cpu-usage-overall .progress').style.width = cpuPercentage + '%';
    document.querySelector('.cpu-usage-overall .cpu-overall-percentage').textContent = cpuPercentage + '%';
}

function RAMFunc(data){
    // Set RAM usage dynamically
    let ramPercentage = data; // Example value
    document.querySelector('.ram-usage .progress').style.width = ramPercentage + '%';
    document.querySelector('.ram-usage .ram-percentage').textContent = ramPercentage + '%';
}

function StatusFunc(data){
    let status = 'stopped'; // Example values: 'running', 'stopped', 'paused'
    if(data == 1){
        status = 'running'
    }else if(data == 0){
        status = 'stopped'
    }
    // Set status dynamically

    let statusIndicator = document.querySelector('.status-indicator');
    statusIndicator.classList.remove('running', 'stopped', 'paused');
    statusIndicator.classList.add(status);
    statusIndicator.textContent = status.charAt(0).toUpperCase() + status.slice(1);
}

function pressedButton(datas){
    //Send to python if Stop Button pressed
    const data = {value: datas};

    fetch('/btn', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
}

function fetchStatus() {
            fetch('/status')
                .then(response => response.json())
                .then(data => {
                    StatusFunc(data.status.message);
                    CPUFunc(data.status.cpu_load);
                    RAMFunc(data.status.ram_load);
                })
                .catch(error => console.error('Error fetching status:', error));
        }

// Fetch status every 1 seconds
setInterval(fetchStatus, 1000);

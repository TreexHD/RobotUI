document.addEventListener('DOMContentLoaded', () => {
    CPUFunc();
    RAMFunc();
    StatusFunc();
});

function CPUFunc(){
    // Set CPU usage dynamically
    let cpuPercentage = 65; // Example value
    document.querySelector('.cpu-usage-overall .progress').style.width = cpuPercentage + '%';
    document.querySelector('.cpu-usage-overall .cpu-overall-percentage').textContent = cpuPercentage + '%';
}

function RAMFunc(){
    // Set RAM usage dynamically
    let ramPercentage = 50; // Example value
    document.querySelector('.ram-usage .progress').style.width = ramPercentage + '%';
    document.querySelector('.ram-usage .ram-percentage').textContent = ramPercentage + '%';
}

function StatusFunc(){
    // Set status dynamically
    let status = 'running'; // Example values: 'running', 'stopped', 'paused'
    let statusIndicator = document.querySelector('.status-indicator');
    statusIndicator.classList.remove('running', 'stopped', 'paused');
    statusIndicator.classList.add(status);
    statusIndicator.textContent = status.charAt(0).toUpperCase() + status.slice(1);
}

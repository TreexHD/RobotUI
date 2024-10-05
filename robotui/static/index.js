document.addEventListener('DOMContentLoaded', () => {
    CPUFunc();
    RAMFunc();
    StatusFunc();
    ConsoleFunc('[BLUE]Ready...[END]');
    fetch_get_Program();
});

function CPUFunc(data){
    // Set CPU usage dynamically
    let cpuPercentage = data; // Example value
    document.querySelector('.cpu-usage-overall .progress').style.width = cpuPercentage + '%';
    document.querySelector('.cpu-usage-overall .cpu-overall-percentage').textContent = cpuPercentage + '%';
}

function CurrentProgram(data){
    //set the current program that is running
    const currentElement = document.getElementById("current_program");
    currentElement.innerHTML = "Program:" + data
}

function RAMFunc(data){
    // Set RAM usage dynamically
    let ramPercentage = data; // Example value
    document.querySelector('.ram-usage .progress').style.width = ramPercentage + '%';
    document.querySelector('.ram-usage .ram-percentage').textContent = ramPercentage + '%';
}

function scrollToBottom() {
        var consoleWindow = document.querySelector('.console-window');
        consoleWindow.scrollTop = consoleWindow.scrollHeight;
    }

function ConsoleFunc(data) {
    const consoleElement = document.getElementById("console");
    const maxChars = 10000; // Set the maximum number of characters

    // Check for [CLEAR] command
    if (data.includes('[CLEAR]')) {
        consoleElement.innerHTML = '';
        return;
    }

    // Replace color tags with corresponding HTML span elements
    data = data.replace(/\[RED\]/g, '<span style="color: #ff2b1c;">')
               .replace(/\[BLUE\]/g, '<span style="color: #00FFFF;">') // Brighter blue
               .replace(/\[GREEN\]/g, '<span style="color: #7FFF00;">')
               .replace(/\[YELLOW\]/g, '<span style="color: #FFFF00;">')
               .replace(/\[END\]/g, '</span>');

    // Replace newline characters with <br> tags
    data = data.replace(/\n/g, '<br>');

    // Split the data by <br> and add a timestamp to each part
    const parts = data.split('<br>');
    const timestamp = new Date().toLocaleTimeString();
    const formattedParts = parts.map(part => part.trim() ? `${timestamp}: ${part}<br>` : '').filter(part => part);

    // Append new data to the existing content
    if (formattedParts.some(part => part.trim() !== '<br>')) {
        consoleElement.innerHTML += formattedParts.join('');
        // Scroll to bottom
        scrollToBottom();
    }
    // If the content exceeds the maximum number of characters, trim the oldest data
    while (consoleElement.textContent.length > maxChars) {
        // Remove the oldest character
        consoleElement.innerHTML = consoleElement.innerHTML.substring(1);
    }
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

function fetch_get_Program(){
    fetch('/pgm')
        .then(response => response.json())
        .then(data => {
            ProgramAddOptions(data.status.prog);
    })
    .catch(error => console.error('Error fetching programs:', error));

}

function ProgramAddOptions(names) {
    const selectElement = document.getElementById("program-select");
    const options = names.split('!');
    options.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option;
        newOption.text = option;
        selectElement.appendChild(newOption);
    });
}

function ProgramSelectOption(name) {
    const selectElement = document.getElementById("program-select");
    selectElement.value = name;
}


function ProgramGetSelectedOption() {
    const selectElement = document.getElementById("program-select");
    return selectElement.value;
}

function pressedButton(datas){
    //Send to python if Stop Button pressed
    const data = {value: datas,
                  program: ProgramGetSelectedOption()};

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
            ConsoleFunc(data.status.console);
            CurrentProgram(data.status.program)
        })
        .catch(error => console.error('Error fetching status:', error));
}

// Fetch status every 1 seconds
setInterval(fetchStatus, 1000);

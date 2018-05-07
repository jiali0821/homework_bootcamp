var $tbody = document.querySelector("tbody");
var $datatimeInput = document.querySelector("#Date_Time");
var $searchBtn = document.querySelector("#search");

$searchBtn.addEventListener("click", handleSearchButtonClick);

var filteredData = dataSet;


function renderTable() {
    $tbody.innerHTML = "";
    for (var i = 0; i < filteredData.length; i++ ){

        var $row = $tbody.insertRow(i);

        for (var j = 0; j < 7; j++) {

            var $cell = $row.insertCell(j);

            $cell.innerText = Object.values(filteredData[i])[j];
    }
  }
};





function handleSearchButtonClick() {
    
    var filterInput = $datatimeInput.value.trim().toLowerCase();
  
    filteredData_1 = dataSet.filter(function(x) {   
    var fileDate = x.datetime.toLowerCase();
  
      // If true, add the address to the filteredAddresses, otherwise don't add it to filteredAddresses
      return fileDate === filterInput;
    });

    renderTable();
  }


renderTable();
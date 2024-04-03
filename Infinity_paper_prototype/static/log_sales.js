$(document).ready(function() {
    const salesperson = "Naira Altunkeser";
    const salesList = $("#sales-list");
    const localStorageKey = "salesData";

    function displaySalesList(sales) {
        salesList.empty();
        sales.forEach(function(sale) {
            const listItem = $("<li>").addClass("list-group-item").text(`${sale.client} - ${sale.reams} - ${sale.salesperson}`);
            const deleteButton = $("<button>").addClass("btn btn-danger btn-sm float-end delete-btn").text("Delete");
            deleteButton.click(function() {
                deleteSale(sale.id, listItem);
            });
            listItem.append(deleteButton);
            salesList.append(listItem);
            listItem.draggable({ revert: "invalid", cursor: "move" });
        });
    }

    function saveSale(newSale) {
        $.ajax({
            url: '/save_sale',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(newSale),
            success: function(response) {
                displaySalesList(response.sales);
                // Save updated sales data to local storage
                localStorage.setItem(localStorageKey, JSON.stringify(response.sales));
            },
            error: function(xhr, status, error) {
                console.error('Error saving sale:', error);
            }
        });
    }
function getClientList() {
        $.ajax({
            url: '/get_clients', // Define a route in your server.py to handle client list request
            type: 'GET',
            success: function(response) {
                // Initialize autocomplete for client input field
                $("#client").autocomplete({
                    source: response.clients
                });
            },
            error: function(xhr, status, error) {
                console.error('Error getting client list:', error);
            }
        });
    }



    getClientList();

    function deleteSale(id, listItem) {
        $.ajax({
            url: '/delete_sale',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ id: id }),
            success: function(response) {
                listItem.remove(); 
                displaySalesList(response.sales);
                // Save to local storage
                localStorage.setItem(localStorageKey, JSON.stringify(response.sales));
            },
            error: function(xhr, status, error) {
                console.error('Error deleting sale:', error);
            }
        });
    }

    $("#sale-form").submit(function(event) {
        event.preventDefault();
        const client = $("#client").val().trim();
        const reams = $("#reams").val().trim();

        if (client === "" || reams === "" || isNaN(reams)) {
            alert("Please fill all fields with valid data.");
            return;
        }

        const newSale = {
            client: client,
            reams: parseInt(reams),
            salesperson: salesperson
        };

        saveSale(newSale);

        // Clear input fields
        $("#client").val("");
        $("#reams").val("");
    });

    // Initial display of sales from local storage if available
    const storedSales = JSON.parse(localStorage.getItem(localStorageKey));
    if (storedSales) {
        displaySalesList(storedSales);
    }

    // Make trash droppable
   $("#trash").droppable({
        accept: "#sales-list li",
        drop: function(event, ui) {
            const draggedItem = ui.draggable;
            const listItem = draggedItem.closest("li");
            const saleId = draggedItem.find(".delete-btn").data("sale-id");
            deleteSale(saleId, listItem);
        }
    });
});
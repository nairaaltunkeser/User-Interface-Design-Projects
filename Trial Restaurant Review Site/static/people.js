
$(document).ready(function(){
    //when the page loads, display all the names
    displayNames(data)                        

    $("#submit_name").click(function(){                
        get_and_save_name()
    })

    
    $("#new_name").keypress(function(e){     
        if(e.which == 13) {
            get_and_save_name()
        }   
    })

})

$(document).ready(function() {
    $('#addItemForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/add',
            data: $('#addItemForm').serialize(),
            success: function(response) {
                $('#addItemForm')[0].reset(); // Clear the form
                $('#name').focus(); // Set focus to the first input field
                $('#errorMessage').hide(); // Hide any previous error message
                alert(response.success); // Show success message
            },
            error: function(xhr, status, error) {
                $('#errorMessage').text(xhr.responseJSON.error).show(); // Show error message
            }
        });
    });
});

$(document).ready(function() {
    // Handle discard changes button click
    $('#discardChanges').click(function() {
        // Show confirmation dialog
        if (confirm("Are you sure you want to discard changes?")) {
            // If user confirms, redirect to the view page
            window.location.href = "/view/{{ item.id }}";
        }
    });
});


function createRestaurantElement(restaurant) {
    const restaurantElement = document.createElement('div');
    restaurantElement.classList.add('restaurant');
    
    const restaurantName = document.createElement('h3');
    restaurantName.textContent = restaurant.name;
    
    const restaurantLocation = document.createElement('p');
    restaurantLocation.textContent = "Location: " + restaurant.location;
    
    const restaurantSummary = document.createElement('p');
    restaurantSummary.textContent = restaurant.summary;
    
    restaurantElement.appendChild(restaurantName);
    restaurantElement.appendChild(restaurantLocation);
    restaurantElement.appendChild(restaurantSummary);
    
    return restaurantElement;
}

// Function to render popular restaurants on the homepage
function renderPopularRestaurants() {
    const popularRestaurantsContainer = document.getElementById('popularRestaurants');
    turkishRestaurants.forEach(restaurant => {
        const restaurantElement = createRestaurantElement(restaurant);
        popularRestaurantsContainer.appendChild(restaurantElement);
    });
}

// Call the function to render popular restaurants when the page loads
window.onload = renderPopularRestaurants;
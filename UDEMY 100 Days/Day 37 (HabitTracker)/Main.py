#POST / PUT / DELETE REQUESTS
# API --> "Pixela"
    # Habit Tracker, but also tracks INTENSITY

#HTTP REQUESTS
    # GET()
        #requests.get()
        ## Asking the External System for some sort of data
    # POST()
        #requests.post()
        ## We give the external system a piece of data - not really interested in the response (just whether it was successful or not). E.g. a Tweet.
    # PUT()
        #requests.put()
        ## Simply update a piece of data - E.G. Adding to Google Sheets 
    # DELETE()
        #requests.delete()
        ## Delete data in external service --> E.G. a Tweet will be deleted 
        
        
## API DOCUMENTATION FOR PIXELA
# Required and not


# THIS MEANS YOU CAN CREATE YOUR OWN API KEY --> between 8 and 128 characters. Must be kept to authenticate.
#[required] A token string used to authenticate as a user to be created. The token string is hashed and saved.
#Validation rule: [ -~]{8,128}



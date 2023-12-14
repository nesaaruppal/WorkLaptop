##### CSS #####
    #Cascading Style Sheets
    
# Adding CSS

##### INLINE #####
# SINGLE ELEMENT
#tag style="css"/>
    # Goes into the same line as a CSS element
    # E.G.
        # <html style="background:blue">
        # </html>
        # "property you want to change: value of property"
        # "background:blue"
        

##### INTERNAL #####
# SINGLE WEBPAGE
#<style>css</style>
    # Add the CSS style code inbetween 
    # Different because it's not inline with a particular CSS element 
    # This can apply to ANYTHING
    # Add a SELECTOR --> E.G. "html"
    # html {
        #background:red;
    #}
        # Good for ONE HTML document 
        # Not great for multiple pages 

##### EXTERNAL #####
# ENTIRE WEBSITE 
#link href="style.css"/>



##### INLINE #####
    #<body>
    #<h1 style = "color:blue;">TEXT</h1>
    #</body>
    
##### INTERNAL #####
    # <head>
    
        #<style>
        # h1 {
            #color:red;
        #}
        #</style>
        
    # <body>
    # <h1> STYLE MY IN RED!</h1>
    # </body>
    
    # </head>
    
##### EXTERNAL #####
    #<!DOCTYPE html>
    
    # <head> 
        # <meta charset = "URF-8">
        # <title> EXTERNAL </title>
        # <link rel="stylesheet" href=".\style.css"/>
    # </head>
    
    #<body>
        #<h1>STYLE ME IN GREEN</h1>
    #</body>
    
    #</html>
    
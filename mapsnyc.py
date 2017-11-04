# importing folium for maps and pandas for csv files
import folium
import pandas as pd

# function that sets markers on the map if the user wishes set them manually
def markers(newMap):

        flag = True

        while flag:
            
            decision = str(input("Do you want to place a marker? (y/n): "))
            
            if (decision == "y"):
                
                lat = input("\nEnter the lattitude: ")
                lon = input("Enter the longitude: ")
                
                popup = str(input("Enter name of the popup: "))
                
                folium.Marker(location = [lat,lon], popup = popup).add_to(newMap)       
                
                print("Marker has been placed. \n")
        
            else:
                                
                print("Please find your map in the folder. Thank you.")
                flag = False
        

# Function that decides to set markers on the location based on the CSV file
# It happens automatically.
def importCSV(newMap):
    
        cuny = pd.read_csv("cunyLocations.csv")
        
        for index, row in cuny.iterrows():
            
            lat = row["Latitude"]
            lon = row["Longitude"]
            
            name = row["Campus"]
            
            folium.Marker([lat, lon], popup = name).add_to(newMap)
        
        
        #folium.Marker(location = [40.768731,-73.964915], popup = "Hunter College").add_to(newMap)
        #folium.Marker([])


# Function that saves the map as an HTML file in the same directory as the program
def save(name):
    
        name.save(outfile = "NYCmap.html")    

# Main function that creates the map and asks the user for their decision.
def main():
    
    newMap = folium.Map( location = [40.75,-74.125], zoom_start = 10)
    
    decision = str(input("Do you want to import locations from the CSV file? (y/n): "))
    
    if (decision == "n"):
        
        decEnter = str(input("Do you want to enter your own data? (y/n): "))
        
        if (decEnter == "y"):
            
            markers(newMap)
    
            save(newMap)
            
        else:
            
            print("Thank you, Goodbye.")
    
    else:
        
        importCSV(newMap)
        save(newMap)

# Invoking main method    
main()

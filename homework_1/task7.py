#Pip packages 
import matplotlib.pyplot as plt

#Creates  cool triangl with matplotlib and saves it as a png
def create_triangle_image(filename="triangle.png"):

    #Define the triangle vertices.
    x = [0, 1, 0.5, 0]  # Starting at (0,0), to (1,0), to (0.5,0.8), back to (0,0)
    y = [0, 0, 0.8, 0]

    #Create a new figure.
    plt.figure()
    
    #Plot the triangle with markers at the vertices.
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    
    #Add a title and set limits
    plt.title("Cool Triangle")
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.5, 1.5)
    
    #Save the figure as an image file.
    plt.savefig(filename)
    plt.close()
    
    return filename

#Runs it all
if __name__ == "__main__":
    image_file = create_triangle_image()
    print(f"Triangle image created: {image_file}")

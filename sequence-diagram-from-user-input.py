from flowdiagram import Diagram

# Path to your flow text file
flow_file = 'sequence_flow.txt'

# Create a Diagram instance
diagram = Diagram()

# Read the flow text file
diagram.read_file(flow_file)

# Generate and save the sequence diagram as an image
diagram.save('sequence_diagram.png')
